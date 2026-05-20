# vLLM on ECS GPU

vLLM을 Amazon ECS on EC2 GPU 클러스터에 배포해 OpenAI 호환 API 서버로 운영하는 예제입니다.

> 이 저장소는 블로그 글을 보조하기 위한 **학습용 샘플**입니다. 운영 환경에 그대로 적용하기보다는, vLLM OpenAI-compatible server를 ECS GPU EC2 기반으로 배포할 때 필요한 구성 요소를 이해하는 용도로 사용하세요.

---

## 📎 관련 아티클

- [vLLM으로 OpenAI 호환 API 서버 만들기: ECS GPU EC2 클러스터 운영 방법](https://tistory-cloud.tistory.com/entry/vLLM%EC%9C%BC%EB%A1%9C-OpenAI-%ED%98%B8%ED%99%98-API-%EC%84%9C%EB%B2%84-%EB%A7%8C%EB%93%A4%EA%B8%B0-ECS-GPU-EC2-%ED%81%B4%EB%9F%AC%EC%8A%A4%ED%84%B0-%EC%9A%B4%EC%98%81-%EB%B0%A9%EB%B2%95)

---

## ✅ 이 예제가 보여주는 것

- vLLM OpenAI 호환 API 서버 실행 구조
- ECS on EC2에서 GPU 리소스를 예약하는 Task Definition 예시
- GPU Capacity Provider와 Auto Scaling 설계 방향
- OpenAI SDK에서 `base_url`만 바꿔 vLLM 엔드포인트를 호출하는 방식
- CloudWatch와 Grafana로 토큰 사용량, 지연 시간, GPU 상태를 보는 운영 관점
- Self-hosted LLM을 선택하기 전에 확인해야 할 비용과 운영 체크리스트

---

## ❌ 이 예제가 하지 않는 것

- 실제 프로덕션 전체 배포를 보장하지 않습니다.
- 모델 라이선스 검토를 대신하지 않습니다.
- GPU 인스턴스 비용 최적화를 자동으로 보장하지 않습니다.
- Fargate GPU 구성을 다루지 않습니다. 이 예제는 **ECS on EC2 GPU** 기준입니다.
- 대규모 멀티 GPU/멀티 노드 분산 추론 전체 구성을 다루지 않습니다.

---

## 📁 폴더 구조

```text
docker/             vLLM 서버 컨테이너 예제
ecs/                ECS Task Definition, Service 예제
terraform/          ECS GPU 클러스터 구성 뼈대
examples/           OpenAI SDK 호환 호출 예제
docs/               블로그 구조, 비용 기준, 운영 체크리스트
cloudwatch/         CloudWatch Dashboard 샘플
grafana/            Grafana Dashboard 샘플
scripts/            로컬 테스트와 헬스체크 스크립트
```

---

## 🧭 블로그 섹션과 예제 파일 매핑

| 블로그 섹션 | 관련 파일 |
|---|---|
| vLLM이 해결하려는 문제 | `docs/blog-outline.md` |
| vLLM Dockerfile과 OpenAI-compatible server 실행 | `docker/Dockerfile`, `docker/entrypoint.sh` |
| ECS on EC2 GPU 클러스터 구조 | `terraform/main.tf`, `terraform/variables.tf` |
| Task Definition에서 GPU 리소스 지정하기 | `ecs/task-definition.json` |
| OpenAI SDK에서 base_url만 바꿔 호출하기 | `examples/openai_compatible_client.py` |
| GPU Auto Scaling의 현실 | `docs/autoscaling-notes.md` |
| CloudWatch + Grafana로 토큰 사용량 보기 | `cloudwatch/dashboard.json`, `grafana/dashboard.json` |
| vLLM 운영 체크리스트 | `docs/operation-checklist.md` |

---

## 🚀 빠른 시작

### 1. 로컬에서 vLLM 서버 실행 형태를 확인합니다

GPU 환경이 있는 서버에서 아래와 같은 형태로 실행합니다.

```bash
docker build -t vllm-openai:sample -f docker/Dockerfile .

docker run --gpus all --rm -p 8000:8000 \
  -e MODEL_ID=Qwen/Qwen2.5-7B-Instruct \
  -e VLLM_API_KEY=dummy-key-for-vllm \
  vllm-openai:sample
```

> 모델 ID는 예시입니다. 실제 운영 전에는 모델 라이선스, VRAM 요구량, 상업적 사용 가능 여부를 확인하세요.

### 2. OpenAI 호환 API를 호출합니다

```bash
python examples/openai_compatible_client.py
```

이 예제는 OpenAI SDK의 `base_url`을 vLLM 서버 주소로 바꿔 호출합니다. 샘플에서는 `OPENAI_API_KEY=dummy-key-for-vllm` 값을 사용합니다.

### 3. ECS Task Definition의 GPU 설정을 확인합니다

`ecs/task-definition.json`에서 아래 항목이 핵심입니다.

```json
"resourceRequirements": [
  {"type": "GPU", "value": "1"}
]
```

Amazon ECS 공식 문서에 따르면 GPU 요구사항을 컨테이너 정의에 지정하면 ECS가 해당 컨테이너 런타임을 NVIDIA 컨테이너 런타임으로 설정하고 GPU를 예약합니다.

---

## ⚠️ 운영 전 확인

- ECS Fargate가 아니라 ECS on EC2 GPU 기준인지 확인합니다.
- GPU 최적화 AMI 또는 NVIDIA 드라이버가 준비된 인스턴스를 사용합니다.
- 모델이 요구하는 VRAM이 인스턴스 GPU 메모리보다 작은지 확인합니다.
- 모델 다운로드와 캐시를 고려해 EBS 용량을 충분히 잡습니다.
- 스케일 아웃보다 콜드스타트, 모델 로딩 시간, warm-up 시간이 더 큰 병목일 수 있습니다.
- OpenAI API와 달리 직접 운영 서버는 장애, 보안, 패치, 용량 계획의 책임이 생깁니다.

---

## 🧯 자주 막히는 지점

| 증상 | 확인할 것 |
|---|---|
| ECS Task가 배치되지 않음 | GPU 인스턴스가 클러스터에 등록됐는지, GPU 리소스가 남아 있는지 확인 |
| 컨테이너에서 GPU가 안 보임 | GPU 최적화 AMI, NVIDIA 드라이버, ECS agent 상태 확인 |
| 모델 로딩이 너무 오래 걸림 | 모델 크기, EBS 성능, 캐시 위치, 이미지 빌드 전략 확인 |
| 응답이 느림 | 동시 요청 수, max model length, GPU 사용률, queue 대기 시간 확인 |
| 비용이 예상보다 큼 | GPU 인스턴스 idle 시간, scale-in 정책, Spot 사용 가능 여부 확인 |

---

## 📚 참고 문서

- [vLLM OpenAI-Compatible Server](https://docs.vllm.ai/serving/openai_compatible_server.html)
- [vLLM Quickstart](https://docs.vllm.ai/en/stable/getting_started/quickstart/)
- [Amazon ECS task definitions for GPU workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu.html)
- [Specifying GPUs in an Amazon ECS task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-gpu-specifying.html)
- [Amazon ECS capacity providers for EC2 workloads](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/asg-capacity-providers.html)