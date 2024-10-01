# your task is to complete this function
# Function should return an integer value
# head1 denotes head node of 1st list
# head2 denotes head node of 2nd list

'''
class node:
    def __init__(self):
        self.data = None
        self.next = None
'''

class Solution:
    def multiply_two_lists(self, first, second):
        # Code here
        MOD = 10**9 + 7
        def ListToNum(head):
            num = 0
            while head:
                num = (num * 10 + head.data) % MOD
                head = head.next
            return num
        num1 = ListToNum(first)
        num2 = ListToNum(second)
        result = (num1 * num2) % MOD
        return result
