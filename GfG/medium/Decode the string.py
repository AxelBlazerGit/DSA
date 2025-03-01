
class Solution:
    def decodedString(self, s):
        # code here
        n=len(s)
        stk=[]
        ans=""
        for i in s:
            if i != ']':
                stk.append(i)
            else:
                temp=""
                while stk[-1] != '[':
                    temp=stk.pop()+temp
                stk.pop()
                mul = ""
                while stk and stk[-1].isdigit():
                    mul=stk.pop()+mul
                mul=int(mul)
                stk.append(temp*mul)
        return "".join(stk)
