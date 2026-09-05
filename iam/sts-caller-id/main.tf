terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "6.12.0"
    }
  }
}

provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    iam = "http://localhost:4566"
  }
}

resource "aws_iam_role" "test_role" {
  name = "test-role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = "sts:AssumeRole"
      Effect = "Allow"

      Principal = {
        AWS = "arn:aws:iam::000000000000:root"
      }
    }]
  })
}

output "role_arn" {
    value = aws_iam_role.test_role.arn
}
