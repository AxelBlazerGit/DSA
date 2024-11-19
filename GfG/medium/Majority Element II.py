class Solution:
    # Function to find the majority elements in the array
    def findMajority(self, arr):
        #Your Code goes here.
        n=len(arr)
        if n==0:
            return []
        c1, c2=None, None
        f1, f2=0, 0
        for num in arr:
            if c1==num:
                f1+=1
            elif c2==num:
                f2+=1
            elif f1==0:
                c1, f1=num, 1
            elif f2==0:
                c2, f2=num, 1
            else:
                f1 -= 1
                f2 -= 1
        f1, f2=0, 0
        for num in arr:
            if num==c1:
                f1+=1
            elif num==c2:
                f2+=1
        
        res=[]
        if f1 > n // 3:
            res.append(c1)
        if f2 > n // 3:
            res.append(c2)
        
        return sorted(res)
