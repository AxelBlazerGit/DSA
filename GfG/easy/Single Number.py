#User function Template for python3

class Solution:
    
    def getSingle(self,arr):
        # code here
        single=0
        for i in arr:
            single^=i
        return single
