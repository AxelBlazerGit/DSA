class Solution:
    def minOperation(self, arr):
        #code here
        r,c=[0]*len(arr),[0]*len(arr)
        ops=199
        for i in range(len(arr)):
            for j in range(len(arr)):
                if not arr[i][j]:
                    r[i]+=1
                    c[j]+=1
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i][j]:
                    ops=min(ops,r[i]+c[j])
                else:
                    ops=min(ops,r[i]+c[j]-1)
        return ops
