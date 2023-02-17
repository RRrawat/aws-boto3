import boto3

# Set the name of the S3 bucket and the file to move
bucket_name = 'your_bucket_name'
old_file_key = 'path/to/old/file.txt'
new_file_key = 'path/to/new/file.txt'

# Create an S3 client
s3 = boto3.client('s3')

# Copy the file to the new location
s3.copy_object(Bucket=bucket_name, CopySource=bucket_name+'/'+old_file_key, Key=new_file_key)

# Delete the file from the old location
s3.delete_object(Bucket=bucket_name, Key=old_file_key)

print('File moved successfully!')
