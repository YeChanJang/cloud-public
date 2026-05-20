# vLLM 운영 체크리스트

## 배포 전

- [ ] 모델 라이선스를 확인했는가
- [ ] 모델 VRAM 요구량과 GPU 메모리를 비교했는가
- [ ] ECS on EC2 GPU 구성이 맞는가
- [ ] GPU 최적화 AMI 또는 NVIDIA 드라이버 구성이 준비됐는가
- [ ] EBS 용량과 모델 캐시 경로를 정했는가
- [ ] OpenAI 호환 API 인증 방식을 추가했는가

## 운영 중

- [ ] 요청 수, latency, 오류율을 수집하는가
- [ ] GPU 사용률과 메모리 사용량을 수집하는가
- [ ] 모델 로딩 실패 로그를 확인할 수 있는가
- [ ] scale-out 후 warm-up 시간을 반영했는가
- [ ] scale-in 전에 연결 drain 정책이 있는가
- [ ] 비용 계산에 GPU idle 시간을 포함했는가

## 장애 대응

- [ ] 모델 다운로드 실패 시 재시도 정책이 있는가
- [ ] GPU OOM 발생 시 max model length와 batch 설정을 낮출 수 있는가
- [ ] 특정 모델 장애 시 Bedrock 또는 OpenAI API fallback을 둘 수 있는가
- [ ] Spot interruption을 사용할 경우 graceful shutdown이 가능한가
