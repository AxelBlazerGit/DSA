#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        big=small=-1
        for i in arr:
            if i>big:
                small=big
                big=i
            if i>small and i!=big:
                small=i
        return small
