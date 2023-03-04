#here's an example Python script that uses the boto3 library to retrieve details about all VPCs in your AWS account
import boto3

# Replace <vpc-id> with the ID of the VPC you want to retrieve details for
vpc_id = '<your-vpc-id>'

# Create an EC2 client
ec2 = boto3.client('ec2')

# Retrieve information about the VPC
response = ec2.describe_vpcs(VpcIds=[vpc_id])

# Print information about the VPC
vpc = response['Vpcs'][0]
print('VPC ID:', vpc['VpcId'])
print('CIDR Block:', vpc['CidrBlock'])
print('Is Default:', vpc['IsDefault'])
print('State:', vpc['State'])
print('DHCPOptions ID:', vpc['DhcpOptionsId'])
print('Instance Tenancy:', vpc['InstanceTenancy'])
print('Tags:')
for tag in vpc['Tags']:
    print('\t', tag['Key'], ':', tag['Value'])

    
    
"""
In this script, we first define the ID of the VPC we want to retrieve details for by setting the vpc_id variable to a string containing the VPC ID. 
We then create an EC2 client object and call the describe_vpcs() method with the VpcIds parameter set to a list containing the vpc_id variable. 
This will return a dictionary containing information about the specified VPC.

We then extract the details we're interested in from the Vpcs list in the response dictionary and print them out. The details we're retrieving include 
the VPC ID, CIDR block, default status, state, DHCP options ID, instance tenancy, and any tags associated with the VPC.

Note that you'll need to have the boto3 library installed and properly configured with your AWS credentials in order to run this script. 
Also, make sure to replace <vpc-id> with the actual ID of the VPC you want to retrieve details for.

"""
