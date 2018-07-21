import threading
from queue import Queue
import requests

Lock = threading.Lock()

q = Queue()


def calculation_request(url):
    with Lock:
        reqs = requests.get(url)
        print(threading.current_thread().getName(), reqs.json())


def consumer():
    while True:
        url = q.get()
        calculation_request(url)
        q.task_done()


def producer():
    for i in range(30):
        url = "http://127.0.0.1:8000/apicollegesmodify/" + str(10) + "/student/" + str(30 + i) + "/options/"
        q.put(url)
    q.join()


t = threading.Thread(target=producer)
t.daemon = True
t.start()

for i in range(10):
    t1 = threading.Thread(target=consumer)
    t1.daemon = True
    t1.start()

t.join()
