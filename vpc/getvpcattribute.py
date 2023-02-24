"""

Before we get started, make sure you have Boto3 installed on your machine, and that you have the necessary AWS credentials to access the VPC 
you want to interact with. Once that's done, here's a Python script that should do the trick:

"""

import boto3

# Specify the region and the VPC ID you want to interact with
region_name = 'us-west-2'
vpc_id = 'vpc-123456789'

# Create a Boto3 EC2 client in the specified region
ec2 = boto3.client('ec2', region_name=region_name)

# Get the Internet Gateway associated with the VPC
igw_response = ec2.describe_internet_gateways(
    Filters=[{'Name': 'attachment.vpc-id', 'Values': [vpc_id]}]
)
igw_id = igw_response['InternetGateways'][0]['InternetGatewayId']

# Get the Route Table associated with the VPC
route_table_response = ec2.describe_route_tables(
    Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
)
route_table_id = route_table_response['RouteTables'][0]['RouteTableId']

# Get the Network ACL associated with the VPC
nacl_response = ec2.describe_network_acls(
    Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
)
nacl_id = nacl_response['NetworkAcls'][0]['NetworkAclId']

# Get the Elastic IP address associated with the VPC
eip_response = ec2.describe_addresses(
    Filters=[{'Name': 'domain', 'Values': ['vpc']}]
)
eip_id = eip_response['Addresses'][0]['AllocationId']

# Get the NAT Gateway associated with the VPC
nat_response = ec2.describe_nat_gateways(
    Filters=[{'Name': 'vpc-id', 'Values': [vpc_id]}]
)
nat_id = nat_response['NatGateways'][0]['NatGatewayId']

# Print out the IDs of the resources we found
print(f'Internet Gateway ID: {igw_id}')
print(f'Route Table ID: {route_table_id}')
print(f'Network ACL ID: {nacl_id}')
print(f'Elastic IP ID: {eip_id}')
print(f'NAT Gateway ID: {nat_id}')


"""

In this script, we use the describe_* methods provided by the EC2 client to get information about the Internet Gateway, Route Table, 
Network ACL, Elastic IP, and NAT Gateway associated with the specified VPC. We then extract the IDs of these resources from the response 
objects and print them out to the console.

Make sure you replace region_name and vpc_id with the appropriate values for your use case.

"""
