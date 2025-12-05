from fastapi import FastAPI
import asyncio
from .scheduler import start_scheduler

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI  App Running on ECS Fargate"}

@app.on_event("startup")
async def startup_event():
    asyncio.create_task(start_scheduler())
