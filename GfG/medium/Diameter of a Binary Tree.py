'''
# Tree Node
class Node:

    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def diameter(self, root):
        # Your code here
        dia=[0]
        def heightSum(root,dia):
            if not root:
                return 0
            l=heightSum(root.left,dia) if root.left else 0
            r=heightSum(root.right,dia) if root.right else 0
            dia[0]=max(dia[0],l+r)
            return 1+max(l,r)
        heightSum(root,dia)
        return dia[0]
