#User function Template for python3
import heapq as h
class Solution:
    def nearlySorted(self, arr, k):
        #code
        heap=arr[:k+1]
        h.heapify(heap)
        idx=0
        for i in range(k+1,len(arr)):
            arr[idx]=h.heappop(heap)
            h.heappush(heap,arr[i])
            idx+=1
        while heap:
            arr[idx]=h.heappop(heap)
            idx+=1
        return arr
