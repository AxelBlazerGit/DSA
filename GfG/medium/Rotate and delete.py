# from typing import List


class Solution:
    def rotateDelete(self,  arr):
        # code here
        cur=1
        n=len(arr)
        while cur<n//2+1:
            temp=arr.pop()
            arr.insert(0, temp)
            arr.pop(-cur)
            cur += 1
        return arr[0]
