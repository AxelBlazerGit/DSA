
class Solution:
    def maxWater(self, arr):
        # code here
        l, r = 0, len(arr) - 1
        ans, mxL, mxR = 0, 0, 0
    
        while l <= r:
            if arr[l] <= arr[r]:
                if arr[l] >= mxL:
                    mxL = arr[l]
                    l += 1
                else:
                    ans += mxL - arr[l]
                    l += 1
            else:
                if arr[r] >= mxR:
                    mxR = arr[r]
                    r -= 1
                else:
                    ans += mxR - arr[r]
                    r -= 1
    
        return ans
