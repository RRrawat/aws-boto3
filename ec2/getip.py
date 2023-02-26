"""
we can use the describe_instances method from the boto3 library to get the IP addresses of all EC2 instances in your AWS account. 
Here is an example Python code snippet that uses boto3 to achieve this:
"""

import boto3

# Create an EC2 client object
ec2 = boto3.client('ec2')

# Retrieve information about all running instances
response = ec2.describe_instances()

# Extract the IP addresses of each instance
ip_addresses = []
for reservation in response['Reservations']:
    for instance in reservation['Instances']:
        ip_address = instance['PublicIpAddress']
        ip_addresses.append(ip_address)
        
# Print the list of IP addresses
print(ip_addresses)
