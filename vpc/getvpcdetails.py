#here's an example Python script that uses the boto3 library to retrieve details about all VPCs in your AWS account:
import boto3

# Replace <vpc-id> with the ID of the VPC you want to retrieve details for
vpc_id = '<vpc-id>'

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
