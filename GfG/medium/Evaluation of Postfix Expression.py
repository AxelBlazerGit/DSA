class Solution:
    def evaluate(self, arr):
        # code here
        stk=[]
        for i in arr:
            if i in '+-*/':
                a,b=stk.pop(),stk.pop()
                if i=='+':
                    stk.append(a+b)
                elif i=='-':
                    stk.append(b-a)
                elif i=='*':
                    stk.append(a*b)
                else:
                    stk.append(int(b/a))
                    
            else:
                stk.append(int(i))
        return stk[0]
