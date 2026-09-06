"""
Write a policy granting only s3:GetObject on
one specific bucket you own.

Create it as a customer managed policy.

Attach it to a test IAM User.

Confirm that user can read from the intended
bucket but not write to it or read any other bucket.
"""

import boto3

REGION_NAME = "us-east-1"
BUCKET_NAME = "tjs-bucket"
OBJECT_KEY = "sample.txt"
ENDPOINT_URL = "http://localhost:4566"

# get outputs from tf; update these every run
USER_ACCESS_KEY_ID = "LKIAQAAAAAAANBODOUQW"
USER_SECRET_ACCESS_KEY = "PYO8v5FNLEVCpyy7IZIxJ+Oma69mu4lh4ojXetfK"

# upload as root user to both buckets
s3 = boto3.client(
    "s3",
    aws_access_key_id="root",
    aws_secret_access_key="root",
    endpoint_url=ENDPOINT_URL,
    region_name=REGION_NAME,
)
print(s3.put_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY, Body=b"data"))
print(s3.put_object(Bucket="tjs-bucket-2", Key=OBJECT_KEY, Body=b"bucket 2 data"))
print(f"uploading sample file to '{BUCKET_NAME}' and 'tjs-bucket-2' as root user...")


# authenticating as user anniej
sts = boto3.client(
    "sts",
    aws_access_key_id=USER_ACCESS_KEY_ID,
    aws_secret_access_key=USER_SECRET_ACCESS_KEY,
    endpoint_url=ENDPOINT_URL,
    region_name=REGION_NAME,
)
user = sts.get_caller_identity()
print("authenticating as user anniej")
print(user["Arn"])

# authenticating as user anniej for s3 client
s3 = boto3.client(
    "s3",
    aws_access_key_id=USER_ACCESS_KEY_ID,
    aws_secret_access_key=USER_SECRET_ACCESS_KEY,
    endpoint_url=ENDPOINT_URL,
    region_name=REGION_NAME,
)

# anniej tries S3 GetObject on tjs-bucket
print(s3.get_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY))  # succeeds
print("anniej is able to do S3 GetObject")

# anniej tries S3 PutObject on tjs-bucket
print(s3.put_object(Bucket=BUCKET_NAME, Key=OBJECT_KEY, Body=b"data")) # fails
print("anniej is NOT able to do S3 PutObject")

# anniej tries S3 GetObject on tjs-bucket
print(s3.get_object(Bucket="tjs-bucket-2", Key=OBJECT_KEY))  # fails
print("anniej is NOT able to do S3 GetObject")