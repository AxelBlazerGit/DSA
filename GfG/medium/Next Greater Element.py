# User function Template for python3

class Solution:
    # Function to find the next greater element for each element of the array.
    def nextLargerElement(self, arr):
        # code here
        stk=[]
        ngr=[-1]*len(arr)
        for idx in range(len(arr)-1,-1,-1):
            while stk and stk[-1]<=arr[idx]:
                stk.pop()
            if stk:
                ngr[idx]=stk[-1]
                # else:
                #     ngr.append(-1)
            # else:
            #     ngr.append(-1)
            stk.append(arr[idx])
        return ngr
