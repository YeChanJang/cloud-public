# cloud-public

Public examples and reference files for the [tistory-cloud blog](https://tistory-cloud.tistory.com/).

This repository collects practical configuration examples that accompany blog posts.
Each topic lives in its own folder so the examples can stay focused, reusable, and safe to publish.

## Topics

- `keycloak/helm-practical-guide/` - Helm-based Keycloak deployment examples for production-oriented configuration

## Repository policy

- Example files use `{{PLACEHOLDER}}` values where environment-specific data is required.
- Secrets, passwords, private keys, and real production endpoints are never committed.
- Files ending with `.example.yaml` are templates for readers to copy and adapt before deployment.
