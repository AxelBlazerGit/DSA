
#User function Template for python3

class Solution:
    
    #Function to check if a string is Isogram or not.
    def isIsogram(self,s):
        #Your code here
        # if len(s)>26:
            # return 0
        return len(s) == len(set(s))
