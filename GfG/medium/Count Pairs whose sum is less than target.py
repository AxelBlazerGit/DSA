#User function Template for python3
from bisect import bisect_left
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        arr.sort()
        pairs=0
        for i in range(len(arr)):
            pairs+=bisect_left(arr,target-arr[i],i+1)-i-1
        return pairs
