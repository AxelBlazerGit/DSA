#User function Template for python3

class Solution:
    def pivotDupe(self,arr):
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] < arr[right]:
                right = mid
            elif arr[mid] > arr[right]:
                left = mid + 1
            else:
                right -= 1
    
        return left
    
    def findMin(self, arr):
        #complete the function here
        return arr[self.pivotDupe(arr)]
