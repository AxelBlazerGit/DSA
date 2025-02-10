from collections import defaultdict
'''
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None
'''
class Solution:
    def sumK(self,root,k):
        # code here
        hash = defaultdict(int)
        hash[0]+=1
        self.total = 0

        def findPathSum(node, cur):
            if not node:
                return

            cur += node.data

            if (cur - k) in hash:
                self.total += hash[cur - k]

            hash[cur] += 1

            findPathSum(node.left, cur)
            findPathSum(node.right, cur)

            hash[cur] -= 1

        findPathSum(root, 0)
        return self.total
