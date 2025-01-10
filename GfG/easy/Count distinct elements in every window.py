from collections import defaultdict
class Solution:
    def countDistinct(self, arr, k):
        # Code here
        slide=defaultdict(int)
        distincts=[]
        for i in range(k):
            slide[arr[i]]+=1
        distincts.append(len(slide))
        for i in range(k,len(arr)):
            slide[arr[i]]+=1
            slide[arr[i-k]]-=1
            if not slide[arr[i-k]]:
                del slide[arr[i-k]]
            distincts.append(len(slide))
        return distincts
