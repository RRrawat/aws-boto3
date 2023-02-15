import boto3

# Initialize S3 client
s3 = boto3.client('s3')

# Replace 'bucket' with the name of your S3 bucket
bucket_name = 'bucket'

# List all objects in the bucket
response = s3.list_objects_v2(Bucket=bucket_name)

# Iterate over the objects and print their names
for obj in response['Contents']:
    print(obj['Key'])
"""
This script first initializes an S3 client using the Boto3 library. It then sets the name of the bucket that you want to list the contents of. 
The script then uses the list_objects_v2 method to retrieve a list of all the objects in the bucket. Finally, the script iterates over the 
objects in the response and prints their names using the Key attribute.

Note that if there are a large number of objects in the bucket, you may need to use pagination to retrieve all the objects. 
You can do this by setting the MaxKeys parameter in the list_objects_v2 method to the maximum number of objects you want to 
retrieve per page, and then using the NextContinuationToken value from the response to retrieve the next page of results.

"""
