#User function Template for python3

""" Node Class
    class Node:
        def __init__(self, data):   # data -> value stored in node
            self.data = data
            self.next = None
"""
class Solution:
    def findFirstNode(self, head):
        #code here
        s=f=head
        while f and f.next:
            s=s.next
            f=f.next.next
            if s==f:
                break
        if s!=f:
            return Node(-1)
        
        s=head
        while s!=f:
            s=s.next
            f=f.next
        return s
