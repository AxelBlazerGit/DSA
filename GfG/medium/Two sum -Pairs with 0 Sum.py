#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        zero_count = arr.count(0)
        arr = sorted(set(arr))
        pairs = []
        arr_set = set(arr)
        for num in arr:
            if num > 0:
                break
            if -num in arr_set and num != 0:
                pairs.append([num, -num])
        if zero_count >= 2:
            pairs.append([0, 0])
        
        return pairs
