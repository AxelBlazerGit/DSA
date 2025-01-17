#User function Template for python3

class Solution:
    def productExceptSelf(self, arr):
        #code here
        n = len(arr)
        res = [1] * n
    
        l = 1
        for i in range(n):
            res[i] = l
            l *= arr[i]
    
        r = 1
        for i in range(n - 1, -1, -1):
            res[i] *= r
            r *= arr[i]
    
        return res
