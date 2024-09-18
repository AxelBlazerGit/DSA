# User function Template for python3

class Solution:
    
    #Function to reverse words in a given string.
    def reverseWords(self,str):
        # code here 
        str=str.split(".")
        str=".".join(str[::-1])
        return str
