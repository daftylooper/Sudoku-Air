import cv2 as cv    
import numpy as np
import pygame
import tkinter  
import mathplotlib

class Button():
  def draw():

  def isClicked():
   
    
def drawGrid():

    blank =np.zeros((1920,1920),dtype='uint8')
    cv.rectangle(blank, (0,0), (900,900), (255,255,255), thickness=4)
    cv.rectangle(blank, (1000,0), (1300,300), (255,255,255), thickness=4)
    for i in range(1,3):
        cv.rectangle(blank, (0,0), (i*300,900), (255,255,255), thickness=3)
        cv.rectangle(blank, (0,0), (900,i*300), (255,255,255), thickness=3)
        cv.line(blank, (1000,100*i), (1300,100*i), (255,255,255), thickness=2)
    for i in range(1,9): 
        cv.line(blank, (i*100,0), (i*100,900), (255,255,255), thickness=1)
        cv.line(blank, (0,i*100), (900,i*100), (255,255,255), thickness=1)
    for i in range(11,13):
        cv.line(blank, (100*i,0), (100*i,300), (255,255,255), thickness=2)
    cv.imshow('Line', blank)
    cv.waitKey(0)

keypad = []
run = True

while run:
    drawGrid()

    if cv.waitKey(20) & 0xFF==ord('d'):
        break
