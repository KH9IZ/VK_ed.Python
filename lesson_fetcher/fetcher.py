import aiohttp
import asyncio
import argparse

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

async def fetcher(q, session):
    while True:
        url = await q.get()
        try:
            async with session.get(url) as resp:
                data = await resp.read()
        finally:
            q.task_done()
        yield len(data)

async def crawl(queue, threads=10):
    async with aiohttp.ClientSession() as session:
        for thread in range(threads):
            task = asyncio.create_task(fetch(queue, session))
            
        tasks = [
            asyncio.create_task(fetch(url, session))
            for _ in range(thread)
        ]
        await q.join()
    for t in tasks:
        t.cancel()

async def load(queue, f):
    for line in f:
        await queue.put(line)

class GenQueue(asyncio.Queue):
    def __init__(self, maxsize=0, loading)
    async def __next__(self):
        while loading
        if self.empty() and self.loading.done():
            raise StopIteration
        return await self.get()

async def thread(myqueue):
    async for url in myqueue:
        async with aiohttp.ClientSession as session:
            try:
                data = fetch(queue, sessions)
            finally:
                q.task_done()
            yield data
    

async def download(file, parallel_count: int = 1) -> list[int]:
    q = GenQueue(maxsize=parallel_count)
    loading = asyncio.create_task(load(q, f))
    tasks = [
        asyncio.create_task(thread(q))
        for _ in range(parallel_count)
    ]
    results = await asyncio.gather(tasks)
    return dict(
            zip(
                seq1=(f"thread_{i} sum" for i in range(parallel_task)), 
                seq2=results
            )
        )
    


if __name__ == "__main__":
    args = get_args()
    with open(args.filename) as f:
        result = asyncio.run(download(f, parallel_count=args.count))
    print(result)
