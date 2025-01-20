#User function Template for python3
'''
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

'''
class Solution:
    def sortedMerge(self,head1, head2):
        # code here
        l1=head1
        l2=head2
        temp=Node(0)
        head=temp
        while l1 and l2:
            if l1.data<l2.data:
                temp.next=l1
                l1=l1.next
            else:
                temp.next=l2
                l2=l2.next
            temp=temp.next
        temp.next=l1 if l1 else l2
        return head.next
