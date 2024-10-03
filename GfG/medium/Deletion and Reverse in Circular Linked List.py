#User function Template for python3
'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    # Function to reverse a circular linked list
    def reverse(self, head):
        #code here
        if not head or not head.next:
            return head
        
        prev = None
        curr = head
        next_node = None
        first = head
        
        while True:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            if curr == first:
                break
        head.next = prev
        return prev
        
    # Function to delete a node from the circular linked list
    def deleteNode(self, head, key):
        #code here
        if not head:
            return None
        
        curr = head
        prev = None
        if head.data == key and head.next == head:
            return None
        while True:
            if curr.data == key:
                break
            prev = curr
            curr = curr.next
            if curr == head:
                return head
        if curr == head:
            last = head
            while last.next != head:
                last = last.next
            last.next = head.next
            head = head.next
        else:
            prev.next = curr.next
        
        return head
