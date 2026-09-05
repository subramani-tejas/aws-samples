import boto3
import json


with open('outputs.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

key_object = data['anniej-access-key']
key_values = key_object['value']

access_key = key_values['id']
secret_key = key_values['secret']

sts = boto3.client(
    'sts',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    endpoint_url='http://localhost:4566',
    region_name='us-east-1'
)

"""
CONFIRM USER IDENTITY
run this before calling STS: 
terraform output -json > outputs.json
"""
print(sts.get_caller_identity())

"""
CONFIRM INVALID USER
run this before calling STS:
terraform destroy
"""
print(sts.get_caller_identity())  # returns root
