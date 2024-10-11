class Solution:
    def rearrange(self, arr):
        #Code here
        hash={}
        for i in arr:
            hash[i]=0
        for idx,ele in enumerate(arr):
            if idx in hash:
                arr[idx]=idx
            else:
                arr[idx]=-1
        return arr
