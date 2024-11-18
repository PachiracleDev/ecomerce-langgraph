import boto3
from fastapi import UploadFile, HTTPException
from settings import settings
from uuid import uuid4

 
BUCKET_NAME=settings.AWS_BUCKET_NAME
REGION_NAME=settings.AWS_REGION_NAME
ACCESS_KEY=settings.AWS_ACCESS_KEY
SECRET_KEY=settings.AWS_SECRET_KEY
 
def upload_file_to_s3(file: UploadFile, folder: str):
   
    file_id = f"{folder}/{uuid4()}"

    s3_client = boto3.client(
        's3',
        aws_access_key_id=ACCESS_KEY,
        aws_secret_access_key=SECRET_KEY,
        region_name=REGION_NAME
    )

    try: 
        s3_client.upload_fileobj(file.file, BUCKET_NAME, file_id, ExtraArgs={'ContentType': file.content_type})
 
        url = f"https://{settings.AWS_CLOUDFRONT}/{file_id}"
        return url
    except:
        raise HTTPException(status_code=500, detail="Error al subir el archivo a S3")