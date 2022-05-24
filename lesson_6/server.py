import argparse
import socket
import json
import threading
from queue import Queue
import requests
from collections import Counter


def get_args():
    parser = argparse.ArgumentParser(description="download list of urls")
    parser.add_argument(
        "-w", "--workers", default=1, type=int, metavar=1, help="Count of threads"
    )
    parser.add_argument("-k", default=1, type=int, metavar=1, help="Top k words")
    args = parser.parse_args()
    return args


def worker(q, k):
    while True:
        conn, url = q.get()
        r = requests.get(url)
        cntr = Counter(r.text.split())
        conn.sendall(json.dumps(dict(cntr.most_common(k))).encode())


def make_threads(n_threads, *args):
    threads = [
        threading.Thread(target=worker, args=args, name=f"worker_{i}", daemon=True)
        for i in range(n_threads)
    ]
    for th in threads:
        th.start()
    return threads


def main(args):
    q = Queue(args.workers)
    threads = make_threads(args.workers, q, args.k)

    sock = socket.socket()
    sock.bind(("", 7301))
    sock.listen(args.workers)

    while True:
        print("wait conn")
        client, addr = sock.accept()
        print("server: conn from ", addr)
        data = client.recv(1024)
        print("data: ", data)
        q.put((client, data.decode()))


if __name__ == "__main__":
    args = get_args()
    main(args)
