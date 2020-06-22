import threading
import time
from datetime import datetime

sem = threading.Semaphore(2)

def worker(sem):
    with sem:
        print(f'開始 {datetime.now()}')
        time.sleep(5)
        print(f'終了 {datetime.now()}')

t1 = threading.Thread(target=worker, args=(sem,))
t2 = threading.Thread(target=worker, args=(sem,))
t1.start()
t2.start()