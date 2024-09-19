#User function Template for python3

class Solution:
    def binS(self, arr, s, e, x):
        while s<=e:
            mid=s+e
            mid//=2
            if not arr[mid]:
                e=mid-1
            else:
                if not arr[mid+1] or mid==len(arr)-1:
                    return mid+1
                else:
                    s=mid+1
        return -1
    def countZeroes(self, arr):
        # code here 
        if arr[-1]:
            return 0
        if not arr[0]:
            return len(arr)
        return len(arr) - self.binS(arr,0,len(arr)-1,1)
