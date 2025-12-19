class Node:
    def __init__(self, val, prev = None, next = None):
        self.val = val
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self, val = None):
        self.begin = None
        self.end = None

    def append(self, val):
        node = Node(val)
        if self.end is not None:
            node.prev = self.end
            self.end.next = node
            self.end = node
        #first element added to list
        else:
            self.begin = node
            self.end = node
    
    def dequeue(self):
        if self.begin is None:
            return None
        else:
            node = self.begin
            self.begin = self.begin.next
            if self.begin is not None:
                self.begin.prev = None
            return node.val
        
    def remove(self, val):
        if self.begin is None:
            return None
        else:
            node = self.begin
            while node is not None and node.val != val:
                node = node.next
            if node is None:
                return None
            if node.prev is not None and node.next is not None:
                node.prev.next = node.next
                node.next.prev = node.prev
            elif node.prev is None and node.next is not None:
                self.begin = node.next
                node.next.prev = None
            elif node.next is None and node.prev is not None:
                self.end = node.prev
                node.prev.next = None
            else:
                self.begin = None
                self.end = None
            return None
    

class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.queue = DoubleLinkedList()
        self.capacity = capacity
        self.used = 0

    def get(self, key: int) -> int:
        val = self.cache.get(key, -1)
        if val != -1:
            self.queue.remove(key)
            self.queue.append(key)
        return val
        
    def put(self, key: int, value: int) -> None:
        if self.cache.get(key) is not None:
            self.queue.remove(key)
        elif self.used == self.capacity:
            delkey = self.queue.dequeue()
            del self.cache[delkey]
        else:
            self.used += 1
        self.cache[key] = value
        self.queue.append(key)