# User function Template for Python3

class Solution:
    def maxLength(self, str):
        # code here
        stack=[-1]
        ans=0
        for i in range(len(str)):
            if str[i]=='(':
                stack.append(i)
            else:
                if stack:
                    stack.pop()
                if stack:
                    ans=max(ans,i-stack[-1])
                else:
                    stack.append(i)
        return ans
