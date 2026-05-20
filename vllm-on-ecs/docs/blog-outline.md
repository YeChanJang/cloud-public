# vLLM + ECS GPU 블로그 구조

## 제목

vLLM + ECS GPU EC2 클러스터로 OpenAI 호환 API 서버 운영하기

## 핵심 메시지

LLM 사용량이 커질수록 API 비용보다 GPU 직접 운영이 더 저렴해지는 구간이 올 수 있다. 하지만 self-hosted LLM은 단순 비용 문제가 아니라 GPU 운영, 모델 로딩, 큐 관리, 관찰성까지 함께 다뤄야 하는 LLMOps 문제다.

## 섹션

1. OpenAI API 비용이 계속 커지는 이유
2. vLLM이 해결하려는 문제: 높은 처리량과 OpenAI 호환 API
3. PagedAttention을 쉽게 이해하기
4. Self-hosted LLM을 선택하기 전 봐야 할 비용 기준
5. ECS on EC2 GPU 클러스터 구조
6. vLLM Dockerfile과 OpenAI-compatible server 실행
7. Task Definition에서 GPU 리소스 지정하기
8. OpenAI SDK에서 base_url만 바꿔 호출하기
9. GPU Auto Scaling의 현실: 모델 로딩과 warm-up
10. 밤에는 0대, 낮에는 2대: 가능한 경우와 위험한 경우
11. CloudWatch + Grafana로 토큰 사용량과 GPU 상태 보기
12. vLLM 운영에서 만나는 문제: VRAM, CUDA, Queue, 모델 캐시
13. Bedrock, OpenAI API, vLLM을 나누는 기준
14. vLLM 운영 체크리스트
15. SUMMARY
16. CONCLUSION
