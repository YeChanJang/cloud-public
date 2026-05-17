# Architecture

1. The workload runs on EKS.
2. The CloudWatch Observability add-on injects auto instrumentation into supported workloads.
3. Metrics and traces flow through the CloudWatch agent.
4. Application Signals renders service health, dependencies, and SLO-oriented views in CloudWatch.
