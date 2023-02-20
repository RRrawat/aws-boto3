#You can use the boto3 library in Python to copy an S3 file from one bucket to another. Here's some sample code that should do the trick:

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

# set up the S3 client
s3 = boto3.client('s3')

# set up the source and destination bucket and key names
src_bucket = 'source-bucket'
src_key = 'path/to/source/file'
dst_bucket = 'destination-bucket'
dst_key = 'path/to/destination/file'

# copy the file
s3.copy_object(Bucket=dst_bucket, CopySource={'Bucket': src_bucket, 'Key': src_key}, Key=dst_key)


"""

In this code, you first set up a client for S3 using the boto3.client method. Then you define the source and destination bucket and key names. 
Finally, you use the s3.copy_object method to copy the file, specifying the source bucket and key with the CopySource parameter, 
and the destination bucket and key with the Bucket and Key parameters, respectively.

"""
