
'''
# Node Class:
class Node:
    def init(self,val):
        self.data = val
        self.left = None
        self.right = None
'''

class Solution:
    def inOrder(self,root):
        # code here
        if not root:    return []
        return self.inOrder(root.left)+[root.data]+self.inOrder(root.right)
