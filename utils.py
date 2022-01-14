import cv2 as cv
import numpy as np

class Button():
    def  __init__(self, root, pos, text, size=[70,70]):
        self.root = root
        self.pos = pos
        self.size = size
        self.text = text
    
    def draw(self):
        x,y= self.pos
        w,h= self.size 
        cv.rectangle(self.root, self.pos, (x+w, y+h), (255,255,255),2)
        cv.putText(self.root, self.text, (x+20, y+50), cv.FONT_HERSHEY_PLAIN, 3, (255,255,255), 4)
        
    def withinButton(self, xcor, ycor):
        if((xcor>=self.pos.x and xcor<=self.pos.x+self.size.w) and (ycor>=self.pos.y and ycor<=self.pos.y+self.size.h)):
            return True
        return False

class Grid():    
    def drawGrid(blank, x, y):
        cv.rectangle(blank, (0,0), (x, y), (255,255,255), thickness=4)
        for i in range(1,3):
            cv.rectangle(blank, (0,0), (i*int(x/3), y), (255,255,255), thickness=3)
        for i in range(1,3):
            cv.rectangle(blank, (0,0), (x, i*int(y/3)), (255,255,255), thickness=3)
        for i in range(1,9):
            cv.line(blank, (i*int(x/9),0), (i*int(x/9), y), (255,255,255), thickness=2)
        for i in range(1,9):
            cv.line(blank, (0,i*int(y/9)), (x, i*int(y/9)), (255,255,255), thickness=2)
