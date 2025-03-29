#User function Template for python3

class Solution:
    def getMinDiff(self, arr,k):
        # code here
        n=len(arr)
        arr.sort()
        result = arr[-1] - arr[0]
        small = arr[0] + k
        large = arr[-1] - k
        for i in range(n - 1):
            minh = min(small, arr[i + 1] - k)
            if minh < 0:  continue
            maxh = max(large, arr[i] + k)
            result = min(result, maxh - minh)

        return result
