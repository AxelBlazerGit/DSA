#User function Template for python3

class Solution:
    def pivot(self,arr):
        n = len(arr)
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) // 2
            
            if arr[mid] < arr[right]:
                right = mid
            else:
                left = mid + 1
        
        return left
    
    def binS(self,s,e,arr,key):
        while s <= e:
            m = (s + e) // 2
            if arr[m] == key:
                return m
            elif arr[m] < key:
                s = m + 1
            else:
                e = m - 1
        return -1
            
    
    def search(self,arr,key):
        # Complete this function
        piv = self.pivot(arr)
        
        check = self.binS(piv, len(arr) - 1, arr, key)
        
        if check == -1:
            check = self.binS(0, piv - 1, arr, key)
            
        return check
