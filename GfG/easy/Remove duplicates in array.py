class Solution:
    def removeDuplicates(self, arr):
        # code here 
        hash=[False]*101
        uniques=[]
        for i in arr:
            if not hash[i]:
                uniques.append(i)
                hash[i]=True
        return uniques
