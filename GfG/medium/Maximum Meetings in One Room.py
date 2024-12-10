from typing import List


class Solution:
    def maxMeetings(self, N : int, S : List[int], F : List[int]) -> List[int]:
        # code here
        meets = [(S[i], F[i], i + 1) for i in range(N)]

        meets.sort(key=lambda x: (x[1], x[2]))
        
        attend = []
        finish = 0
        
        for s, f, idx in meets:
            if s > finish:
                attend.append(idx)
                finish = f
        
        return sorted(attend)
