#User function Template for python3
from collections import Counter

class Solution:
    
    #Function to find all elements in array that appear more than n/k times.
    def countOccurence(self,arr,n,k):
        #Your code here
        arr=Counter(arr)
        ans=0
        for i in arr:
            if arr[i]>n/k:
                ans+=1
        return ans
