import asyncio
from datetime import datetime
import time


sem = asyncio.Semaphore(2)

async def heavy():
    async with sem:
        print(f'開始 {datetime.now()}')
        await asyncio.sleep(10)
        print(f'終了 {datetime.now()}')


async def test():
    sem = asyncio.Semaphore(1)
    async def test_child():
        with await sem:
            await heavy()

async def test2():
    await heavy()



async def main():
    tasks = []
    tasks.append(heavy())
    tasks.append(heavy())
    return await asyncio.wait(tasks)

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())


