class InfinityIterator:
    def __init__(self):
        self.n = -10

    def __next__(self):
        self.n += 10
        return self.n

    def __iter__(self):
        return self
