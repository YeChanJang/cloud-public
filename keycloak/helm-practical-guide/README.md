# Keycloak Helm practical guide

This folder is a small wrapper chart that lets readers clone this repository and deploy Keycloak from the examples used in the blog series.

## Upstream used by this guide

- Upstream Helm chart: `bitnami/keycloak`
- Upstream chart version: `25.3.2`
- Keycloak app version: `26.3.3`
- Keycloak image: `docker.io/bitnami/keycloak:26.3.3-debian-12-r0`
- Keycloak config CLI image from the upstream chart: `docker.io/bitnami/keycloak-config-cli:6.4.0-debian-12-r11`

The upstream chart is consumed as a Helm dependency. This repository keeps the deployment-facing overrides and article examples close together without copying the full upstream chart source.

## What is included

- `Chart.yaml` - wrapper chart that depends on the upstream Bitnami Keycloak chart
- `values.yaml` - default wrapper values with placeholders
- `values/values-dev.example.yaml` - a small development-oriented example
- `values/values-prod.example.yaml` - a production-oriented example using placeholders
- `realm/demo-realm-realm.json` - a minimal realm example
- `realm/realm-configmap.example.yaml` - ConfigMap example for declarative realm configuration
- `secrets/README.md` - Secret creation examples
- `docs/install-checklist.md` - deployment and verification checklist

## Quick start

```bash
git clone https://github.com/YeChanJang/cloud-public.git
cd cloud-public/keycloak/helm-practical-guide
helm dependency update
cp values/values-prod.example.yaml values-prod.yaml
# edit values-prod.yaml and replace every {{PLACEHOLDER}}
helm install keycloak . -f values-prod.yaml
```

## Before you deploy

1. Replace every `{{PLACEHOLDER}}` value with your own environment-specific value.
2. Create Kubernetes Secrets separately. Do not hard-code passwords into values files.
3. Decide where TLS terminates before deployment. The production example assumes TLS terminates at Ingress.
4. Review the checklist in `docs/install-checklist.md`.

## Placeholder rule

The public files in this folder intentionally use placeholders such as:

- `{{KEYCLOAK_DOMAIN}}`
- `{{RDS_HOST}}`
- `{{TLS_SECRET_NAME}}`
- `{{KEYCLOAK_DB_SECRET_NAME}}`
- `{{KEYCLOAK_ADMIN_SECRET_NAME}}`

These placeholders are not rendered automatically by Helm. Replace them before deployment.
