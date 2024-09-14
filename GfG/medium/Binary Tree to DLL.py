#User function Template for python3

'''
class Node:
    """ Class Node """
    def __init__(self, value):
        self.left = None
        self.data = value
        self.right = None
'''

#Function to convert a binary tree to doubly linked list.
class Solution:
    def __init__(self):
        self.parent = None
        self.ans = None
    def bToDLL(self, root):
        if root is None:
            return
        self.bToDLL(root.left)
        if self.parent is None:
            self.ans = root
        else:
            root.left = self.parent
            self.parent.right = root
        self.parent = root
        self.bToDLL(root.right)
        return self.ans
