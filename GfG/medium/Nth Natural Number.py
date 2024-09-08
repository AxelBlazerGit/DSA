#User function Template for python3

class Solution:
#compute base9 number for each test case and return..complexity is logarithmic and constant
    def findNth(self,n):
        #code here
        # n=int(bin(n)[2:])
        ans=0
        size=1
        while(n):
            ans+=(n%9)*size
            size*=10
            n//=9
        return ans
        
