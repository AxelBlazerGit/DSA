from typing import List

class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        ans = 0
        hold = prices[0]
        i = 1
        n = len(prices)
        
        if n == 1:
            return 0
        elif n == 2:
            return 0 if prices[0] >= prices[1] else prices[1] - prices[0]
        
        while i < n:
            while i < n and prices[i] > prices[i - 1]:
                i += 1
            ans += prices[i - 1] - hold
            while i < n and prices[i] <= prices[i - 1]:
                i += 1
            hold = prices[i - 1]
        
        return ans
