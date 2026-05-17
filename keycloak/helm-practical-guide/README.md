# Keycloak Helm practical guide

A deployable wrapper chart for installing **Keycloak** with Helm, external RDS, TLS, and realm configuration examples.

## Related articles

- [Keycloak Helm 설치 방법: values.yaml로 RDS, 인증서, Realm까지 설정하기](https://tistory-cloud.tistory.com/entry/Keycloak-Helm-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-valuesyaml%EB%A1%9C-RDS-%EC%9D%B8%EC%A6%9D%EC%84%9C-Realm%EA%B9%8C%EC%A7%80-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)
- [Keycloak 운영 방법: 인증서 갱신, 백업, 업그레이드, 장애 대응 체크리스트](https://tistory-cloud.tistory.com/entry/Keycloak-%EC%9A%B4%EC%98%81-%EB%B0%A9%EB%B2%95-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EA%B0%B1%EC%8B%A0-%EB%B0%B1%EC%97%85-%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C-%EC%9E%A5%EC%95%A0-%EB%8C%80%EC%9D%91-%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8)

## Upstream used by this guide

| Item | Version |
| --- | --- |
| Helm chart | `bitnami/keycloak` `25.3.2` |
| Keycloak app | `26.3.3` |
| Keycloak image | `docker.io/bitnami/keycloak:26.3.3-debian-12-r0` |
| Config CLI image | `docker.io/bitnami/keycloak-config-cli:6.4.0-debian-12-r11` |

The upstream chart is consumed as a Helm dependency. This repository keeps deployment-facing overrides and article examples close together without copying the full upstream chart source.

## Folder map

| Path | Purpose |
| --- | --- |
| `Chart.yaml` | Wrapper chart definition |
| `values.yaml` | Default wrapper values with placeholders |
| `values/values-dev.example.yaml` | Development-oriented example |
| `values/values-prod.example.yaml` | Production-oriented example |
| `realm/` | Realm import examples |
| `secrets/README.md` | Secret creation examples |
| `docs/install-checklist.md` | Deployment and verification checklist |

## Quick start

```bash
git clone https://github.com/yechan-cloudlab/cloud-public.git
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
4. Review `docs/install-checklist.md` before applying the chart.

## Placeholder rule

Public examples intentionally use placeholders such as:

- `{{KEYCLOAK_DOMAIN}}`
- `{{RDS_HOST}}`
- `{{TLS_SECRET_NAME}}`
- `{{KEYCLOAK_DB_SECRET_NAME}}`
- `{{KEYCLOAK_ADMIN_SECRET_NAME}}`

These placeholders are not rendered automatically by Helm. Replace them before deployment.
