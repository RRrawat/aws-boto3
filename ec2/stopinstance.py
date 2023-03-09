"""
To stop an EC2 instance using Python, you can use the Boto3 library which is the Amazon Web Services (AWS) SDK for Python. 

"""

import boto3

# Create an EC2 client
ec2_client = boto3.client('ec2', aws_access_key_id='access_key', aws_secret_access_key='secret_key', region_name='us-east-1')

# Stop the instance
response = ec2_client.stop_instances(InstanceIds=['instance_id'])
print('Instance stopped:', response['StoppingInstances'][0]['InstanceId'])
