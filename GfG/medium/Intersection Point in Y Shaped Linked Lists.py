#User function Template for python3
'''
	Function to return the value at point of intersection
	in two linked list, connected in y shaped form.
	
	Function Arguments: head_a, head_b (heads of both the lists)
	
	Return Type: value in NODE present at the point of intersection
	             or -1 if no common point.

	Contributed By: Nagendra Jha

	{
		# Node Class
		class Node:
		    def __init__(self, data):   # data -> value stored in node
		        self.data = data
		        self.next = None
	}
'''

#Function to find intersection point in Y shaped Linked Lists.
def intersetPoint(head1,head2):
    #code here
    n1=n2=0
    temp1=head1
    temp2=head2
    while temp1 and temp2:
        n1+=1
        n2+=1
        temp1=temp1.next
        temp2=temp2.next
    while temp1:
        n1+=1
        temp1=temp1.next
    while temp2:
        n2+=1
        temp2=temp2.next
    x=abs(n1-n2)
    temp1=head1
    temp2=head2
    if n1>n2:
        while x:
            temp1=temp1.next
            x-=1
    else:
        while x:
            temp2=temp2.next
            x-=1
    while temp1:
        if temp1==temp2:
            break
        else:
            temp1=temp1.next
            temp2=temp2.next
    return temp1.data if temp1 else -1
