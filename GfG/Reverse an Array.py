class Solution:
    def reverseArray(self, arr):
        # code here
        l=0
        r=len(arr)-1
        while l<=r:
            arr[l],arr[r]=arr[r],arr[l]
            r-=1
            l+=1
        return arr
