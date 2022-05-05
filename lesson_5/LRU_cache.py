import collections


class LRUCache(collections.UserDict):
    def __init__(self, limit):
        self.limit = limit
        super().__init__()

    def get(self, key):
        if key not in self.keys():
            return None
        value = self.data.pop(key)
        self.data[key] = value
        return value

    def set(self, key, value):
        self.data.pop(key, None)
        while len(self) >= self.limit:
            first_key = next(iter(self))
            self.data.pop(first_key)
        self.data[key] = value
