#User function Template for python3

class Solution:
    def maxSum(self,arr):
        # code here
        arr.sort()
        n = len(arr)
        smax=l=0
        r=n-1
        while l<r:
            smax+=2*arr[r]-arr[l]-arr[l+1]
            r-=1
            l+=1
        return smax+arr[n//2]-arr[0]
