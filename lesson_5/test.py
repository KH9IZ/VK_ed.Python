import unittest
from LRU_cache import LRUCache


class LRUCacheTestCase(unittest.TestCase):

    def setUp(self):
        self.ch = LRUCache(limit=3)

    def test_regular(self):
        self.assertIsNone(self.ch.get('k1'))
        self.ch.set('k1', 'v0')
        self.assertEqual(self.ch.get('k1'), 'v0')
        self.ch.set('k1', 'v1')
        self.assertEqual(self.ch.get('k1'), 'v1')
        self.assertIsNone(self.ch.get('k2'))
        self.ch.set('k2', 'v2')
        self.assertEqual(self.ch.get('k1'), 'v1')
        self.assertEqual(self.ch.get('k2'), 'v2')

    def test_overflow(self):
        self.ch.set('k1', 'v1')
        self.ch.set('k2', 'v2')
        self.ch.set('k3', 'v3')
        self.assertSequenceEqual(list(self.ch.values()), ['v1', 'v2', 'v3'])
        self.ch.set('k4', 'imposter')
        self.assertSequenceEqual(list(self.ch.values()), ['v2', 'v3', 'imposter'])
        self.ch.get('k2')
        self.ch.get('k3')
        self.ch.set('k5', 'v5')
        self.assertSequenceEqual(list(self.ch.values()), ['v2', 'v3', 'v5'])


if __name__ == "__main__":
    unittest.main()
