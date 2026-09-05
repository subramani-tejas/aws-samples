"""
Run aws sts get-caller-identity and
note exactly which identity it reports.

Assume a role and inspect the temporary
credentials STS returns. Compare the identity
reported before and after assuming the role.
"""

import boto3

sts = boto3.client(
    "sts",
    endpoint_url="http://localhost:4566",
    region_name="us-east-1",
)

print(sts.get_caller_identity())  # arn:aws:iam::000000000000:root

resp = sts.assume_role(
    RoleArn="arn:aws:iam::000000000000:role/test-role",
    RoleSessionName="testAssumeRoleSession",
)

creds = resp["Credentials"]

assumed_sts = boto3.client(
    "sts",
    aws_access_key_id=creds['AccessKeyId'],
    aws_secret_access_key=creds['SecretAccessKey'],
    endpoint_url="http://localhost:4566",
    region_name="us-east-1",
)

print(assumed_sts.get_caller_identity()) # test-role
# arn:aws:sts::000000000000:assumed-role/test-role/testAssumeRoleSession