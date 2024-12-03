#User function Template for python3

class Solution:
    
    #Function to find the maximum occurring character in a string.
    def getMaxOccurringChar(self, s):
        #code here
        hash=[0]*26
        for i in s:
            hash[ord(i)-97]+=1
        ch=None
        f=0
        for idx in range(26):
            if hash[idx] > f:
                ch = chr(97 + idx)
                f = hash[idx]
        return ch
