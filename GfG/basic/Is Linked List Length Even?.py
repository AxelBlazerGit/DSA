class Solution:
    # your task is to complete this function
    # function should return false if length is even
    # else return true
    def isLengthEven(self, head):
        # Code here
        if not head.next:   return False
        size=1
        while head:
            head=head.next
            size+=1
        return bool(size%2)
