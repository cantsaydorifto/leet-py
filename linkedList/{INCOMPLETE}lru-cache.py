class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.used = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            if key in self.used:
                self.used[key] += 1
            else:
                self.used[key] = 1
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if len(self.cache) >= self.capacity:
            minKey = min(self.used, key=lambda x: self.used[x])
            self.used.pop(minKey)
            self.cache.pop(minKey)
        self.cache[key] = value
        self.used[key] = 1

    def __str__(self) -> str:
        return f"Cache: {self.cache} Used: {self.used}"


# Your LRUCache object will be instantiated and called as such:
lRUCache = LRUCache(2)
lRUCache.put(1, 1)
# cache is {1=1}
lRUCache.put(2, 2)
# cache is {1=1, 2=2}
print(lRUCache.get(1))
# return 1
# print(lRUCache)
lRUCache.put(3, 3)
# LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# print(lRUCache)
print(lRUCache.get(2))
# returns -1 (not found)
print(lRUCache.put(4, 4))
# LRU key was 1, evicts key 1, cache is {4=4, 3=3}
print(lRUCache.get(1))
# return -1 (not found)
print(lRUCache.get(3))
# return 3
print(lRUCache.get(4))
