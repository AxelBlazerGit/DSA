#User function Template for python3

class Solution:
    def totalCount(self, k, arr):
        # code here
        ans=0
        for i in arr:
            if i<k:
                ans+=1
            elif not i%k:
                ans+=i//k
            else:
                ans+=i//k+1
        return ans
