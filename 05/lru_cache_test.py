import unittest
from lru_cache import LRUCache


class TestLRUCache(unittest.TestCase):

    def test_set_and_get(self):
        capacity = 10
        test_cache = LRUCache(capacity)
        for test_val in range(capacity):
            test_cache.set(test_val, test_val)
        for test_val in range(capacity):
            self.assertEqual(test_cache.get(test_val), test_val)

        self.assertEqual(test_cache.get(capacity + 1), None)
        test_cache.set(capacity + 1, capacity + 1)
        self.assertEqual(test_cache.get(capacity + 1), capacity + 1)
        self.assertEqual(test_cache.get(0), None)
        self.assertEqual(test_cache.limit, capacity)

    def test_replace_to_front(self):
        capacity = 3
        test_cache = LRUCache(capacity)
        for test_val in range(capacity):
            test_cache.set(test_val, test_val)
            self.assertEqual(test_cache.get(0), 0)

        for test_val in range(1, capacity + 1):
            test_cache.set(test_val, test_val)
        self.assertEqual(test_cache.get(0), None)
        self.assertEqual(test_cache.limit, capacity)


if __name__ == '__main__':
    unittest.main()
