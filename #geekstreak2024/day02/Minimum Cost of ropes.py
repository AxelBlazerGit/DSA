#User function Template for python3
class Solution:
    from typing import List
    #Function to return the minimum cost of connecting the ropes.
    def minCost(self, arr: List[int]) -> int:
        # code here
        heapq.heapify(arr)
        ans=0
        while len(arr) > 1:
            temp=heapq.heappop(arr)+heapq.heappop(arr)
            heapq.heappush(arr,temp)
            ans+=temp
        return ans
