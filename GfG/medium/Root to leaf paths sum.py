# Your task is to complete this function
# function should return max sum level in the tree
class Solution:
    def tree(self,root,num):
        if not root:    return 0
        num*=10
        num+=root.data
        if not root.left and not root.right:    return num
        return self.tree(root.left,num)+self.tree(root.right,num)
    def treePathSum(self,root):
        # Code here
        return self.tree(root,0)
