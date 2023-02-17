#Here's an example script that uses Boto3 to retrieve and print detailed configuration information for an S3 bucket.

import boto3

"""
#If your AWS CLI is not configure you can configure it as mentioned below 
aws_access_key_id = <your access_key>
aws_secret_access_key = <your secret_access>
aws_region = <your aws region>
s3 = boto3.client('s3', 
                  aws_access_key_id=aws_access_key_id, 
                  aws_secret_access_key=aws_secret_access_key,
                  region_name=aws_region)
"""

# Specify your region and S3 bucket name
region = 'us-west-2' #AWS region
bucket_name = 'example-bucket' #Bucket name 

# Create an S3 client
s3 = boto3.client('s3', region_name=region)

# Get the bucket's website configuration
response = s3.get_bucket_website(Bucket=bucket_name)

if 'WebsiteConfiguration' in response:
    website_config = response['WebsiteConfiguration']
    print(f"Website endpoint: http://{bucket_name}.s3-website.{region}.amazonaws.com/")
    print(f"Index document: {website_config['IndexDocument']['Suffix']}")
    if 'ErrorDocument' in website_config:
        print(f"Error document: {website_config['ErrorDocument']['Key']}")
else:
    print("The bucket does not have a website configuration.")

# Get the bucket's policy
response = s3.get_bucket_policy(Bucket=bucket_name)

if 'Policy' in response:
    print("Bucket policy:")
    print(response['Policy'])
else:
    print("The bucket does not have a policy.")

# Get the bucket's lifecycle configuration
response = s3.get_bucket_lifecycle_configuration(Bucket=bucket_name)

if 'Rules' in response:
    print("Lifecycle rules:")
    for rule in response['Rules']:
        print(f"  {rule['ID']}: {rule['Prefix']}, {rule['Status']}, {rule['Expiration']['Days']} days")
else:
    print("The bucket does not have a lifecycle configuration.")

# Get the bucket's versioning configuration
response = s3.get_bucket_versioning(Bucket=bucket_name)

if 'Status' in response:
    if response['Status'] == 'Enabled':
        print("Versioning is enabled for the bucket.")
    else:
        print("Versioning is not enabled for the bucket.")
else:
    print("The bucket does not have a versioning configuration.")

# Get the bucket's encryption configuration
response = s3.get_bucket_encryption(Bucket=bucket_name)

if 'ServerSideEncryptionConfiguration' in response:
    print("Server-side encryption is enabled for the bucket.")
    for rule in response['ServerSideEncryptionConfiguration']['Rules']:
        print(f"  {rule['ApplyServerSideEncryptionByDefault']['SSEAlgorithm']}")
else:
    print("Server-side encryption is not enabled for the bucket.")

# Get the bucket's public access configuration
response = s3.get_public_access_block(Bucket=bucket_name)

if response['PublicAccessBlockConfiguration']['BlockPublicAcls']:
    print("Block public ACLs is enabled for the bucket.")
if response['PublicAccessBlockConfiguration']['BlockPublicPolicy']:
    print("Block public bucket policies is enabled for the bucket.")
if response['PublicAccessBlockConfiguration']['IgnorePublicAcls']:
    print("Ignore public ACLs is enabled for the bucket.")
if response['PublicAccessBlockConfiguration']['RestrictPublicBuckets']:
    print("Restrict public bucket policies is enabled for the bucket.")

"""
This script retrieves and prints information about the following configuration settings for an S3 bucket:

Website configuration: If the bucket has a website configuration, it prints the website endpoint URL, index document, and error document.
Bucket policy: If the bucket has a policy, it prints the policy text.
Lifecycle configuration: If the bucket has a lifecycle configuration, it prints the lifecycle rules.
Versioning configuration: If the bucket has a versioning configuration, it prints whether versioning is enabled or not.
Encryption configuration: If the bucket has an encryption configuration, it prints whether server-side encryption is enabled


"""
