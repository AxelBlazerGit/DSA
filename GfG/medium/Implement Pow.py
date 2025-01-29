#User function Template for python3
class Solution:
    def power(self, b: float, e: int) -> float:
        # Code Here
        if e < 0:
            b = 1 / b
            e = -e
        result = 1.0  
        base = b
        
        while e > 0:
            if e % 2 == 1:
                result *= base
            base *= base
            e //= 2
        
        return result
