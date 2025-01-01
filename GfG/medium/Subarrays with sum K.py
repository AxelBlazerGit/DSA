#User function Template for python3
from collections import defaultdict
class Solution:
    def countSubarrays(self, arr, k):
        # code here
        hash=defaultdict(int)
        hash[0]+=1
        cur=cnt=0
        for i in arr:
            cur+=i
            if cur-k in hash:
                cnt+=hash[cur-k]
            hash[cur]+=1
        return cnt
