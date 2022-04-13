"""S3 zip upload module."""
import os
import logging
from datetime import datetime
import boto3
from botocore.exceptions import ClientError
from dotenv import load_dotenv
from requests import session

load_dotenv()

S3_KEY=(str(os.getenv('S3_KEY_NAME')).lstrip())+"-"+(str(datetime.date(datetime.now())).lstrip())+"-"+(str(datetime.now().hour))+":"+(str(datetime.now().minute))+".zip"

session = boto3.Session(profile_name=os.getenv('profile_name'),
region_name=os.getenv('region_name'))

def upload_file():
    """
    This method will upload the zip file to s3.
    """
    print("Uploading Zipped Repository To S3")
    resource = session.resource('s3', region_name='eu-west-1')
    try:
        resource.meta.client.upload_file(
          os.getenv('UPLOAD_FILE_NAME'),
          os.getenv('S3_BUCKET_NAME'),
          S3_KEY
        )      
    except ClientError as error:
        logging.error(error)
        return False

    print("Repository Uploaded To S3")
    return True
