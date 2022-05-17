from aiohttp.test_utils import AioHTTPTestCase, TestServer
from aiohttp import web
import fetcher
import queue
import unittest
from unittest.mock import patch
import asyncio
from io import StringIO
import tracemalloc

tracemalloc.start()

class FetcherTestCase(AioHTTPTestCase):
    async def get_application(self):
        async def hello(request):
            return web.Response(text='Hello, World!')
        app = web.Application()
        app.router.add_get('/', hello)
        return app
    async def get_server(self):
        return TestServer(await self.get_application())

    async def setUpAsync(self):
        self.file = "https://example.com\nhttps://python.org"
        self.gq = fetcher.GenQueue(10)
        self.mck_open = unittest.mock.mock_open(read_data=self.file)
        self.srv = await self.get_server()
        await self.srv.start_server()

    async def tearDownAsync(self):
        await self.srv.close()
        
    async def test_load(self):
        with patch("builtins.open", self.mck_open) as mck:
            with open("urls.txt", 'rt') as f:
                await fetcher.load(self.gq, f)

        self.assertEqual(self.gq.get_nowait(), "https://example.com")
        self.assertEqual(self.gq.get_nowait(), "https://python.org")
        with self.assertRaises(asyncio.queues.QueueEmpty):
            self.gq.get_nowait()

    async def test_fetch(self):
        url = str(self.srv.make_url('/'))
        res = await fetcher.fetch(url)
        self.assertEqual(bytes("Hello, World!", 'utf8'), res)

    @patch("sys.stdout", new_callable=StringIO)
    async def test_worker(self, mck):
        url = str(self.srv.make_url('/'))
        await self.gq.put(url)
        url404 = str(self.srv.make_url('/404'))
        await self.gq.put(url404)
        self.gq.loading = unittest.mock.MagicMock()
        self.gq.loading.done = unittest.mock.MagicMock(return_value=True)
        await fetcher.worker(self.gq)
        self.assertRegex(mck.getvalue(), r"Task: [^\n]*")
        self.assertRegex(mck.getvalue(), url404+": {b'404:': 1, b'Not': 1, b'Found': 1}")
        self.assertRegex(mck.getvalue(), url+": {b'Hello,': 1, b'World!': 1}")

    @patch("sys.stdout", new_callable=StringIO)
    async def test_download(self, out):
        with patch("builtins.open", self.mck_open) as mck:
            with open("urls.txt", 'rt') as f:
                await fetcher.download(f, 10)
        self.assertRegex(out.getvalue(), r"Task: \d*\n(https:\/\/python.org: {[^}]*}|https:\/\/example.com: {[^}]*})")


if __name__ == "__main__":
    unittest.main()
