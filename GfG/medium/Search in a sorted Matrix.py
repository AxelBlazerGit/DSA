
#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here
    	col=len(mat[0])
    	s=0
    	e=len(mat)*col-1
    	while s<=e:
    	    m=(s+e)//2
    	    mx,my=divmod(m,col)
    	    if mat[mx][my]==x:
    	        return True
    	    elif mat[mx][my]>x:
    	        e=m-1
    	    else:
    	        s=m+1
    	return False
