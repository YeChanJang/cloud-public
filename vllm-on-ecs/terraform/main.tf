terraform {
  required_version = ">= 1.6.0"

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = ">= 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}

resource "aws_ecs_cluster" "this" {
  name = var.cluster_name

  setting {
    name  = "containerInsights"
    value = "enabled"
  }
}

resource "aws_cloudwatch_log_group" "vllm" {
  name              = "/ecs/${var.service_name}"
  retention_in_days = var.log_retention_days
}

# This is a skeleton for blog/demo use.
# Add VPC, subnets, ALB, IAM roles, launch template, ASG, and capacity provider before production use.
