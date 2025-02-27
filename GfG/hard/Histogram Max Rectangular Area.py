class Solution:
    def getMaxArea(self,arr):
        #code here
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
        area=-1
        for i,h in enumerate(arr):
            area=max(area,h*(r[i]-l[i]-1))
        return area
        
