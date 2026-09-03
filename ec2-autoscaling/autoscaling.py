"""
Launch an EC2 instance

Create an autoscaling group with:
- minimum of 1 and 
- maximum of 3 instances

Manually trigger a scale up by changing the desired capacity to 3

Watch new instances appear within minutes.

Scale back down to 1 and watch the extra instances terminate automatically.
"""

import boto3
import time
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# connect to localstack-aws
localstack_config = {
    'endpoint_url': 'http://localhost:4566',
    'region_name': 'us-east-1',
    'aws_access_key_id': 'test',
    'aws_secret_access_key': 'test',
    'aws_session_token': 'test'
}
ec2 = boto3.client('ec2', **localstack_config)
autoscaling = boto3.client('autoscaling', **localstack_config)

# create launch template (blueprint)
ec2.create_launch_template(
    LaunchTemplateName='my-launch-template',
    LaunchTemplateData={
        'InstanceType': 't3.micro',
        'ImageId': 'ami-00000000'
    }
)
logger.info("Launch template created.")

# create auto scaling group
autoscaling.create_auto_scaling_group(
    AutoScalingGroupName='my-asg',
    LaunchTemplate={
        'LaunchTemplateName': 'my-launch-template',
        'Version': '$LATEST'
    },
    MinSize=1,
    MaxSize=3,
    DesiredCapacity=1,
    AvailabilityZones=['us-east-1a', 'us-east-1b']
)
logger.info("ASG created. Waiting for initial instance...")
time.sleep(5)

# trigger scale up
autoscaling.set_desired_capacity(
    AutoScalingGroupName='my-asg',
    DesiredCapacity=3,
    HonorCooldown=False
)
logger.info("Scaling up to 3 instances. Waiting for state change...")
time.sleep(5)

# verify scale up
response = autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=['my-asg'])
instances = response['AutoScalingGroups'][0]['Instances']
logger.info(f"Instances running after scale up: {len(instances)}")

# trigger scale down
autoscaling.set_desired_capacity(
    AutoScalingGroupName='my-asg',
    DesiredCapacity=1,
    HonorCooldown=False
)
logger.info("Scaling down to 1 instance. Waiting for state change...")
time.sleep(5)

# verify scale down
response = autoscaling.describe_auto_scaling_groups(AutoScalingGroupNames=['my-asg'])
instances = response['AutoScalingGroups'][0]['Instances']
logger.info(f"Instances running after scale down: {len(instances)}")