#Your task is to complete this function
#Your should return the required output
class Solution:
    def maxLen(self, n, arr):
        #Code here
        hash = {}
        prefix = 0
        ans = 0

        for i in range(n):
            prefix += arr[i]
            if prefix == 0:
                ans = i + 1
            if prefix in hash:
                cur = i - hash[prefix]
                ans = max(ans, cur)
            else:
                hash[prefix] = i

        return ans
