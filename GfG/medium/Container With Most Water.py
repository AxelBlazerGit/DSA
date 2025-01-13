
class Solution:
    def maxWater(self, arr):
        # code here
        # we dont need to worry about the heights being like physical containers..
        # we can simply traverse to find max area possible with two pointers
        l,r=0,len(arr)-1
        ans=0
        while r-l:
            ans=max(ans,(r-l)*min(arr[r],arr[l]))
            if arr[r]>arr[l]:
                l+=1
            else:
                r-=1
        return ans
