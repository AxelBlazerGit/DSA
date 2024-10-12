class Solution:
    def pairWithMaxSum(self, arr):
        #code here
        mx=-1
        if len(arr)==1 or not arr:
            return mx
        for i in range(len(arr)-1):
            mx=max(mx,arr[i]+arr[i+1])
        return mx
