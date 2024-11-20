from typing import List

class Solution:
    def maximumProfit(self, prices) -> int:
        # code here
        """
        Traverse array to find peaks(sell) and valleys(buy):
          1. Find next peak where prices stop increasing; calculate profit.
          2. Find next valley where prices stop decreasing; set new buy price.
        """
        ans = 0
        hold = prices[0]
        i = 1
        n = len(prices)
        
        if n == 1:
            return 0
        elif n == 2:
            return 0 if prices[0] >= prices[1] else prices[1] - prices[0]
        
        while i < n:
            # Find a peak (sell opportunity)
            while i < n and prices[i] > prices[i - 1]:
                i += 1
            ans += prices[i - 1] - hold
            # Find a valley (buy opportunity)
            while i < n and prices[i] <= prices[i - 1]:
                i += 1
            hold = prices[i - 1]
        
        return ans
