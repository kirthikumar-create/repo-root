from fastapi import FastAPI
import asyncio
from .scheduler import start_scheduler
from .database import init_db

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI App Running on ECS Fargate"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.on_event("startup")
async def startup_event():
    init_db()
    asyncio.create_task(start_scheduler())
