import numpy as np
import pickle

grid = [[5,3,0,0,7,0,0,0,0],
        [6,0,0,1,9,5,0,0,0],
        [0,9,8,0,0,0,0,6,0],
        [8,0,0,0,6,0,0,0,3],
        [4,0,0,8,0,3,0,0,1],
        [7,0,0,0,2,0,0,0,6],
        [0,6,0,0,0,0,2,8,0],
        [0,0,0,0,1,9,0,0,5],
        [0,0,0,0,0,0,0,0,0]]

class solver():
    def __init__(self, grid):
        self.solutions = []
        self.grid = grid

    def possible(self, grid, row, column, number):
        #Is the number appearing in the given row?
        for i in range(0,9):
            if self.grid[row][i] == number:
                return False

        #Is the number appearing in the given column?
        for i in range(0,9):
            if self.grid[i][column] == number:
                return False
        
        #Is the number appearing in the given square?
        x0 = (column // 3) * 3
        y0 = (row // 3) * 3
        for i in range(0,3):
            for j in range(0,3):
                if self.grid[y0+i][x0+j] == number:
                    return False

        return True

    def solve(self):
        for row in range(0,9):
            for column in range(0,9):
                if self.grid[row][column] == 0:
                    for number in range(1,10):
                        if self.possible(self.grid, row, column, number):
                            self.grid[row][column] = number
                            self.solve()
                            self.grid[row][column] = 0

                    return
    
        self.solutions[self.x] = self.grid
        print(self.solutions.pop(0))
        print("\n-------------------------------------------------------------------------")

solvo = solver(grid)
solvo.solve()
