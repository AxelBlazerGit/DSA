#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, s):
        # code here
        n = len(s)
        idx = [-1] * 26
        st = lus = 0

        for e in range(n):
            temp = ord(s[e]) - 97
            if idx[temp] >= st:
                st = idx[temp] + 1
            idx[temp] = e
            lus = max(lus, e - st + 1)

        return lus
