#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        arr=sorted(arr)
        ans=arr[-1]-arr[0]
        if not ans:
            return ans
        for i in range(len(arr)-1):
                temp0=min(arr[0]+k,arr[i+1]-k)
                temp1=max(arr[-1]-k,arr[i]+k)
                if temp0>=0:
                    ans=min(ans,temp1-temp0)
        return ans
        
                
# 1 1 4 6 6 8 9 10
# 8 8 11 13 13 1 2 3
# 1 2 3 8 8 11 13 13
# piv=5

# piv=x            
# a b c piv x y z
# smallest => a,x
# largest=> c,z
