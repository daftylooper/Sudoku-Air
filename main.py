import cv2 as cv    
import numpy as np
import pygame
import tkinter  
import mathplotlib

class Button():
  def __init__():
    pass
  def isClicked():
    pass
    
def drawGrid():

    blank =np.zeros((900,900),dtype='uint8')
    cv.imshow('Blank',blank)
    cv.rectangle(blank, (0,0), (900,900), (255,255,255), thickness=4)
    cv.imshow('Rectangle',blank)
    for i in range(1,3):
        cv.rectangle(blank, (0,0), (i*300,900), (255,255,255), thickness=3)
        cv.imshow('Rectangle',blank)
    for i in range(1,3):
        cv.rectangle(blank, (0,0), (900,i*300), (255,255,255), thickness=3)
        cv.imshow('Rectangle',blank)
    for j in range(0,3):
        for i in range(1,3):
            cv.rectangle(blank, (0,0+300*j), (i*100,300), (255,255,255), thickness=2)
            cv.imshow('Rectangle',blank) 
        for i in range(1,3):
            cv.rectangle(blank, (0,0+300*j), (300,i*100), (255,255,255), thickness=2)
            cv.imshow('Rectangle',blank)
    for j in range(0,3):
        for i in range(4,6):
            cv.rectangle(blank, (300+300*j,0), (i*100,600), (255,255,255), thickness=2)
            cv.imshow('Rectangle',blank) 
        for i in range(4,6):
            cv.rectangle(blank, (300+300*j,0), (600,i*100), (255,255,255), thickness=2)
            cv.imshow('Rectangle',blank)
    for j in range(0,3):
        for i in range(7,9):
            cv.rectangle(blank, (600+300*j,0), (i*100,900), (255,255,255), thickness=2)
            cv.imshow('Rectangle',blank) 
        for i in range(7,9):
            cv.rectangle(blank, (600+300*j,0), (900,i*100), (255,255,255), thickness=2)
            cv.imshow('Rectangle',blank)
    
    cv.waitKey(0)


keypad = []
run = True

while run:
  #DRAW
  #CHECK USER INPUT
  #CHANGE VARIOUS STATES
