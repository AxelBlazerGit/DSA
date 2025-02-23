class Solution:
    def ngl(self,arr):
        res=[i+1 for i in range(len(arr))]
        stk=[]
        for i in range(len(arr)):
            while stk and stk[-1][0]<=arr[i]:
                stk.pop()
            if stk and stk[-1][0]>arr[i]:
                res[i]-=stk[-1][1]
            stk.append((arr[i],i+1))
        return res
    def calculateSpan(self, arr):
        #write code here
        return self.ngl(arr)
        # res = [0]*len(arr)
        # stk = []
        
        # for i,price in enumerate(arr):
        #     while stk and stk[-1][0]<=price:
        #         stk.pop()
            
        #     res[i]=i-stk[-1][1] if stk else i+1
        #     stk.append((price,i))
        
        # return res
