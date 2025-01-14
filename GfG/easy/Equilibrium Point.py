# User function Template for python3

class Solution:
    #Function to find equilibrium point in the array.
    def findEquilibrium(self, arr):
        # code here
        s=sum(arr)
        cur=0
        for i in range(len(arr)):
            s-=arr[i]
            if cur==s:
                return i
            cur+=arr[i]
        return -1
