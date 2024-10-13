#User function Template for python3

'''class Node: 
   
    # Function to initialize the node object 
    def __init__(self, data): 
        self.data = data  
        self.next = None'''

class Solution:
    def deleteAlt(self, head):
        # code here
        if not head or not head.next:
            return None
        temp=head
        while temp and temp.next:
            temp.next=temp.next.next
            temp=temp.next
        return head
