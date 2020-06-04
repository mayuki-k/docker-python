from fastapi import FastAPI
import time
from datetime import datetime
import threading
import asyncio

app = FastAPI()

def heveay_task():
    print(f'開始 {datetime.now()}')
    time.sleep(10)
    print(f'終了 {datetime.now()}')

sem = asyncio.Semaphore(1)
sem_thread = threading.Semaphore(1)

@app.get("/")
async def root():
    with await sem:
        heveay_task()
        return {"message": "Hello World"}

@app.get("/h")
async def h():
    with sem_thread:
        heveay_task()
        return {"Message":"HelloWorld"}

@app.get("/t")
async def t():
    heveay_task()
    return {"Message":"HelloWorld"}
