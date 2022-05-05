import unittest
from LRU_cache import LRUCache


class LRUCacheTestCase(unittest.TestCase):
    def setUp(self):
        self.ch = LRUCache(limit=3)

    def test_regular(self):
        self.assertIsNone(self.ch.get("k1"))
        self.ch.set("k1", "v0")
        self.assertEqual(self.ch.get("k1"), "v0")
        self.ch.set("k1", "v1")
        self.assertEqual(self.ch.get("k1"), "v1")
        self.assertIsNone(self.ch.get("k2"))
        self.ch.set("k2", "v2")
        self.assertEqual(self.ch.get("k1"), "v1")
        self.assertEqual(self.ch.get("k2"), "v2")

    def test_overflow(self):
        self.ch.set("k1", "v1")
        self.ch.set("k2", "v2")
        self.ch.set("k3", "v3")
        self.assertEqual(self.ch.get("k1"), "v1")
        self.assertEqual(self.ch.get("k2"), "v2")
        self.assertEqual(self.ch.get("k3"), "v3")
        self.ch.set("k4", "imposter")
        self.assertIsNone(self.ch.get("k1"))
        self.assertEqual(self.ch.get("k2"), "v2")
        self.assertEqual(self.ch.get("k3"), "v3")
        self.assertEqual(self.ch.get("k4"), "imposter")

        self.ch.get("k2")
        self.ch.get("k3")
        self.ch.set("k5", "v5")
        self.assertEqual(self.ch.get("k2"), "v2")
        self.assertEqual(self.ch.get("k3"), "v3")
        self.assertEqual(self.ch.get("k5"), "v5")

    def test_extra(self):
        self.ch.set("k1", "v1")
        self.ch.set("k2", "v2")
        self.ch.set("k3", "v3")
        self.assertEqual(self.ch.get("k1"), "v1")
        self.assertEqual(self.ch.get("k2"), "v2")
        self.assertEqual(self.ch.get("k3"), "v3")
        self.ch.set("k2", "v2.")
        self.assertEqual(self.ch.get("k1"), "v1")
        self.assertEqual(self.ch.get("k3"), "v3")
        self.assertEqual(self.ch.get("k2"), "v2.")
        self.ch.set("k4", "v4")
        self.assertEqual(self.ch.get("k3"), "v3")
        self.assertEqual(self.ch.get("k2"), "v2.")
        self.assertEqual(self.ch.get("k3"), "v3")

    def test_limit1(self):
        ch = LRUCache(limit=1)
        ch.set(1, 1)
        ch.set(2, 2)
        ch.set(2, 0)
        self.assertIsNone(ch.get(0))
        self.assertIsNone(ch.get(1))
        self.assertEqual(ch.get(2), 0)

    def test_fulloverload(self):
        self.ch.set(1, 1)
        self.ch.set(2, 2)
        self.ch.set(3, 3)
        self.assertEqual(self.ch.get(1), 1)
        self.assertEqual(self.ch.get(2), 2)
        self.assertEqual(self.ch.get(3), 3)
        self.ch.set(4, 4)
        self.ch.set(5, 5)
        self.ch.set(6, 6)
        self.assertEqual(self.ch.get(4), 4)
        self.assertEqual(self.ch.get(5), 5)
        self.assertEqual(self.ch.get(6), 6)

    def test_dup_refresh(self):
        self.ch.set(1, 1)
        self.ch.set(2, 2)
        self.ch.set(3, 3)
        self.ch.set(1, 10)
        self.assertEqual(self.ch.get(2), 2)
        self.assertEqual(self.ch.get(3), 3)
        self.assertEqual(self.ch.get(1), 10)
        self.ch.set(4, 4)
        self.ch.set(5, 5)
        self.assertIsNone(self.ch.get(2))
        self.assertIsNone(self.ch.get(3))
        self.assertEqual(self.ch.get(1), 10)
        self.assertEqual(self.ch.get(4), 4)
        self.assertEqual(self.ch.get(5), 5)
        self.ch.set(6, 6)
        self.assertIsNone(self.ch.get(1))
        self.assertEqual(self.ch.get(4), 4)
        self.assertEqual(self.ch.get(5), 5)
        self.assertEqual(self.ch.get(6), 6)
        self.assertListEqual(list(self.ch), [4, 5, 6])


if __name__ == "__main__":
    unittest.main()
