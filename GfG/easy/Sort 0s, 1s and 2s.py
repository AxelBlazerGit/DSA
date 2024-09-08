class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        # code here
        z, o, t = 0, 0, len(arr) - 1
        
        while o <= t:
            if arr[o] == 0:
                arr[z], arr[o] = arr[o], arr[z]
                z += 1
                o += 1
            elif arr[o] == 1:
                o += 1
            else:
                arr[o], arr[t] = arr[t], arr[o]
                t -= 1
        
        return arr
