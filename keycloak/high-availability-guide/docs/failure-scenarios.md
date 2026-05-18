# Failure Scenarios

| Scenario | Expected behavior | What must already be true |
|---|---|---|
| One Keycloak Pod fails | Login should continue through another healthy Pod | `replicaCount >= 2`, service routing, readiness probes |
| One node fails | Pods should remain available on another node | anti-affinity or spread, enough node capacity |
| One AZ loses capacity | Service should continue in another AZ | multi-AZ nodes, spread constraints, healthy database path |
| Rolling update starts | At least one Pod should stay available | readiness probe, startup probe, PDB, safe rollout settings |
| Database instance fails | Keycloak should reconnect after failover | external DB HA such as Multi-AZ, tested failover behavior |

## Notes

- More replicas do not remove every single point of failure.
- Database availability is often more important than adding a third application Pod.
- Session behavior should be tested together with application login flows, not only Pod status.
- A single Kubernetes cluster can still remain a control-plane-level failure domain.
