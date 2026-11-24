"""
IA 645 — Lab 6
Data ingestion script: loads security_events.db and indexes into Elasticsearch

Run this from your base course container (JupyterLab) AFTER starting ELK with start_elk.bat
"""

import sqlite3
import json
import urllib.request
import urllib.error
from datetime import datetime

DB_PATH = "/course/week5/datasets/security_events/security_events.db"
ES_URL = "http://host.docker.internal:9200"  # connects from container to host ELK

def check_elasticsearch():
    try:
        req = urllib.request.urlopen(f"{ES_URL}", timeout=5)
        data = json.loads(req.read())
        print(f"Elasticsearch is running — cluster: {data.get('cluster_name', 'unknown')}")
        return True
    except Exception as e:
        print(f"Cannot reach Elasticsearch: {e}")
        print("Make sure start_elk.bat is running before executing this script")
        return False

def index_documents(index_name, records, field_names):
    success = 0
    errors = 0
    for i, record in enumerate(records):
        doc = dict(zip(field_names, record))
        # Fix timestamp for Kibana time series
        if 'timestamp' in doc and doc['timestamp']:
            try:
                dt = datetime.strptime(doc['timestamp'], "%Y-%m-%d %H:%M:%S")
                doc['@timestamp'] = dt.strftime("%Y-%m-%dT%H:%M:%SZ")
            except:
                doc['@timestamp'] = doc['timestamp']
        payload = json.dumps(doc).encode('utf-8')
        req = urllib.request.Request(
            f"{ES_URL}/{index_name}/_doc/{i+1}",
            data=payload,
            headers={'Content-Type': 'application/json'},
            method='PUT'
        )
        try:
            urllib.request.urlopen(req, timeout=10)
            success += 1
        except Exception as e:
            errors += 1
        if (i+1) % 100 == 0:
            print(f"  Indexed {i+1} records...")
    return success, errors

def delete_index(index_name):
    req = urllib.request.Request(
        f"{ES_URL}/{index_name}",
        method='DELETE'
    )
    try:
        urllib.request.urlopen(req, timeout=5)
        print(f"  Deleted existing index: {index_name}")
    except:
        pass  # Index didn't exist, that's fine

def main():
    print("IA 645 — Lab 6 ELK Ingestion Script")
    print("=" * 40)

    if not check_elasticsearch():
        return

    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()

    # Index auth_log
    print("\nIndexing auth_log → ia645-auth...")
    delete_index("ia645-auth")
    c.execute("SELECT timestamp, username, source_ip, hostname, event_type, auth_method, port FROM auth_log")
    records = c.fetchall()
    fields = ["timestamp", "username", "source_ip", "hostname", "event_type", "auth_method", "port"]
    success, errors = index_documents("ia645-auth", records, fields)
    print(f"  auth_log: {success} indexed, {errors} errors (expected: {len(records)})")

    # Index network_log
    print("\nIndexing network_log → ia645-network...")
    delete_index("ia645-network")
    c.execute("SELECT timestamp, username, src_ip, dst_ip, protocol, bytes_out, bytes_in, duration_sec, dst_port FROM network_log")
    records = c.fetchall()
    fields = ["timestamp", "username", "src_ip", "dst_ip", "protocol", "bytes_out", "bytes_in", "duration_sec", "dst_port"]
    success, errors = index_documents("ia645-network", records, fields)
    print(f"  network_log: {success} indexed, {errors} errors (expected: {len(records)})")

    conn.close()

    print("\nVerifying record counts in Elasticsearch...")
    for index in ["ia645-auth", "ia645-network"]:
        try:
            req = urllib.request.urlopen(f"{ES_URL}/{index}/_count", timeout=5)
            data = json.loads(req.read())
            print(f"  {index}: {data.get('count', '?')} documents")
        except Exception as e:
            print(f"  {index}: could not verify — {e}")

    print("\nIngestion complete.")
    print("Open Kibana at http://localhost:5601 to build your dashboard.")
    print("In Kibana: Stack Management → Data Views → Create data view")
    print("  Index pattern: ia645-auth | Timestamp field: @timestamp")
    print("  Index pattern: ia645-network | Timestamp field: @timestamp")

if __name__ == "__main__":
    main()
