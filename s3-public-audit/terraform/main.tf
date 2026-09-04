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
    s3 = "http://localhost:4566"
  }
}

resource "aws_s3_bucket" "tjs-private-bucket-1" {
  bucket = "tjs-private-1"
}

resource "aws_s3_bucket" "tjs-private-bucket-2" {
  bucket = "tjs-private-2"
}

resource "aws_s3_bucket" "tjs-public-bucket" {
  bucket = "tjs-public"
}

resource "aws_s3_bucket_public_access_block" "tjs-private-bucket-1" {
  bucket = aws_s3_bucket.tjs-private-bucket-1.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true

}

resource "aws_s3_bucket_public_access_block" "tjs-private-bucket-2" {
  bucket = aws_s3_bucket.tjs-private-bucket-2.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true

}

resource "aws_s3_bucket_public_access_block" "tjs-public-bucket" {
  bucket = aws_s3_bucket.tjs-public-bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false

}