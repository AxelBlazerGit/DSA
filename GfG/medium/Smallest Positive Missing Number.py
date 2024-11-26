#User function Template for python3

class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr):
        #Your code here
        hash=set([x for x in arr if x>0])
        ans=1
        for i in hash:
            if ans in hash:
                ans+=1
            else:
                break
        return ans
