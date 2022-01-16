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
solutions=[]
class solver():
    def __init__(self, someGrid):
        self.grid = someGrid
        self.solutions=[]
    def possible(self, row, column, number):#Checks if the number can be palce at the particular position
        for i in range(0,9):
            if self.grid[row][i] == number:
                return False

        for i in range(0,9):
            if self.grid[i][column] == number:
                return False
        
        x0 = (column // 3) * 3
        y0 = (row // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if self.grid[y0+i][x0+j] == number:
                    return False

        return True
    def solve(self):#Solves the sudoku
        for row in range(0,9):
            for column in range(0,9):
                if self.grid[row][column] == 0:
                    for number in range(1,10):
                        if self.possible(row, column, number):
                            self.grid[row][column] = number
                            solver.solve(self)
                            self.grid[row][column] = 0
                    return
        self.solutions.append(self.grid)
        ind=self.solutions.index(self.grid)
        print(np.matrix(self.solutions[ind]))
        input('Enter')
            

s=solver(grid)
sol=s.solve()
print(sol)
