class Solution:
    def maxLen(self, arr):
        # code here
        hash={}
        cur=ans=0
        for i in range(len(arr)):
            cur+=1 if arr[i] else -1
            if not cur:
                ans=i+1
            if cur in hash:
                ans=max(ans,i-hash[cur])
            else:
                hash[cur]=i
        return ans
