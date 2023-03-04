"""

To list details of all running AWS services in an account using Python boto3, you can use a combination of several AWS service clients and API calls. 
Here's an example script that demonstrates how to do this:

"""
import boto3

# create clients for each service you want to get information for
ec2 = boto3.client('ec2')
rds = boto3.client('rds')
ecs = boto3.client('ecs')
sqs = boto3.client('sqs')
s3 = boto3.client('s3')

# get a list of all running EC2 instances
ec2_response = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

# iterate over the instances and print their details
for reservation in ec2_response['Reservations']:
    for instance in reservation['Instances']:
        print(f"EC2 Instance ID: {instance['InstanceId']}")
        print(f"EC2 Instance Type: {instance['InstanceType']}")
        print(f"EC2 Public IP Address: {instance.get('PublicIpAddress', '-')}")
        print(f"EC2 Private IP Address: {instance.get('PrivateIpAddress', '-')}")
        print(f"EC2 State: {instance['State']['Name']}")
        print(f"EC2 Launch Time: {instance['LaunchTime']}")
        print("")

# get a list of all running RDS instances
rds_response = rds.describe_db_instances()

# iterate over the instances and print their details
for instance in rds_response['DBInstances']:
    print(f"RDS Instance ID: {instance['DBInstanceIdentifier']}")
    print(f"RDS Instance Type: {instance['DBInstanceClass']}")
    print(f"RDS Engine: {instance['Engine']}")
    print(f"RDS Engine Version: {instance['EngineVersion']}")
    print(f"RDS Endpoint: {instance['Endpoint']['Address']}:{instance['Endpoint']['Port']}")
    print(f"RDS State: {instance['DBInstanceStatus']}")
    print("")

# get a list of all running ECS clusters
ecs_response = ecs.list_clusters()

# iterate over the clusters and print their details
for cluster in ecs_response['clusterArns']:
    cluster_response = ecs.describe_clusters(clusters=[cluster])
    for c in cluster_response['clusters']:
        print(f"ECS Cluster ARN: {c['clusterArn']}")
        print(f"ECS Cluster Name: {c['clusterName']}")
        print(f"ECS Container Instance Count: {c['registeredContainerInstancesCount']}")
        print(f"ECS Active Service Count: {c['activeServicesCount']}")
        print("")

# get a list of all running SQS queues
sqs_response = sqs.list_queues()

# iterate over the queues and print their details
for queue_url in sqs_response['QueueUrls']:
    queue_name = queue_url.split('/')[-1]
    queue_attributes = sqs.get_queue_attributes(QueueUrl=queue_url, AttributeNames=['All'])
    print(f"SQS Queue Name: {queue_name}")
    print(f"SQS Queue URL: {queue_url}")
    print(f"SQS Queue Approximate Number of Messages: {queue_attributes['Attributes']['ApproximateNumberOfMessages']}")
    print("")

# get a list of all running S3 buckets
s3_response = s3.list_buckets()

# iterate over the buckets and print their details
for bucket in s3_response['Buckets']:
    bucket_name = bucket['Name']
    bucket_location = s3.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
    print(f"S3 Bucket Name: {bucket_name}")
    print(f"S3 Bucket Location: {bucket_location}")
    print("")


"""
This code will list details of all running EC2 instances, RDS instances, and ECS clusters in the default region for your AWS account, along with their 
respective details. If you want to list details of other running services or for a specific region, you can create additional clients for those services
and modify the API calls accordingly.
"""
