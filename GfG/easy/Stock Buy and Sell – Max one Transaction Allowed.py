class Solution:
    def maximumProfit(self, prices):
        # code here
        if not prices:  return 0
        buy=float('inf')
        ans=0
        for i in prices:
            if i<buy:
                buy=i
            elif i-buy>ans:
                ans=i-buy
        return ans
