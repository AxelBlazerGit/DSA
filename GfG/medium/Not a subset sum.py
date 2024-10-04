#User function Template for python3

class Solution:
    def findSmallest(self, arr):
        # code here
        if arr[0]>1:
            return 1
        temp=1
        for i in arr:
            if temp<i:
                return temp
            temp+=i
        return temp
