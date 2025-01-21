"""Node is defined as

class Node:
    def __init__(self, data):
		self.data = data
		self.next = None
"""
class Solution:
    def reverseKGroup(self, head, k):
        # Code here
        cur = head
        pre = nxt = new = temp = None
        c = 0
    
        while head:
            while cur and c < k:
                nxt = cur.next
                cur.next = pre
                pre = cur
                cur = nxt
                c += 1
    
            if not new:
                new = pre
            if temp:
                temp.next = pre
    
            temp = head
            pre = None
            head = cur
            c = 0
    
        return new
