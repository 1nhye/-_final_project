from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import file_upload

app = FastAPI()

origins = [
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(file_upload.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


