#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        # repeat= (sum(arr)-n n+1//2 + sum(arr[i]^2)-i^2) // 2
        # missing = sum(arr)-nn+1//2
        # subtract array sum to expected
        # subtract squares of elements of array to squares of elements from 1->n
        n=len(arr)
        degree1=n*(n+1)//2
        degree2=n*(n+1)*(2*n+1)//6
        arrsum=0
        sqsum=0
        for i in arr:
            arrsum+=i
            sqsum+=i*i
        temp1=arrsum-degree1
        temp2=sqsum-degree2
        temp2//=temp1
        missing=(temp1+temp2)//2
        repeat=missing-temp1
        return missing,repeat
