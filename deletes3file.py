#Here's a basic Python script using Boto3 to delete a file from an S3 bucket:


import boto3

# Replace the placeholders with your S3 bucket name and the name of the file to delete
bucket_name = "your-bucket-name"
file_name = "file-to-delete.txt"

# Create an S3 client
s3 = boto3.client('s3')

# Delete the file from the S3 bucket
s3.delete_object(Bucket=bucket_name, Key=file_name)

print(f"File {file_name} deleted from S3 bucket {bucket_name}")
