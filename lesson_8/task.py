import LRU_cache

class Exam:
    def __init__(name, score):
        self.score = score
        self.name = name

class ExamSolid:
    __slots__ = ("name", "score")

    def __init__(name, score):
        self.score = score
        self.name = name

if __name__ == "__main__":
    cache = LRUCache(100)
    cahce.set("default", Exam('Python', 5))
    cache.set("slots", ExamSolid('C++', 5))

