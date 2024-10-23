#User function Template for python3

class Solution:
    def shift(self, arr):
        z = nz = 0
        while z < len(arr):
            if arr[z]:  # If arr[z] is non-zero
                arr[nz], arr[z] = arr[z], arr[nz]
                nz += 1
            z += 1
        return arr
    def modifyAndRearrangeArr (self, arr) : 
        #Complete the function
        for i in range(len(arr)-1):
            if arr[i]==arr[i+1] and arr[i]:
                arr[i]*=2
                arr[i+1]=0
        return self.shift(arr)
