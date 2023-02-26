#here's a Python script using boto3 to get all the details of your EC2 instances:
import boto3

# Initialize the EC2 client

ec2 = boto3.client('ec2')

# Get all instances
instances = ec2.describe_instances()

# Loop through instances and print details
for reservation in instances['Reservations']:
    for instance in reservation['Instances']:
        # Print instance details
        print("Instance ID: " + instance['InstanceId'])
        print("Instance Type: " + instance['InstanceType'])
        print("Public IP Address: " + instance.get('PublicIpAddress', 'N/A'))
        print("Private IP Address: " + instance.get('PrivateIpAddress', 'N/A'))
        print("AMI ID: " + instance['ImageId'])
        print("Subnet ID: " + instance.get('SubnetId', 'N/A'))
        print("VPC ID: " + instance.get('VpcId', 'N/A'))
        print("Security Groups: " + str(instance['SecurityGroups']))
        print("IAM Instance Profile: " + str(instance.get('IamInstanceProfile', {}).get('Arn', 'N/A')))
        print("Availability Zone: " + instance['Placement']['AvailabilityZone'])
        print("Key Pair Name: " + instance.get('KeyName', 'N/A'))
        print("Block Device Mappings: " + str(instance['BlockDeviceMappings']))
        print("State: " + instance['State']['Name'])
        print("Tags: " + str(instance.get('Tags', [])))
        print("Launch Time: " + str(instance['LaunchTime']))
        print("-----------------------------------------")

 """
 This code will connect to the AWS account and retrieve information about all EC2 instances, including those that are stopped or terminated. 
 It will then loop through each instance and print out a comprehensive set of details, such as the instance ID, type, IP addresses, AMI ID, 
 subnet ID, VPC ID, security groups, IAM instance profile, availability zone, key pair name, block device mappings, state, tags, and launch time. 
 You can modify the code to include or exclude specific details based on your needs.
 
 """
