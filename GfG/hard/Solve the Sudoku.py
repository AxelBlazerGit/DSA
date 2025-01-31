#User function Template for python3

class Solution:
    
    #Function to find a solved Sudoku. 
    def solveSudoku(self, mat):
        
        # Your code here
        self.solved = False
        empty = [[0] * 9 for _ in range(9)]
        row = [[0] * 10 for _ in range(9)]
        column = [[0] * 10 for _ in range(9)]
        square = [[0] * 10 for _ in range(9)]

        def calculate_grid(i, j):
            return (i // 3) * 3 + (j // 3)

        def checkGrid():
            for i in range(9):
                for j in range(1, 10):
                    if row[i][j] != 1:
                        return False
            for i in range(9):
                for j in range(1, 10):
                    if column[i][j] != 1:
                        return False
            for i in range(9):
                for j in range(1, 10):
                    if square[i][j] != 1:
                        return False
            return True

        def fillGrid(i, j):
            if i == 9:
                if checkGrid():
                    self.solved = True
                return
            
            if empty[i][j]:
                for k in range(1, 10):
                    if row[i][k] or column[j][k] or square[calculate_grid(i, j)][k]:
                        continue

                    mat[i][j] = k
                    row[i][k] = column[j][k] = square[calculate_grid(i, j)][k] = 1
                    
                    if j == 8:
                        fillGrid(i + 1, 0)
                    else:
                        fillGrid(i, j + 1)

                    if self.solved:
                        return

                    row[i][k] = column[j][k] = square[calculate_grid(i, j)][k] = 0
                    mat[i][j] = 0
            else:
                if j == 8:
                    fillGrid(i + 1, 0)
                else:
                    fillGrid(i, j + 1)

        for i in range(9):
            for j in range(9):
                if mat[i][j] == 0:
                    empty[i][j] = 1
                else:
                    row[i][mat[i][j]] = 1
                    column[j][mat[i][j]] = 1
                    square[calculate_grid(i, j)][mat[i][j]] = 1

        fillGrid(0, 0)
