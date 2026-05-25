# eks-manifest-auditor v0.2 프로그램 설명서

## 1. 프로그램 개요

`eks-manifest-auditor`는 Kubernetes/EKS Manifest YAML 파일을 로컬에서 정적 분석하는 Python 기반 CLI 도구입니다.

실제 AWS 계정, EKS 클러스터, kubeconfig에 연결하지 않고 YAML 파일만 읽어서 보안, 리소스, 운영 안정성 관련 문제를 탐지합니다.

이 도구의 목적은 배포 이후 문제가 발생한 뒤 확인하는 것이 아니라, 배포 전에 Manifest 수준에서 발견 가능한 위험을 미리 찾는 것입니다.

## 2. 주요 특징

- AWS API 호출 없음
- EKS 클러스터 연결 없음
- kubeconfig 사용 없음
- 로컬 YAML 파일만 분석
- 단일 YAML 파일과 디렉터리 스캔 지원
- 여러 Kubernetes 리소스가 들어 있는 multi-document YAML 처리
- 콘솔, JSON, Markdown 리포트 출력
- CI/CD에서 사용할 수 있는 `--fail-on` 실패 기준 지원

## 3. v0.2 기준 검사 항목

### Workload 검사

대상:

- Deployment
- StatefulSet
- DaemonSet

검사 항목:

- `resources.requests` 누락
- `resources.limits` 누락
- `latest` 이미지 태그 사용
- image tag 미지정
- `replicas` 값이 1 이하인 경우
- `readinessProbe` 누락
- `livenessProbe` 누락
- `startupProbe` 누락

### Security 검사

검사 항목:

- `privileged: true`
- `hostPath` volume 사용
- `default` namespace 사용
- `allowPrivilegeEscalation: true`
- `runAsNonRoot` 미설정
- `readOnlyRootFilesystem` 미설정
- 위험 Linux capabilities 사용
- `capabilities.drop: ["ALL"]` 미설정
- `seccompProfile` 미설정
- `runAsUser: 0` 설정

### Service 검사

검사 항목:

- `Service type: LoadBalancer`
- `NodePort` 사용

### Ingress 검사

검사 항목:

- Ingress annotation 목록 출력
- ingress class annotation 확인

### IRSA 검사

검사 항목:

- ServiceAccount의 `eks.amazonaws.com/role-arn` annotation 존재 여부 확인

## 4. v0.2에서 개선된 점

v0.2에서는 v0.1보다 운영 환경에서 더 자주 보는 항목을 추가했습니다.

추가된 주요 기능:

- 헬스체크 검사 추가
- 컨테이너 보안 하드닝 검사 추가
- `--fail-on` 옵션 추가
- cluster-scoped 리소스 default namespace 오탐 수정
- 테스트 케이스 확장

특히 `IngressClass`, `ValidatingWebhookConfiguration`, `MutatingWebhookConfiguration` 같은 cluster-scoped 리소스는 namespace가 없기 때문에 `default namespace` 경고를 발생시키지 않도록 수정했습니다.

## 5. 기본 실행 방법

저장소를 내려받습니다.

```bash
git clone https://github.com/yechan-cloudlab/cloud-public.git
cd cloud-public/eks-manifest-auditor
```

가상환경을 만들고 의존성을 설치합니다.

```bash
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
```

PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -e ".[dev]"
```

예제 디렉터리 스캔:

```bash
eks-manifest-auditor scan ./examples
```

특정 YAML 파일 스캔:

```bash
eks-manifest-auditor scan ./manifests/app.yaml
```

JSON 리포트 생성:

```bash
eks-manifest-auditor scan ./examples --output json --file report.json
```

Markdown 리포트 생성:

```bash
eks-manifest-auditor scan ./examples --output markdown --file report.md
```

## 6. CI 실패 기준

`--fail-on` 옵션은 특정 severity 이상의 finding이 있을 때 CLI를 실패 처리합니다.

예:

```bash
eks-manifest-auditor scan ./manifests --fail-on HIGH
```

동작:

| 옵션 | 실패 조건 |
|---|---|
| `--fail-on HIGH` | HIGH finding이 1개 이상이면 실패 |
| `--fail-on MEDIUM` | MEDIUM 또는 HIGH finding이 있으면 실패 |
| `--fail-on LOW` | LOW, MEDIUM, HIGH finding이 있으면 실패 |

이 기능은 GitHub Actions, Jenkins, GitLab CI 같은 CI/CD 환경에서 배포 전 검증 기준으로 사용할 수 있습니다.

## 7. 출력 결과 구조

각 finding은 아래 정보를 포함합니다.

- `severity`
- `check_id`
- `resource_kind`
- `resource_name`
- `namespace`
- `message`
- `recommendation`
- `file_path`

예시:

```json
{
  "severity": "MEDIUM",
  "check_id": "WORKLOAD_MISSING_RESOURCE_LIMITS",
  "resource_kind": "Deployment",
  "resource_name": "ingress-nginx-controller",
  "namespace": "ingress-nginx",
  "message": "Container 'controller' is missing resources.limits.",
  "recommendation": "Set CPU and memory limits for predictable runtime behavior.",
  "file_path": "manifests/ingress-nginx-controller-all-in-one-eks.yaml"
}
```

## 8. 현재 한계

v0.2는 로컬 정적 분석 도구입니다. 따라서 아래 항목은 아직 확인하지 않습니다.

- 실제 EKS 클러스터 상태
- 실제 Pod 실행 상태
- AWS IAM 정책 내용
- ALB/NLB 실제 생성 여부
- Security Group 실제 규칙
- CloudWatch metric
- Prometheus alert
- kubeconfig 기반 live scan

즉, YAML 안에 명확히 드러난 설정 문제를 찾는 도구입니다.

## 9. 권장 사용 방식

초기 도입 단계:

```bash
eks-manifest-auditor scan ./manifests --fail-on HIGH
```

운영 기준이 어느 정도 정리된 팀:

```bash
eks-manifest-auditor scan ./manifests --fail-on MEDIUM
```

엄격한 플랫폼 템플릿 검증:

```bash
eks-manifest-auditor scan ./manifests --fail-on LOW
```

## 10. 향후 개선 방향

다음 버전에서는 단일 리소스 검사보다 리소스 간 관계를 보는 방향으로 확장하는 것이 좋습니다.

후보 기능:

- PodDisruptionBudget 누락 검사
- HPA와 `resources.requests` 관계 검사
- Namespace별 ResourceQuota 확인
- LimitRange 확인
- NetworkPolicy 존재 여부 확인
- 설정 파일 기반 check enable/disable
- severity override
- GitHub Actions 예제 workflow
- PR comment용 Markdown 리포트
- HTML Dashboard
- Live Kubernetes Cluster Scan
- AWS API 기반 IRSA/IAM 검증
- AI 기반 수정 제안

## 11. 요약

`eks-manifest-auditor v0.2`는 EKS Manifest를 배포 전에 로컬에서 검사하기 위한 Python CLI 도구입니다.

현재 단계에서는 실제 클러스터나 AWS API에 연결하지 않고, YAML만 분석합니다. v0.2에서는 헬스체크, 컨테이너 보안 하드닝, CI 실패 기준, 오탐 수정이 추가되어 단순 예제 도구에서 CI/CD에 연결 가능한 Manifest 검사 도구로 발전했습니다.

다음 단계는 운영 안정성 검사와 정책 설정 파일을 추가해 팀별 배포 기준으로 사용할 수 있게 만드는 것입니다.
