import boto3

iam = boto3.client(
    'iam',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

# List every managed policy attached to a role, a quick first check
# for anything obviously too broad, like AdministratorAccess.
def check_role_policies(role_name):
    attached = iam.list_attached_role_policies(RoleName=role_name)
    for policy in attached['AttachedPolicies']:
        if 'Administrator' in policy['PolicyName']:
            print(f"Warning: {role_name} has broad policy {policy['PolicyName']}")

check_role_policies('reporting-job')

if __name__ == '__main__':
    pass