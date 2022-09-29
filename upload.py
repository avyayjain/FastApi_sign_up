from fastapi import APIRouter, UploadFile, File
import shutil
from googledrive import upload_to_google_drive

upload_file_router = APIRouter()


@upload_file_router.post("/")
async def uploadFile(file: UploadFile = File(...)):
    with open('test.jpg', 'wb') as buffer:
        shutil.copyfileobj(file.file, buffer)
    try:
        upload_to_google_drive(file)
    except Exception as e:
        print(e)
    return {"file name": file.filename,
            'message': "file uploaded successfully"}
