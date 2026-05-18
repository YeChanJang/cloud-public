# Route 53 Resolver Query Log Suspicious Domain Report

| Score | Instance ID | Query Name | Type | RCODE | Count | Reasons |
|---:|---|---|---|---|---:|---|
| 5 | i-0123456789abcdef0 | moneropool.example | A | NOERROR | 12 | known suspicious domain |
| 2 | i-0fedcba9876543210 | does-not-exist-001.example | A | NXDOMAIN | 42 | high NXDOMAIN volume |
| 2 | i-0123456789abcdef0 | random-long-subdomain-9f3a2b7c4d8e.example | TXT | NOERROR | 18 | high TXT volume |

## Notes
- DNS query logs indicate lookups, not confirmed network connections.
- Findings should be validated with additional telemetry such as VPC Flow Logs, proxy logs, or endpoint telemetry.
