#User function Template for python3

def partition(piv, left, right):
    temp = piv.next
    while temp:
        link = temp.next
        if temp.data <= piv.data:
            temp.next = left
            left = temp
        else:
            temp.next = right
            right = temp
        temp = link
    return left, right

def quickSort(head):
    if not head or not head.next:
        return head
    
    left, right = None, None
    left, right = partition(head, left, right)
    left = quickSort(left)
    right = quickSort(right)
    
    if left:
        current = left
        while current.next:
            current = current.next
        current.next = head
    else:
        left = head
        
    head.next = right
    
    return left
