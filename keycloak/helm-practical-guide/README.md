# Keycloak Helm Practical Guide

Helm, 외부 RDS, TLS, Realm 설정을 포함한 Keycloak 배포 예제입니다.

---

## 📎 관련 아티클

- [Keycloak Helm 설치 방법: values.yaml로 RDS, 인증서, Realm까지 설정하기](https://tistory-cloud.tistory.com/entry/Keycloak-Helm-%EC%84%A4%EC%B9%98-%EB%B0%A9%EB%B2%95-valuesyaml%EB%A1%9C-RDS-%EC%9D%B8%EC%A6%9D%EC%84%9C-Realm%EA%B9%8C%EC%A7%80-%EC%84%A4%EC%A0%95%ED%95%98%EA%B8%B0)
- [Keycloak 운영 방법: 인증서 갱신, 백업, 업그레이드, 장애 대응 체크리스트](https://tistory-cloud.tistory.com/entry/Keycloak-%EC%9A%B4%EC%98%81-%EB%B0%A9%EB%B2%95-%EC%9D%B8%EC%A6%9D%EC%84%9C-%EA%B0%B1%EC%8B%A0-%EB%B0%B1%EC%97%85-%EC%97%85%EA%B7%B8%EB%A0%88%EC%9D%B4%EB%93%9C-%EC%9E%A5%EC%95%A0-%EB%8C%80%EC%9D%91-%EC%B2%B4%ED%81%AC%EB%A6%AC%EC%8A%A4%ED%8A%B8)

---

## ✅ 이 예제가 보여주는 것

- Helm wrapper 차트로 Keycloak을 배포하는 방법
- 외부 RDS, TLS, Realm 설정을 values.yaml로 관리하는 방법
- 개발/프로덕션 환경별 values 파일 분리 전략
- Kubernetes Secret을 별도로 생성하는 방법

## 📦 업스트림 버전

| 항목 | 버전 |
| --- | --- |
| Helm chart | `bitnami/keycloak` `25.3.2` |
| Keycloak app | `26.3.3` |
| Keycloak image | `docker.io/bitnami/keycloak:26.3.3-debian-12-r0` |
| Config CLI image | `docker.io/bitnami/keycloak-config-cli:6.4.0-debian-12-r11` |

---

## 📁 폴더 구조

| 경로 | 설명 |
| --- | --- |
| `Chart.yaml` | Wrapper 차트 정의 |
| `values.yaml` | 플레이스홀더가 포함된 기본 values |
| `values/values-dev.example.yaml` | 개발 환경 예제 |
| `values/values-prod.example.yaml` | 프로덕션 환경 예제 |
| `realm/` | Realm import 예제 |
| `secrets/README.md` | Secret 생성 예제 |
| `docs/install-checklist.md` | 배포 및 검증 체크리스트 |

---

## 🚀 빠른 시작

```bash
git clone https://github.com/yechan-cloudlab/cloud-public.git
cd cloud-public/keycloak/helm-practical-guide
helm dependency update
cp values/values-prod.example.yaml values-prod.yaml
# values-prod.yaml 열고 모든 {{PLACEHOLDER}} 값을 교체
helm install keycloak . -f values-prod.yaml
```

---

## ⚠️ 사용 전 확인

- 모든 `{{PLACEHOLDER}}` 값을 환경에 맞게 교체해야 합니다.
- 비밀번호는 values 파일에 직접 입력하지 말고 Kubernetes Secret으로 별도 생성하세요.
- 배포 전 TLS 종료 위치(Ingress vs 내부)를 결정하세요. 프로덕션 예제는 Ingress에서 TLS 종료를 가정합니다.
- 배포 전 `docs/install-checklist.md`를 반드시 검토하세요.

> 이 예제에서 사용하는 플레이스홀더: `{{KEYCLOAK_DOMAIN}}`, `{{RDS_HOST}}`, `{{TLS_SECRET_NAME}}`, `{{KEYCLOAK_DB_SECRET_NAME}}`, `{{KEYCLOAK_ADMIN_SECRET_NAME}}`  
> 이 값들은 Helm이 자동으로 렌더링하지 않으므로 배포 전에 직접 교체해야 합니다.
