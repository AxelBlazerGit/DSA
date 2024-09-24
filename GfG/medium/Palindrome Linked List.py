#User function Template for python3
'''
	Your task is to check if given linkedlist
	is a pallindrome or not.
	
	Function Arguments: head (reference to head of the linked list)
	Return Type: boolean , no need to print just return True or False.

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}

	Contributed By: Nagendra Jha
'''
#Function to check whether the list is palindrome.
class Solution:
    def isPalindrome(self, head):
        #code here
        slow = head
        fast = head
    
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        prev = None
        current = slow
    
        while current:
            nextNode = current.next
            current.next = prev
            prev = current
            current = nextNode
        left = head
        right = prev
    
        while right:
            if left.data != right.data:
                return False
            left = left.next
            right = right.next
    
        return True
