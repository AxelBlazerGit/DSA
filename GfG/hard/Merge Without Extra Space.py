class Solution:
    def mergeArrays(self, a, b):
        # code here
        i=len(a)-1
        j=0
        while i!=-1 and j<len(b):
            if a[i]<=b[j]:  break
            a[i],b[j]=b[j],a[i]
            i-=1
            j+=1
        a.sort()
        b.sort()
        return a,b
