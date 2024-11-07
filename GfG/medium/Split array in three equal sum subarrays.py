#User function Template for python3
class Solution:
    
    def findSplit(self, arr):
        # Return an array of possible answer, driver code will judge and return true or false based on
        s=sum(arr)
        if s%3: return [-1,-1]
        cur=0
        s=s//3
        l=r=-1
        for i in range(len(arr)):
            cur+=arr[i]
            if cur==s:
                if l==-1:   l=i
                elif r==-1:
                    r=i
                    break
                cur=0
        if l!=-1 and r!=-1: return [l,r]
        return [-1,-1]
