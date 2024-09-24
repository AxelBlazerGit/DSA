#User function Template for python3

class Solution:
    
    #Function to find the smallest window in the string s consisting
    #of all the characters of string p.
    def smallestWindow(self, s, p):
        #code here
        if len(p) > len(s):
            return "-1"
        strr = [0] * 26
        check = [0] * 26
        c, curr, j, start, end, length = 0, 0, 0, -1, -1, float('inf')
        for char in p:
            check[ord(char) - ord('a')] += 1
            if check[ord(char) - ord('a')] == 1:
                c += 1
        for i in range(len(s)):
            char = s[i]
            strr[ord(char) - ord('a')] += 1
            if strr[ord(char) - ord('a')] == check[ord(char) - ord('a')]:
                curr += 1
            while strr[ord(s[j]) - ord('a')] > check[ord(s[j]) - ord('a')]:
                strr[ord(s[j]) - ord('a')] -= 1
                j += 1
            if curr == c:
                if length > i - j + 1:
                    start = j
                    end = i
                    length = i - j + 1
        return s[start:end + 1] if start != -1 else "-1"
