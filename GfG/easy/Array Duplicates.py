from typing import List


class Solution:
    def duplicates(self, n : int, arr : List[int]) -> List[int]:
        # code here
        dupes=set()
        ans=set()
        for i in arr:
            if i not in dupes:
                dupes.add(i)
            else:
                ans.add(i)
        if not ans:
            return [-1]
        return sorted(list(ans))
