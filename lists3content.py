import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Replace 'my-bucket' with the name of your S3 bucket
bucket_name = 'my-bucket'

# List all objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# Iterate over the objects and print their names
for obj in response['Contents']:
    print(obj['Key'])
"""
