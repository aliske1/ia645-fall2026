# SQL Threat Hunting Cheat Sheet — IA 645

## Brute Force Detection
```sql
SELECT source_ip, COUNT(*) as failed_attempts
FROM auth_log
WHERE event_type = 'FAILED'
GROUP BY source_ip
HAVING COUNT(*) > 10
ORDER BY failed_attempts DESC;
```

## Credential Stuffing Detection
```sql
SELECT source_ip, COUNT(DISTINCT username) as unique_users
FROM auth_log
WHERE event_type = 'FAILED'
GROUP BY source_ip
HAVING COUNT(DISTINCT username) > 5
ORDER BY unique_users DESC;
```

## Off-Hours Access Detection
```sql
SELECT username, source_ip, timestamp
FROM auth_log
WHERE event_type = 'SUCCESS'
AND (CAST(strftime('%H', timestamp) AS INTEGER) < 7
     OR CAST(strftime('%H', timestamp) AS INTEGER) > 19)
ORDER BY timestamp;
```

## Multiple Location Detection
```sql
SELECT username, COUNT(DISTINCT source_ip) as ip_count
FROM auth_log
WHERE event_type = 'SUCCESS'
GROUP BY username
HAVING COUNT(DISTINCT source_ip) > 2
ORDER BY ip_count DESC;
```

## Data Exfiltration Detection
```sql
SELECT session_id, username, bytes_out
FROM network_log
ORDER BY bytes_out DESC
LIMIT 20;
```

## Privilege Escalation Detection
```sql
SELECT a.username, a.timestamp as failed_login, r.timestamp as role_change, r.new_role
FROM auth_log a
JOIN role_changes r ON a.username = r.username
WHERE a.event_type = 'FAILED'
AND ABS(JULIANDAY(r.timestamp) - JULIANDAY(a.timestamp)) < 1
ORDER BY a.timestamp;
```
