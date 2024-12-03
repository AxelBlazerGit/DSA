
#User function Template for python3

class Solution:
    
    #Function to remove common characters and concatenate two strings.
    def concatenatedString(self,s1,s2):
        #code here
        # t='0'
        s1=[[x,1] for x in s1]
        s2=[[x,1] for x in s2]
        hash = set([x[0] for x in s1]) & set([x[0] for x in s2])
        for x in s1:
            if x[0] in hash:
                x[1] = 0
        for x in s2:
            if x[0] in hash:
                x[1] = 0
        final=''.join([x[0] for x in s1 if x[1]] + [x[0] for x in s2 if x[1]])
        return final if final else -1
