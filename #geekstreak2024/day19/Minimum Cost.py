#User function Template for python3
class Solution:
    def minimizeCost(self, k, arr):
        # code here
        n=len(arr)
        cost=[float("inf")]*n
        cost[0]=0
        for i in range(1,n):
            for j in range(max(0,i-k),i):
                cost[i]=min(cost[i],cost[j]+abs(arr[i]-arr[j]))
        return cost[-1]
