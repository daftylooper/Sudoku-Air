import cv2 as cv
import numpy as np

class Button():
    def  __init__(self, root, pos, text, size=[70,70]):
        self.root = root
        self.pos = pos
        self.size = size
        self.text = text
        self.highlight = False
    
    def draw(self):
        x,y= self.pos
        w,h= self.size
        if(self.highlight):
            cv.rectangle(self.root, self.pos, (x+w, y+h), (255,0,0), -1)
            cv.rectangle(self.root, self.pos, (x+w, y+h), (255,255,255), -1)
            cv.putText(self.root, self.text, (x+20, y+50), cv.FONT_HERSHEY_PLAIN, 3, (255,255,255), 4)
        else:
            cv.rectangle(self.root, self.pos, (x+w, y+h), (255,255,255), 2)
            cv.putText(self.root, self.text, (x+20, y+50), cv.FONT_HERSHEY_PLAIN, 3, (255,255,255), 4)
        
    def withinButton(self, cor, clicked):
        if(clicked):
            if((cor[0]>=self.pos[0] and cor[0]<=self.pos[0]+self.size[0]) and (cor[1]>=self.pos[1] and cor[1]<=self.pos[1]+self.size[1])):
                return True
            return False

    def highlightButton(self):
        self.highlight = True

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
