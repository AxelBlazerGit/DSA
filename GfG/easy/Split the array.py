#User function Template for python3
class Solution:
	def countgroup(self,arr): 
		#Complete the function
		mod=7+1e9
		ans=0
		for i in arr:   ans^=i
		return 0 if ans else int((2**(len(arr)-1)-1)%mod)
