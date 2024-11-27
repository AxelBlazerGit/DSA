#User function template for Python
class Solution:
    def myAtoi(self, s):
        # Code here
        limit=2**31-1
        flag=False
        s=s.strip()
        i=0
        ans=0
        if s[0]=='-':
            flag=True
            i=1
        elif s[0]=='+':
            i=1
        if i==len(s):   return 0
        while i<len(s):
            if s[i].isdigit():
                ans=ans*10+int(s[i])
            else:
                break
            i+=1
        if ans>limit or ans<-(limit+1): return -(limit+1) if flag else limit
        return -ans if flag else ans
