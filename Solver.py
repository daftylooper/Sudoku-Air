import numpy as np

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

class solver(object):
    def possible(self, row, column, number):#Checks if the number can be palce at the particular position
        global grid
        for i in range(0,9):
            if grid[row][i] == number:
                return False

        for i in range(0,9):
            if grid[i][column] == number:
                return False
        
        x0 = (column // 3) * 3
        y0 = (row // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if grid[y0+i][x0+j] == number:
                    return False
        if True:
            print()
        return True

    def solve(self):#Solves the sudoku
        global grid
        for row in range(0,9):
            for column in range(0,9):
                if grid[row][column] == 0:
                    for number in range(1,10):
                        if self.possible(row, column, number):
                            grid[row][column] = number
                            solver.solve(self)
                            grid[row][column] = 0
                    return
        
        print(np.matrix(grid))
        input('More possible solutions')

s=solver()
s.solve()
