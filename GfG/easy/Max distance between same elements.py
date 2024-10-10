class Solution:
    # Your task is to Complete this function
    # functtion should return an integer
    def maxDistance(self, arr):
        # Code here
        hash = {}
        ans = 0
    
        for idx, val in enumerate(arr):
            if val in hash:
                hash[val][1] = idx
            else:
                hash[val] = [idx, idx]
        for val in hash:
            dist = hash[val][1] - hash[val][0]
            ans = max(ans, dist)
        
        return ans
