import os
import json
import logging
import datetime
from datetime import date
from datetime import timedelta
import boto3
from azure.storage.blob import BlobServiceClient, BlobClient
from io import BytesIO

#get the current data
today = date.today()
yesterday_date = str(today - timedelta(days=1)) 
print(yesterday_date) 
#azure_cred
source_container_name = os.environ["CONTAINER_NAME"] #loyalty
source_blob_name =  str("loyalty_fraud_report"+yesterday_date+".csv") 
connect_str = os.environ['CONNECTION_STRING'] 
#AWS
destination_bucket_name = os.environ["DEST_BUCKET_NAME"] #"dev-mcd-resources"
destination_object_key =  str(os.environ["DEST_OBJECT_KEY"]+source_blob_name) #"inbound/mcd_plexure/mcd_plexure_loyalty_fraud/"

def copy_csv_file(source_container_name, source_blob_name, connect_str, destination_bucket_name, destination_object_key):
    try:
        # Create an Azure Blob Storage client
        print('Azure connection started')
        blob_service_client = BlobServiceClient.from_connection_string(connect_str)
        print('Azure blob connection succeeded')

        # Get a reference to the source CSV file
        source_blob_client = blob_service_client.get_blob_client(container=source_container_name, blob=source_blob_name)

        # Download the source CSV file to a memory buffer
        print('Downloading the source CSV file to a memory buffer')
        download_stream = source_blob_client.download_blob(timeout=7200)
        csv_buffer = BytesIO(download_stream.content_as_bytes())
    except Exception as e:
        dict = {
            "An error occurred":"Error while downloading from azure",
            "errordetail": e  
        }
        print(dict)
    else:
        try:
            # Create an S3 client
            print('Creating an S3 client')
            #s3 = boto3.resource('s3') 
            client = boto3.client('s3')
            print('s3 connection succeeded')

            # Upload the CSV file to S3
            print("upload start")
            client.put_object(Body=csv_buffer.getvalue(), Bucket=destination_bucket_name, Key=destination_object_key)
            #s3.Object(destination_bucket_name, destination_object_key).put(Body=csv_buffer.getvalue())
            print('upload done')
        except Exception as e:
            dict = {
                "An error occurred":"Error while uploading to the S3",
                "errordetail": e  
            }
            print(dict)
    

copy_csv_file(source_container_name, source_blob_name, connect_str, destination_bucket_name, destination_object_key)
