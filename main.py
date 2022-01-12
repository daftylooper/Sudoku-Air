import cv2 as cv    
import numpy as np
import pygame
import tkinter  
import mathplotlib

class Button():
  def __init__(self, pos, text, size=[70,70], w, h, x, y):
    self.pos = pos
    self.size = size
    self.text = text
    self.x=x
    self.y=y
    self.h=h
    self.w=w
  
  def draw(self, root):
        cv.rectangle(root, self.pos, (self.x+self.w, self.y+self.h), (255,255,255),2)
        cv.putText(root, self.text, (self.x+20, self.y+50), cv.FONT_HERSHEY_PLAIN, 3, (255,255,255), 4)
        return root
      
  def isClicked(self,xcor,ycor):
    if((xcor>=self.x and xcor<=self.x+self.w) and (ycor>=self.y and ycor<=self.y+self.h)):
            return True
        return False
    
def drawGrid():

    blank =np.zeros((1920,1080),dtype='uint8')
    #cv.imshow('Blank',blank)
    cv.rectangle(blank, (0,0), (900,900), (255,255,255), thickness=4)
    #cv.imshow('Rectangle',blank)
    for i in range(1,3):
        cv.rectangle(blank, (0,0), (i*300,900), (255,255,255), thickness=3)
        #cv.imshow('Rectangle',blank)
    for i in range(1,3):
        cv.rectangle(blank, (0,0), (900,i*300), (255,255,255), thickness=3)
        #cv.imshow('Rectangle',blank)
    for i in range(1,9): 
        cv.line(blank, (i*100,0), (i*100,900), (255,255,255), thickness=2)
        #cv.imshow('Line',blank)
    for i in range(1,9):
        cv.line(blank, (0,i*100), (900,i*100), (255,255,255), thickness=2)
        #cv.imshow('Line',blank)
    cv.imshow('Line',blank)
    cv.waitKey(0)

keypad = []
run = True

while run:
    drawGrid()

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
