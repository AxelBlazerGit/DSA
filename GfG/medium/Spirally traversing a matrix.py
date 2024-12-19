class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        # code here
        n, m = len(mat), len(mat[0])
        top, bot, rt, lt = 0, n - 1, m - 1, 0
        total = 0
        result = []
    
        while total < n * m:
            for j in range(lt, rt + 1):
                if total < n * m:
                    result.append(mat[top][j])
                    total += 1
            top += 1
    
            for i in range(top, bot + 1):
                if total < n * m:
                    result.append(mat[i][rt])
                    total += 1
            rt -= 1
            
            for j in range(rt, lt - 1, -1):
                if total < n * m:
                    result.append(mat[bot][j])
                    total += 1
            bot -= 1
    
            for i in range(bot, top - 1, -1):
                if total < n * m:
                    result.append(mat[i][lt])
                    total += 1
            lt += 1
    
        return result
