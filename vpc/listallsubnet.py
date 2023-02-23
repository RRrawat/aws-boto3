#To list all private and public subnets inside a VPC here is the python script in boto3
import boto3

# Enter your AWS access key ID and secret access key
ACCESS_KEY = 'YOUR_ACCESS_KEY'
SECRET_KEY = 'YOUR_SECRET_KEY'

# Enter the ID of your VPC
VPC_ID = 'YOUR_VPC_ID'

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    region_name='us-east-1' # Enter your AWS region
)

# Create a client for EC2 service
ec2_client = session.client('ec2')

# Use the describe_subnets method to get all subnets in the VPC
response = ec2_client.describe_subnets(
    Filters=[
        {
            'Name': 'vpc-id',
            'Values': [
                VPC_ID,
            ]
        },
    ]
)

# Initialize empty lists to store private and public subnet IDs
private_subnets = []
public_subnets = []

# Loop through all subnets and add the IDs to the appropriate list
for subnet in response['Subnets']:
    if subnet['MapPublicIpOnLaunch']:
        public_subnets.append(subnet['SubnetId'])
    else:
        private_subnets.append(subnet['SubnetId'])

# Print the private and public subnet IDs
print("Private subnets: ", private_subnets)
print("Public subnets: ", public_subnets)

#Make sure to replace the placeholders with your own values before running the script.
#This script allows you to quickly get a list of private and public subnets in your VPC.
