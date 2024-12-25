#User function Template for python3
class Solution:
    def setMatrixZeroes(self, mat):
        # use first colm n first row as flags for elements
        # arr[0][0] is to be handled separately
        # traverse from row1,col1 to end checking if either flags are True
        # check first row in reverse
        # check first column in reverse
        
        colFlag=False
        n=len(mat)
        m=len(mat[0])
        for i in range(n):
            if mat[i][0] == 0:
                colFlag = True
            for j in range(1, m):
                if mat[i][j] == 0:
                    mat[i][0] = 0
                    mat[0][j] = 0
        for i in range(1,n):
            for j in range(1,m):
                if mat[i][0] == 0 or mat[0][j] == 0:
                    mat[i][j] = 0
        if mat[0][0] == 0:
            for i in range(m):
                mat[0][i]=0
        if colFlag:
            for i in range(n):
                mat[i][0]=0
        return mat
