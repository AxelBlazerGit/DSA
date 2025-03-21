#User function Template for python3
class Solution:
    def getSecondLargest(self, arr):
        # Code Here
        largest=slargest=-1
        for i in arr:
            if i>largest:
                slargest=largest
                largest=i
            if i>slargest and i!=largest:
                slargest=i
        return slargest
