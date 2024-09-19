class Solution:
    def transitionPoint(self, arr, n): 
        # Code here
        if not arr[-1]:
            return -1
        if arr[0]:
            return 0
        l=0
        n=len(arr)
        h=n-1
        ans=-1
        while(l<=h):
            mid=l+h
            mid//=2
            if not arr[mid]:
                ans=mid
                l=mid+1
            else:
                h=mid-1
        return ans+1
