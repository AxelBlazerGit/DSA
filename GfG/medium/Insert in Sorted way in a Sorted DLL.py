#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
'''
class Solution:
    # Function to insert a node in a sorted doubly linked list.
    def sortedInsert(self, head, x):
        #code here
        temp = Node(x)
        
        if x <= head.data:
            temp.next = head
            head.prev = temp
            return temp
        
        cur = head
        while cur.next and cur.data < x:
            cur = cur.next
            
        if cur.data >= x:
            prev_node = cur.prev
            prev_node.next = temp
            temp.prev = prev_node
            temp.next = cur
            cur.prev = temp
            return head
            
        cur.next = temp
        temp.prev = cur
        
        return head
