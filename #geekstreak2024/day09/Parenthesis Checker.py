#User function Template for python3

class Solution:
    
    #Function to check if brackets are balanced or not.
    def ispar(self,s):
        # code here
        if len(s)%2:
            return False
        stk=[]
        for i in s:
            if i in "({[":
                stk.append(i)
            else:
                if i==')':
                    if stk:
                        if stk[-1]=='(':
                            stk.pop()
                        else:
                            return False
                    else:
                        return False
                elif i==']':
                    if stk:
                        if stk[-1]=='[':
                            stk.pop()
                        else:
                            return False
                    else:
                        return False
                elif i=='}':
                    if stk:
                        if stk[-1]=='{':
                            stk.pop()
                        else:
                            return False
                    else:
                        return False
        return True if not stk else False
