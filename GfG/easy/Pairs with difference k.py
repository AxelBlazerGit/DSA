#User function Template for python3
from collections import Counter
class Solution:
	def countPairsWithDiffK(self,arr, k):
    	# code here
    	arr=Counter(arr)
    	pairs=0
    	for i in arr:
            if i + k in arr:
                pairs += arr[i] * arr[i + k]
            if k != 0 and i - k in arr:
                pairs += arr[i] * arr[i - k]
                
        return pairs // 2
