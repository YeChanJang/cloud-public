# CloudWatch Application Signals on EKS

A small reproducible example for enabling **CloudWatch Application Signals** on EKS and checking application-level latency, errors, and dependencies.

- Related article: [CloudWatch Application Signals 사용법](https://tistory-cloud.tistory.com/entry/CloudWatch-Application-Signals-%EC%82%AC%EC%9A%A9%EB%B2%95-EKS-%EC%95%A0%ED%94%8C%EB%A6%AC%EC%BC%80%EC%9D%B4%EC%85%98-%EC%A7%80%EC%97%B0%EA%B3%BC-%EC%98%A4%EB%A5%98%EB%A5%BC-%EC%9E%90%EB%8F%99%EC%9C%BC%EB%A1%9C-%ED%99%95%EC%9D%B8%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95)

## What this example shows

- How Application Signals complements infrastructure monitoring
- What to verify before enabling automatic instrumentation
- How to install, validate, and review the setup

## Folder map

| Path | Purpose |
| --- | --- |
| `manifests/` | Minimal sample workload |
| `commands/` | Install, verification, and enablement notes |
| `docs/` | Architecture, comparisons, metrics, checklist, troubleshooting |
| `images/` | Simple architecture diagram |

## Quick start

1. Install the CloudWatch Observability EKS add-on.
2. Deploy the sample workload in `manifests/`.
3. Enable monitoring for the workload or namespace.
4. Verify Application Signals data in CloudWatch.

## Before you use it

- Review any existing OpenTelemetry setup before enabling Application Signals.
- Application Signals on EKS supports Java, Python, Node.js, and .NET workloads.
- Application Signals is not supported on EKS Windows nodes.
