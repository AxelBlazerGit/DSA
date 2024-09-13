#User function Template for python3

class Solution:
    def rearrange(self,arr):
        # code here
        n=len(arr)
        plus=[x for x in arr if x>=0]
        minus=[x for x in arr if x<0]
        p,n=0,0
        idx=0
        while p<len(plus) and n<len(minus):
            arr[idx]=plus[p]
            idx+=1
            p+=1
            arr[idx]=minus[n]
            idx+=1
            n+=1
        while p<len(plus):
            arr[idx]=plus[p]
            idx+=1
            p+=1
        while n<len(minus):
            arr[idx]=minus[n]
            idx+=1
            n+=1
        return arr
