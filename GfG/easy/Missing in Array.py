class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, nums):
        
        # code here
        nums=set(nums)
        for i in range(1,len(nums)+2):
            if i not in nums:
                return i
        return 0
