#User function Template for python3

class Solution:
    
    #Function to find maximum number of consecutive steps
    #to gain an increase in altitude with each step.
    def maxStep(self, arr):
        #Your code here
        jump=0
        temp=0
        for i in range(1,len(arr)):
            if arr[i]>arr[i-1]:
                temp+=1
            else:
                jump=max(jump, temp)
                temp=0
        return max(jump,temp)
