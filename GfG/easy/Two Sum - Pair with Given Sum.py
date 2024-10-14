#User function Template for python3
class Solution:
	def twoSum(self,arr, target):
		# code here
		hash=set()
		for i in arr:
		    if target-i in hash:
		        return True
            hash.add(i)
        return False
