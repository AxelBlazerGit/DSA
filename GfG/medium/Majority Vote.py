class Solution:
    # variant of moore voting
    def findMajority(self, nums):
        ele1, ele2 = None, None
        vote1, vote2 = 0, 0
        for num in nums:
            if ele1 == num:
                vote1 += 1
            elif ele2 == num:
                vote2 += 1
            elif vote1 == 0:
                ele1, vote1 = num, 1
            elif vote2 == 0:
                ele2, vote2 = num, 1
            else:
                vote1 -= 1
                vote2 -= 1
        vote1, vote2 = 0, 0
        for num in nums:
            if num == ele1:
                vote1 += 1
            elif num == ele2:
                vote2 += 1
        result = []
        n = len(nums)
        if vote1 > n // 3:
            result.append(ele1)
        if vote2 > n // 3:
            result.append(ele2)
        return result if result else [-1]
