# Private EKS Helm Deployment with GitHub Actions

Self-hosted GitHub Actions runner를 통해 Private Amazon EKS 클러스터에 Helm 차트를 배포하는 예제입니다.

---

## 📎 관련 아티클

- [GitHub Actions로 Private EKS에 Helm 배포 자동화하는 방법: self-hosted runner 구성부터 배포까지](https://tistory-cloud.tistory.com/entry/GitHub-Actions%EB%A1%9C-Private-EKS%EC%97%90-Helm-%EB%B0%B0%ED%8F%AC-%EC%9E%90%EB%8F%99%ED%99%94%ED%95%98%EB%8A%94-%EB%B0%A9%EB%B2%95-self-hosted-runner-%EA%B5%AC%EC%84%B1%EB%B6%80%ED%84%B0-%EB%B0%B0%ED%8F%AC%EA%B9%8C%EC%A7%80)

---

## ✅ 이 예제가 보여주는 것

- Private EKS에 배포 트래픽이 VPC 내부에서 와야 하는 이유
- Self-hosted runner가 VPC 내부에서 GitHub Actions 작업을 실행하는 방법
- OIDC로 장기 AWS 액세스 키 없이 인증하는 방법
- 배포 전 Helm 검증을 실행해야 하는 이유

---

## 📁 폴더 구조

| 경로 | 설명 |
| --- | --- |
| `.github/workflows/deploy-private-eks.yaml` | 배포 워크플로우 |
| `chart/` | 최소 샘플 Helm 차트 |
| `values/` | Dev/Prod values 예제 |
| `runner/` | Self-hosted runner 설정 가이드 |
| `docs/` | 아키텍처, 사전 조건, 인증, 트러블슈팅, 체크리스트 |

---

## 🚀 빠른 시작

1. Private EKS 클러스터를 준비합니다.
2. 클러스터 private 엔드포인트에 접근 가능한 네트워크에 self-hosted runner를 배치합니다.
3. GitHub OIDC와 워크플로우용 IAM 역할을 설정합니다.
4. 아래 GitHub Secret을 추가합니다:
   - `AWS_ROLE_TO_ASSUME`
   - `EKS_CLUSTER_NAME`
5. 워크플로우를 수동으로 실행하고 `dev` 또는 `prod`를 선택합니다.

---

## ⚠️ 사용 전 확인

- Runner가 Kubernetes API private 엔드포인트에 접근 가능한지 확인하세요.
- Runner는 격리된 환경에서 운영하고 신뢰할 수 있는 배포 인프라로 취급하세요.
- 프로덕션 워크플로우 실행 전 IAM 권한을 반드시 검토하세요.
