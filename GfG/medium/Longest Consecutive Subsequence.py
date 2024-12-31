 #User function Template for python3
#  from collections import Counter
class Solution:
    
    # arr[] : the input array
    
    #Function to return length of longest subsequence of consecutive integers.
    def longestConsecutive(self,arr):
        #code here
        arr = set(arr)
        lc = 0
        
        for num in arr:
            if num - 1 not in arr:
                current_num = num
                streak = 1
                while current_num + 1 in arr:
                    current_num += 1
                    streak += 1
                lc = max(lc, streak)
        
        return lc
