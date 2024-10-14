#User function Template for python3



class Solution:
    def find3Numbers(self, arr):
        # Code Here
        n = len(arr)
        if n < 3:
            return []
        minL = [0] * n
        maxR = [0] * n
        minL[0] = arr[0]
        for i in range(1, n):
            minL[i] = min(minL[i - 1], arr[i])
        maxR[n - 1] = arr[n - 1]
        for i in range(n - 2, -1, -1):
            maxR[i] = max(maxR[i + 1], arr[i])
        for i in range(1, n - 1):
            l = minL[i - 1]
            m = maxR[i + 1]
            if l < arr[i] < m:
                return [l,arr[i],m]
        return []
