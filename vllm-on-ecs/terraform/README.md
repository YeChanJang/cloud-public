# Terraform skeleton

이 폴더는 전체 배포 코드가 아니라 블로그 예제용 뼈대입니다.

운영 배포에는 최소한 아래 리소스가 추가로 필요합니다.

- VPC, private subnet, route table
- ALB 또는 internal NLB
- ECS optimized GPU AMI 기반 Launch Template
- Auto Scaling Group
- ECS Capacity Provider
- ECS Task Execution Role
- ECS Task Role
- Security Group
- ECR Repository
- CloudWatch Logs
- 선택: VPC Endpoint, Secrets Manager, WAF, ACM

GPU 인스턴스 비용이 크기 때문에 Terraform apply 전에는 반드시 예상 비용을 계산하세요.
