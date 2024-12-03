class Solution:
    def minChar(self, s):
        #Write your code here
        s=s+'.'+s[::-1]
        n=len(s)
        lps=[0]*n
        for i in range(1, n):
            j = lps[i - 1]
            while j > 0 and s[i] != s[j]:
                j = lps[j - 1]
            if s[i] == s[j]:
                j += 1
            lps[i] = j
        return len(s)//2 - lps[-1]
