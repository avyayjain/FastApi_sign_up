import uvicorn
from fastapi import FastAPI
# from disable import disable_router
from login import login_router, logout_router
from signUp import signUp_ops_router, signUp_client_router
from upload import upload_file_router

app = FastAPI()


app.include_router(signUp_ops_router, prefix="/api/signUp_ops")
app.include_router(signUp_client_router, prefix="/api/signUp_client")

app.include_router(upload_file_router, prefix="/api/upload")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, debug=True)
