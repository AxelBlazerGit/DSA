#User function Template for python3
class Solution:
    def checkDuplicatesWithinK(self, arr, k):
        # your code
        hash=set()
        for i in range(len(arr)):
            if arr[i] in hash:  return True
            hash.add(arr[i])
            if i>=k:    hash.remove(arr[i-k])
        return False
