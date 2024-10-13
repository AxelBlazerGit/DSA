#User function Template for python3

'''

#Linked list class
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        '''
class Solution:
    # Function to count nodes of a linked list.
    def getCount(self, head):
        # code here
        if not head:
            return 0
        nodes=1
        while head.next:
            nodes+=1
            head=head.next
        return nodes
