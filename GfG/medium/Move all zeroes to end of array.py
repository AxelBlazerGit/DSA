#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
    	z=p=0
    	while z<len(arr):
    	   if arr[z]:
    	       arr[p],arr[z]=arr[z],arr[p]
    	       p+=1
    	   z+=1
        return arr
