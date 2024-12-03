
#User function Template for python3

class Solution:
    
    #Function to calculate sum of all numbers present in a string.
    def findSum(self,s):
        #code here
        sm=cur=0
        for i in s:
            if i.isdigit():
                cur*=10
                cur+=int(i)
            else:
                sm+=cur
                cur=0
        return sm+cur
