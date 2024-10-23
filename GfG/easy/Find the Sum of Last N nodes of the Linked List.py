#User function Template for python3

'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
'''
class Solution:
    def sumOfLastN_Nodes(self, head, n):
        #function should return sum of last n nodes
        k=0
        temp=head
        while temp:
            k+=1
            temp=temp.next
        for _ in range(k-n):
            head=head.next
        ans=0
        while head:
            ans+=head.data
            head=head.next
        return ans
