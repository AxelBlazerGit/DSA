
#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchRowMatrix(self, mat, x): 
    	# code here 
    	
        def binS(arr,x):
            s=0
            e=len(arr)-1
            while s<=e:
                m=(s+e)//2
                if arr[m]==x:
                    return 1
                elif arr[m]>x:
                    e=m-1
                else:
                    s=m+1
            return 0
        
        for row in mat:
            if binS(row,x):
                return True
        return False
