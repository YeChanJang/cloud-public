# GPU Auto Scaling notes

vLLM 서버의 Auto Scaling은 일반적인 stateless web API보다 어렵습니다.

## 이유

1. 모델 로딩 시간이 길 수 있습니다.
2. GPU 메모리에 모델을 올리는 warm-up 시간이 필요합니다.
3. 새 Task가 RUNNING 상태가 되어도 바로 좋은 latency를 보장하지 않습니다.
4. scale-in 시 진행 중인 추론 요청을 어떻게 drain할지 정해야 합니다.
5. Spot Instance를 쓰면 비용은 줄일 수 있지만 interruption 대응이 필요합니다.

## 권장 접근

- 처음에는 desired count를 고정하고 지표를 수집합니다.
- CPU보다 GPU 사용률, request queue length, p95 latency를 우선 봅니다.
- scale-out은 보수적으로, scale-in은 더 보수적으로 설정합니다.
- 업무 시간이 명확한 내부 도구라면 schedule scaling을 먼저 검토합니다.
- 0대로 줄이는 구조는 cold start를 감당할 수 있는 비동기/배치 업무에만 적용합니다.

## 위험한 접근

- 웹 API처럼 CPU 60% 기준으로 바로 scale-out하는 방식
- 모델 로딩 시간을 고려하지 않고 desired count를 0으로 내리는 방식
- ALB health check만 통과하면 준비 완료라고 가정하는 방식
