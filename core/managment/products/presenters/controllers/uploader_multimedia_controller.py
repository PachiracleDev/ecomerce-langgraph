from fastapi import APIRouter, UploadFile
from core.managment.products.infra.aws_uploader_sdk import upload_file_to_s3


router = APIRouter(prefix='/uploader')


@router.post('/upload/{folder}')
async def upload_file(file: UploadFile, folder: str):
    url_content = upload_file_to_s3(file, folder)
    return {"url_content": url_content}

