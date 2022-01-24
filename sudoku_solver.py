import numpy as np
import pickle

class solver():
    def __init__(self):
        self.solutions = []
        self.grid = []

    def possible(self, row, column, number):
        #Is the number appearing in the given row?
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

    def solve(self):
        for row in range(0,9):
            for column in range(0,9):
                if self.grid[row][column] == 0:
                    for number in range(1,10):
                        if self.possible(row, column, number): 
                            self.grid[row][column] = number
                            self.solve()
                            self.grid[row][column] = 0
   
                    return

        self.solutions.append([row.copy() for row in self.grid])

'''
solvo = solver(grid)
solvo.solve()
print(np.matrix(sol[0]))
'''
