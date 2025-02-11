#User function Template for python3


class Solution:
    
    #Function to check whether a Binary Tree is BST or not.
    def isBST(self, root):
        #code here
        def inorder(root):
            if root:
                inorder(root.left)
                io.append(root.data)
                inorder(root.right)

        io=[]
        inorder(root)
        
        for i in range(1,len(io)):
            if io[i]<=io[i - 1]:
                return False
        return True
