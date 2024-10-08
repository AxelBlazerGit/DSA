from typing import List


class Solution:
    def pairsum(self, arr : List[int]) -> int:
        # code here
        mx=smx=-1
        for i in arr:
            if i>mx:
                smx=mx
                mx=i
            elif i>smx:
                smx=i
        return smx+mx
