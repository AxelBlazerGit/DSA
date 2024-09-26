#User function Template for python3
from collections import deque
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,k,arr):
        #code here
        n=len(arr)
        if n==1:
            return arr
        elif n<k:
            return max(arr)
        curr=0
        nxt=0
        seq=deque()
        ans=[]
        while nxt<n:
            while seq and seq[-1]<arr[nxt]:
                seq.pop()
            seq.append(arr[nxt])
            if nxt-curr+1<k:
                nxt+=1
            elif nxt-curr+1==k:
                ans.append(seq[0])
                if seq[0]==arr[curr]:
                    seq.popleft()
                curr+=1
                nxt+=1
        return ans
