#User function Template for python3
'''
class Node:
    def _init_(self, data):
        self.data = data
        self.next = None

'''

class Solution:
    def alternatingSplitList(self, head):
        #Your code here
        list1_temp = Node(0)
        list2_temp = Node(0)
        list1_tail = list1_temp
        list2_tail = list2_temp
        is_list1 = True
        current = head

        while current:
            if is_list1:
                list1_tail.next = current
                list1_tail = list1_tail.next
            else:
                list2_tail.next = current
                list2_tail = list2_tail.next

            is_list1 = not is_list1
            current = current.next

        list1_tail.next = None
        list2_tail.next = None

        return [list1_temp.next, list2_temp.next]
