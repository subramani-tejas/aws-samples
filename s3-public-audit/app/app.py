import boto3
from botocore.exceptions import ClientError

s3 = boto3.client(
    's3',
    endpoint_url="http://localhost:4566",
    aws_access_key_id="test",
    aws_secret_access_key="test"
)

all_buckets = s3.list_buckets()
bad_buckets = []

for bucket in all_buckets['Buckets']:
    bucket_name = bucket["Name"]
    try:
        all_config = s3.get_public_access_block(Bucket=bucket_name)
        public_config = all_config['PublicAccessBlockConfiguration']

        # Check if ALL four settings are True
        if all(public_config.values()):
            continue
        else:
            bad_buckets.append(bucket_name)

    except ClientError as e:
        # if the config doesn't exist, AWS throws this specific error
        # meaning the bucket is unprotected, so we add it to the bad list
        if e.response['Error']['Code'] == 'NoSuchPublicAccessBlockConfiguration':
            bad_buckets.append(bucket_name)
        else:
            # Re-raise any other unexpected AWS errors (like permission denied)
            raise

print(f"Buckets missing full public access blocks: {bad_buckets}")
