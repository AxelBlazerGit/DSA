#User function Template for python3
class Solution:
    def kthMissing(self, arr, k):
        # code here
        s=0
        e=len(arr)-1
        while s<=e:
            m=(s+e)//2
            absent=arr[m]-m-1
            if absent<k:
                s=m+1
            else:
                e=m-1
        return s+k
