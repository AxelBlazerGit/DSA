#User function Template for python3

'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
class Solution:
    #Function to find the height of a binary tree.
    def height(self, root):
        # code here
        if not root:
            return -1
        
        return max(self.height(root.left),self.height(root.right))+1
