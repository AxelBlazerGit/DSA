#User function Template for python3
class Solution:

	# Function to find maximum
	# product subarray
	def maxProduct(self,arr):
		# code here
        n=len(arr)
        prefix=suffix=1
        ans=-float('inf')
        for i in range(n):
            if not prefix:  prefix=1
            if not suffix:  suffix=1
            prefix*=arr[i]
            suffix*=arr[n-i-1]
            ans=max(ans,prefix,suffix)
        return ans
