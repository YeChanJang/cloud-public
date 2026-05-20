# 비용 판단 기준

Self-hosted vLLM은 사용량이 작을 때 항상 저렴한 선택은 아닙니다.

## API 사용이 유리한 경우

- 호출량이 작거나 불규칙하다.
- 운영 인력이 부족하다.
- 품질과 안정성이 비용보다 중요하다.
- GPU 서버 idle 시간이 길다.

## vLLM 직접 운영을 검토할 수 있는 경우

- 내부 서비스에서 반복적으로 많은 토큰을 사용한다.
- 특정 모델을 고정적으로 많이 호출한다.
- GPU 서버를 계속 활용할 만큼 트래픽이 있다.
- 모델 latency, 데이터 위치, 커스터마이징 요구가 크다.
- 운영팀이 GPU, 컨테이너, 관찰성을 관리할 수 있다.

## 계산할 항목

```text
API 비용 = input tokens + output tokens + provider pricing
vLLM 비용 = GPU instance hours + EBS + data transfer + 운영 비용 + idle cost
```

비용 비교는 월 단위 평균만 보면 안 됩니다. 피크 시간, idle 시간, 장애 대응 비용까지 함께 봐야 합니다.
