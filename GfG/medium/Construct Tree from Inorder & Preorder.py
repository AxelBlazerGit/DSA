#User function Template for python3

'''
# Node class
class Node:
    def __init__(self,val):
        self.data = val
        self.right = None
        self.left = None

'''
# Note: Build tree and return root node
class Solution:
    def buildTree(self, inorder, preorder):
        # code here
        if not preorder or not inorder:
            return None
        root=Node(preorder[0])
        idx=inorder.index(preorder[0])
        root.left=self.buildTree(inorder[:idx],preorder[1:idx+1])
        root.right=self.buildTree(inorder[idx+1:],preorder[idx+1:])
        return root
