#User function Template for python3

class Solution:
	def lps(self, str):
		# code here
		n=len(str)
        curr = 0
        i = 1
        temp = [0] * n
        while i < n:
            if str[i] == str[curr]:
                curr += 1
                temp[i] = curr
                i += 1
            else:
                if curr != 0:
                    curr = temp[curr - 1]
                else:
                    temp[i] = 0
                    i += 1
        return temp[-1]
