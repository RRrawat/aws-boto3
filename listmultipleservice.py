"""
To list details of all running AWS services in an account using Python boto3, you can use a combination of several AWS service clients and API calls. 
Here's an example script that demonstrates how to do this:

"""
import boto3

# create an EC2 client
ec2 = boto3.client('ec2')

# get a list of all running instances
response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# iterate over the instances and print their details
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        print(f"Instance ID: {instance['InstanceId']}")
        print(f"Instance Type: {instance['InstanceType']}")
        print(f"Public IP Address: {instance.get('PublicIpAddress', '-')}")
        print(f"Private IP Address: {instance.get('PrivateIpAddress', '-')}")
        print(f"State: {instance['State']['Name']}")
        print(f"Launch Time: {instance['LaunchTime']}")
        print("")

        
