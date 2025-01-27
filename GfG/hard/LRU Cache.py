#User function Template for python3

# design the class in the most optimal way
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = self.next = None
        
class LRUCache:
      
    #Constructor for initializing the cache capacity with the given value.  
    def __init__(self, cap):
        #code here
        self.capacity = capacity
        self.lru = {}
        self.head = self.tail = Node(-1, -1)
        # print(id(self.head), id(self.tail))
        self.head.next = self.tail
        self.tail.prev = self.head
        # print(id(self.head), id(self.tail))
        
    def pop(self, node: Node):
        prev, next = node.prev, node.next
        prev.next = next
        next.prev = prev
        
    def append(self, node: Node):
        prev = self.tail.prev
        prev.next = node
        node.prev = prev
        node.next = self.tail
        self.tail.prev = node
        
        
    #Function to return value corresponding to the key.
    def get(self, key):
        #code here
        if key in self.lru:
            node = self.lru[key]
            self.pop(node)
            self.append(node)
            return node.value
        return -1
        
        
    #Function for storing key-value pair.   
    def put(self, key, value):
        #code here
        if key in self.lru:
            node = self.lru[key]
            node.value = value
            self.pop(node)
            self.append(node)
        else:
            if len(self.lru) == self.capacity:
                lruNode = self.head.next
                self.pop(lruNode)
                del self.lru[lruNode.key]
            temp = Node(key, value)
            self.lru[key] = temp
            self.append(temp)
