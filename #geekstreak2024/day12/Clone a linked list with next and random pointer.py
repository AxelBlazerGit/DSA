#User function Template for python3

'''
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None
        self.random=None
        
param: head:  head of linkedList to copy
return: the head of the copied linked list the #output will be 1 if successfully copied
'''
class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        if not head:
            return None
        # insert copied node in between original LL
        temp=head
        while temp:
            copy=Node(temp.data)
            copy.next=temp.next
            temp.next=copy
            temp=copy.next
        # connect randoms of original to randoms of copied
        temp=head
        while temp:
            if temp.random:
                temp.next.random=temp.random.next
            temp=temp.next.next
        # segregate copy and original
        temp=head
        temp0=Node(0)
        copy0=temp0
        while temp:
            copy = temp.next
            copy0.next = copy
            copy0 = copy
            temp.next = copy.next
            temp = temp.next
        return temp0.next # return next because first is dummy node
