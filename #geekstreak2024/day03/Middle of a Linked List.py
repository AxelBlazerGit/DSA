# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''
class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # Code here
        # return the value stored in the middle node
        n=0
        temp=head
        while temp:
            n+=1
            temp=temp.next
        n//=2
        temp=head
        while n:
            temp=temp.next
            n-=1
        return temp.data
