#User function Template for python3

'''

class Node():
    def __init__(self,x):
        self.data = x
        self.right = None
        self.down=None

'''

class Solution:
    def constructLinkedMatrix(self, mat):
        if not mat:
            return None
        
        n = len(mat)
        nodes = [[None for _ in range(n)] for _ in range(n)]
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                node = Node(mat[i][j])
                if j < n-1:
                    node.right = nodes[i][j+1]
                    
                if i < n-1:
                    node.down = nodes[i+1][j]
                nodes[i][j] = node
        return nodes[0][0]
