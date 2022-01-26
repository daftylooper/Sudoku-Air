import cv2 as cv
import numpy as np
import pickle
import os

class Button():
    def  __init__(self, root, pos, text, size=[70,70], highlight=False):
        self.root = root
        self.pos = pos
        self.size = size
        self.text = text
        self.highlight = highlight
    
    def draw(self):
        x,y = self.pos
        w,h = self.size
        if(self.highlight):
            cv.rectangle(self.root, self.pos, (x+w, y+h), (255, 255, 255), -1)
            cv.putText(self.root, self.text, (x+20, y+50), cv.FONT_HERSHEY_PLAIN, 3, (255, 255, 255), 4)
        else:
            cv.rectangle(self.root, self.pos, (x+w, y+h), (0, 0, 0), 2)
            cv.putText(self.root, self.text, (x+20, y+50), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 4)
        
    def withinButton(self, cor, clicked):
        if(clicked):
            if((cor[0]>=self.pos[0] and cor[0]<=self.pos[0]+self.size[0]) and (cor[1]>=self.pos[1] and cor[1]<=self.pos[1]+self.size[1])):
                return True
            return False

class Grid():    
    def drawGrid(blank, x, y, xshift, yshift): #x, y - width, height <===> xshift, yshift - x, y
        cv.rectangle(blank, (xshift, yshift), (x+xshift, y+yshift), (255,255,255), thickness=4)
        for i in range(1,3):
            cv.line(blank, (xshift+i*int(x/3), yshift), (xshift+i*int(x/3), y+yshift), (255,255,255), thickness=3)#Vertical Line
            cv.line(blank, (xshift, yshift+i*int(y/3)), (x+xshift, yshift+i*int(y/3)), (255,255,255), thickness=3)#Horizontal Line
        for i in range(1,9):
            cv.line(blank, (i*int(x/9)+xshift, yshift), (i*int(x/9)+xshift, y+yshift), (255,255,255), thickness=2)
        for i in range(1,9):
            cv.line(blank, (xshift, i*int(y/9)+yshift), (x+xshift, i*int(y/9)+yshift), (255,255,255), thickness=2)

    def renderElements(frame, grid):
        for i in range(0, 9):
            for j in range(0, 9):
                cv.putText(frame, str(grid[i][j]), (596+22+66*i, 23+50+66*j), cv.FONT_HERSHEY_PLAIN, 3, (0, 0, 0), 4)

class pickler():
    def __init__(self, topickle):
        self.puzzles = topickle
    def pickle(self):
        if(os.path.exists("sudoku_puzzles.txt")):
            os.remove("sudoku_puzzles.txt")
        outfile = open("sudoku_puzzles.txt", 'ab')
        pickle.dump(self.puzzles, outfile)
        outfile.close()
    def unpickle(self):
        if(os.path.exists("sudoku_puzzles.txt")):
            self.pickle()
        outfile = open("sudoku_puzzles", 'rb')
        self.puzzles = pickle.load(outfile)
        outfile.close()
    def addpuzzle(self, sudoku):
        self.unpickle()
        self.puzzles.append(sudoku)
        self.pickle()
    def removepuzzle(self, index):
        self.unpickle()
        self.puzzles.remove(index)
        self.pickle()
