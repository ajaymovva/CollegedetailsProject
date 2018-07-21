import threading
import requests


def getUrlForStudent(collegeid, studentid):
    url = "http://127.0.0.1:8000/apicollegesmodify/" + str(collegeid) + "/student/" + str(studentid) + "/options/"
    reqs = requests.get(url)
    print(threading.current_thread().getName(), reqs.json())


id = 54
t = []
for i in range(5):
    t.append(threading.Thread(target=getUrlForStudent, args=(4, id)))
    t[i].start()
    id = id + 1

for i in range(5):
    t[i].join()
