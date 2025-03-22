#User function Template for python3

class Solution:
	def pushZerosToEnd(self,arr):
    	# code here
        z=nz=0
        while z<len(arr):
            if arr[z]:
                arr[z],arr[nz]=arr[nz],arr[z]
                nz+=1
            z+=1
        return arr
