# User function Template for python3

class Solution:
    def longestSubarray(self, arr, k):  
        # code here
        hash = {}
        cur = ans = 0
        
        for i, num in enumerate(arr):
            cur += num
            if cur == k:
                ans = max(ans, i + 1)
            if (cur - k) in hash:
                ans = max(ans, i - hash[cur - k])
            if cur not in hash:
                hash[cur] = i
        
        return ans
