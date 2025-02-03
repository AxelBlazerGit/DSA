"""
class Node:
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
"""
from collections import deque
class Solution:
    def levelOrder(self, root):
        # Your code here
        order=[]
        dq = deque((root,))
        while dq:
            temp=[]
            for _ in range(len(dq)):
                
                node=dq.popleft()
                temp.append(node.data)
                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)
            order.append(temp)
        return order
