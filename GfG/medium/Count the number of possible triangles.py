#User function Template for python3

class Solution:
    #Function to count the number of possible triangles.
    def countTriangles(self, arr):
        # code here
        arr.sort()
        triangles=0
        for i in range(len(arr)-1,1,-1):
            j=0
            k=i-1
            while j<k:
                if arr[j]+arr[k]>arr[i]:
                    triangles+=k
                    triangles-=j
                    k-=1
                else:
                    j+=1
        return triangles
