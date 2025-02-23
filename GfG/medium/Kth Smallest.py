#User function Template for python3
import heapq
class Solution:

    def kthSmallest(self, arr,k):
        heap=[]
        for i in range(k):
            heapq.heappush(heap,-arr[i])
        for i in arr[k:]:
            if heap and -i>heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap,-i)
        return -heap[0]
# 3 4 7 10 15 20
