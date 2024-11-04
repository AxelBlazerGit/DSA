#User function Template for python3

def rotate(matrix): 
    #code here
    n=len(matrix)
    for i in range(n):
        for j in range(i+1,n):
            matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
    for i in range(n):
        matrix[i].reverse()
    return matrix
# 1 2 3
# 4 5 6
# 7 8 9
# reverse
# 3 2 1
# 6 5 4
# 9 8 7
# i j = j i
# 7 4 1
# 8 5 2
# 9 6 3
