#User function Template for python3
class Solution:
    def merge(self, root1, root2):
        # code here
        def inorder(root):
            def traverse(node):
                if node is None:
                    return
                traverse(node.left)
                temp.append(node.data)
                traverse(node.right)
                
            temp = []
            traverse(root)
            return temp
        return sorted(inorder(root1) + inorder(root2))
