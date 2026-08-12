# MITRE ATT&CK Quick Reference — IA 645

Full framework: https://attack.mitre.org

---

## Tactics and Techniques Relevant to This Course

### Initial Access (TA0001)
- T1078 — Valid Accounts
- T1110 — Brute Force

### Credential Access (TA0006)
- T1110.001 — Password Guessing
- T1110.003 — Password Spraying
- T1110.004 — Credential Stuffing

### Lateral Movement (TA0008)
- T1021 — Remote Services
- T1078 — Valid Accounts

### Exfiltration (TA0010)
- T1041 — Exfiltration Over C2 Channel
- T1048 — Exfiltration Over Alternative Protocol

### Defense Evasion (TA0005)
- T1078 — Valid Accounts
- T1070 — Indicator Removal

---

## Technique to Detection Mapping

| Technique | What to Look For | Data Source |
|-----------|-----------------|-------------|
| Brute Force (T1110) | High failed login count from one IP | Auth log |
| Password Spraying (T1110.003) | One password, many usernames | Auth log |
| Credential Stuffing (T1110.004) | Many usernames from many IPs | Auth log |
| Off-hours access | Logins outside business hours | Auth log |
| Lateral movement | Auth events across multiple internal hosts | Auth log, network log |
| Data exfiltration | Outlier bytes transferred per session | Network log |
