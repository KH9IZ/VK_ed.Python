import aiohttp
import asyncio
import argparse
from collections import Counter

def get_args():
    parser = argparse.ArgumentParser(description="download list of urls")
    parser.add_argument('count_', nargs='?', type=int, help=argparse.SUPPRESS)
    parser.add_argument('-c', '--count', default=1, type=int, metavar=1,
                        help="Count of parallel requests")
    parser.add_argument('filename', help="name of file with URLs separated by \n")
    args = parser.parse_args()
    if args.count_ is not None:
        args.count = args.count_
        del args.count_
    return args

async def load(queue, f):
    for line in f:
        await queue.put(line.strip())

class GenQueue(asyncio.Queue):
    def __aiter__(self):
        return self

    async def __anext__(self):
        if self.loading.done() and self.empty():
            raise StopAsyncIteration
        return await self.get()

async def fetch(url):
    async with aiohttp.ClientSession(timeout=aiohttp.ClientTimeout(total=10)) as session:
        async with session.get(url) as resp:
            return await resp.read()

async def worker(myqueue):
    task_id = asyncio.current_task().get_name()
    async for url in myqueue:
        try:
            data = await fetch(url)
            cntr = Counter(data.split())
            print(f"Task: {task_id}")
            print(f"{url}: {dict(cntr.most_common(3))}")
        except asyncio.exceptions.TimeoutError:
            print(f"Task: {task_id}")
            print(f"{url}: Timed Out!")
        finally:
            myqueue.task_done()

async def download(file, parallel_count: int = 1) -> list[int]:
    q = GenQueue(maxsize=parallel_count)
    q.loading = asyncio.create_task(load(q, file))
    tasks = [
        asyncio.create_task(worker(q), name=i)
        for i in range(parallel_count)
    ]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    args = get_args()
    with open(args.filename) as f:
        result = asyncio.run(download(f, parallel_count=args.count))
