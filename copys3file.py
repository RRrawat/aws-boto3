import boto3

# set up the S3 client
s3 = boto3.client('s3')

# set up the source and destination bucket and key names
src_bucket = 'source-bucket'
src_key = 'path/to/source/file'
dst_bucket = 'destination-bucket'
dst_key = 'path/to/destination/file'

# copy the file
s3.copy_object(Bucket=dst_bucket, CopySource={'Bucket': src_bucket, 'Key': src_key}, Key=dst_key)
