#User function Template for python3
'''
class DLLNode:
    def __init__(self,val) -> None:
        self.data = val
        self.prev = None
        self.next = None
'''
class Solution:
    def sortAKSortedDLL(self, head, k):
        # Code Here
        heap=[]
        temp=head
        for idx in range(k+1):
            heapq.heappush(heap,temp.data)
            temp=temp.next
        temp2=head
        while heap:
            temp2.data=heapq.heappop(heap)
            if temp:
                heapq.heappush(heap,temp.data)
                temp=temp.next
            temp2=temp2.next
        return head
