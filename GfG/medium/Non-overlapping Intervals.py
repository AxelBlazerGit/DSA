#User function Template for python3

class Solution:
    def minRemoval(self, intervals):
        # Code here
        intervals.sort(key=lambda x: x[1])
        remove = prev = 0

        for start, end in intervals:
            if start < prev:
                remove += 1
            else:
                prev = end
        
        return remove
