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


@app.get("/")
async def root():
    sem = asyncio.Semaphore(1)
    with await sem:
        heveay_task()
        return {"message": "Hello World"}