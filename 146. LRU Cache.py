# 146. LRU Cache
# https://leetcode.com/problems/lru-cache/

class DLLNode:
    
    def __init__(self, key = 0, val = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.reference = dict()
        self.head = DLLNode()
        self.tail = DLLNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def get(self, key: int) -> int:
        if key in self.reference:
            val = self.reference[key].val
            self.remove(key)
            self.add(key, val)
            return val
        return -1
    
    def put(self, key: int, value: int) -> None:
        if key in self.reference:
            self.remove(key)
        self.add(key, value)
        if len(self.reference) > self.capacity:
            self.delete_at_tail()
    
    def delete_at_tail(self) -> None:
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        del self.reference[node.key]
    
    def add(self, key, value) -> None:
        node = DLLNode(key, value)
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node
        self.reference[key] = node
    
    def remove(self, key) -> None:
        node = self.reference[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        del self.reference[key]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
