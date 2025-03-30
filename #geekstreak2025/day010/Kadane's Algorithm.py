#User function Template for python3

class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        maxS=-10000000
        curr=0
        for i in arr:
            curr+=i
            maxS=max(maxS,curr)
            if curr<0:
                curr=0
        return maxS
