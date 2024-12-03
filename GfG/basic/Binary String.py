#User function Template for python3

class Solution:
    
    #Function to count the number of substrings that start and end with 1.
    def binarySubstring(self,n,s):
        #code here
        n=0
        for i in s:
            if i=='1':
                n+=1
        return n*(n-1)//2
