#Here's a Python script that uses Boto3 to list all the S3 buckets in your AWS account and their details:

import boto3

s3 = boto3.client('s3')

# List all S3 buckets in the account
response = s3.list_buckets()

# Loop through the buckets and print their details
for bucket in response['Buckets']:
    # Get the bucket name
    bucket_name = bucket['Name']
    
    # Get the creation date of the bucket
    creation_date = bucket['CreationDate']
    
    # Get the region of the bucket
    location = s3.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
    
    # Print the bucket details
    print(f'Bucket name: {bucket_name}\nCreation date: {creation_date}\nRegion: {location}\n')
