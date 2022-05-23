import sys
import threading
from queue import Queue, Empty
import socket
import json

def worker(q, results):
    while True:
        sock = socket.socket()
        sock.connect(("", 7301))
        try:
            url = q.get(timeout=1)
        except Empty:
            print("closing connection ", threading.current_thread().name)
            break
        print("send to server", url)
        sock.sendall(url.encode())
        data = sock.recv(1024)
        json_data = json.loads(data.decode())
        results.put((url, json_data))
        q.task_done()
        sock.close()

if __name__ == "__main__":
    workers_count = int(sys.argv[1])
    filename = sys.argv[2]

    q = Queue(workers_count)
    results = Queue()
    threads = [
        threading.Thread(target=worker, args=(q, results), name=f'worker_{i}', daemon=True)
        for i in range(workers_count)
    ]
    
    file = open(filename, 'rt')
    fit = iter(file)
    while not q.full():
        try:
            line = next(fit).strip()
        except StopIteration:
            break
        q.put(line)
    for th in threads:
        th.start()
    for line in fit:
        url, json_res = results.get()
        print(f"{url}: {json_res}")
        line = line.strip()
        q.put(line)
    file.close()
    q.join()
    while not results.empty():
        url, json_res = results.get()
        print(f"{url}: {json_res}")
