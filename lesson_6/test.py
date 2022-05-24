import unittest
import unittest.mock
import server
import client
import queue

class ServerTestCase(unittest.TestCase):
    
    def setUp(self):
        self.q = queue.Queue()

    def test_worker(self):
        mm = unittest.mock.MagicMock()
        self.q.put((mm, "https://example.com"))
        try:
            server.worker(self.q, 3)
        except queue.Empty:
            pass
        res = mm.mock_calls[0].args
        self.assertEqual(b'{"{": 5, "}": 5, "<meta": 3}', res[0])

class ClientTestCase:
    ...

if __name__ == "__main__":
    unittest.main()
