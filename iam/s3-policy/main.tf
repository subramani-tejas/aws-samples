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
  s3_use_path_style           = true

  endpoints {
    s3  = "http://localhost:4566"
    iam = "http://localhost:4566"
    sts = "http://localhost:4566"
  }
}

resource "aws_s3_bucket" "tjs_bucket" {
  bucket = "tjs-bucket"
}

resource "aws_s3_bucket" "tjs_bucket_2" {
  bucket = "tjs-bucket-2"
}

resource "aws_iam_user" "anniej" {
  name = "anniej"
}

resource "aws_iam_access_key" "anniej_keys" {
  user = aws_iam_user.anniej.name
}

resource "aws_iam_policy" "tjs_policy" {
  name = "tjs-policy"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Action = [
        "s3:GetObject",
      ]
      Effect   = "Allow"
      Resource = "${aws_s3_bucket.tjs_bucket.arn}/*"
    }]
  })
}

resource "aws_iam_user_policy_attachment" "name" {
  user       = aws_iam_user.anniej.name
  policy_arn = aws_iam_policy.tjs_policy.arn
}

output "access_key" {
  value = aws_iam_access_key.anniej_keys.id
}

output "secret_key" {
  value     = aws_iam_access_key.anniej_keys.secret
  sensitive = true
}
