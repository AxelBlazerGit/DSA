#User function Template for python3

'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def boundaryTraversal(self, root):
        # Code here
        boundary=[]
        if not root:
            return boundary
        def leaf(node):
            return not node.right and not node.left
        def lbound(node):
            cur = node.left
            while cur:
                if not leaf(cur):
                    boundary.append(cur.data)
                cur = cur.left if cur.left else cur.right
        def rbound(node):
            cur = node.right
            rBoundary = []
            while cur:
                if not leaf(cur):
                    rBoundary.append(cur.data)
                cur = cur.right if cur.right else cur.left
            boundary.extend(reversed(rBoundary))
        def leaves(node):
            if not node:
                return
            if leaf(node):
                boundary.append(node.data)
                return
            leaves(node.left)
            leaves(node.right)
        
        if not leaf(root):
            boundary.append(root.data)
        
        lbound(root)
        leaves(root)
        rbound(root)

        return boundary
