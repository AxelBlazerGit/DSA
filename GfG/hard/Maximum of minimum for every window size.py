class Solution:
    def maxOfMins(self, arr):
       # code here
        def nsr(arr):
            res=[len(arr)]*len(arr)
            stk=[]
            for i in reversed(range(len(arr))):
                while stk and arr[stk[-1]]>=arr[i]:
                    stk.pop()
                if stk:
                    res[i]=stk[-1]
                stk.append(i)
            return res
            
        def nsl(arr):
            res=[-1]*len(arr)
            stk=[]
            for i in range(len(arr)):
                while stk and arr[stk[-1]]>=arr[i]:
                    stk.pop()
                if stk:
                    res[i]=stk[-1]
                stk.append(i)
            return res
            
        l,r=nsl(arr),nsr(arr)
        res=[0]*(len(arr)+1)
        for i in range(len(arr)):
            span=r[i]-l[i]-1
            res[span]=max(res[span],arr[i])
        for i in range(len(res)-2,0,-1):
            res[i]=max(res[i],res[i+1])
        return res[1:]
