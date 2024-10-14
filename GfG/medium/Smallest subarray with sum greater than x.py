class Solution:
    def smallestSubWithSum(self, x, arr):
        # Your code goes here 
        n = len(arr)

        if sum(arr) < x:
            return 0
    
        ans = n + 1
        cur = 0
        l = 0
    
        for r in range(n):
            cur += arr[r]
    
            while cur > x:
                ans = min(ans, r - l + 1)
                cur -= arr[l]
                l += 1
    
        return ans if ans != n + 1 else 0
