import cv2 as cv
import numpy as np
import utils

def drawStartScreen(frame, kx, ky):
    #Don't bother about the sizes, just take a frame(only video capture) as input and spit the start screen out
    xcenter = frame.shape[1]//2
    ycenter = frame.shape[0]//2
    gaussian = cv.GaussianBlur(frame, (kx, ky), 0)
    cv.putText(gaussian, "SUDOKU AIR", (xcenter-300, 100), cv.FONT_HERSHEY_TRIPLEX, 3, (255, 255, 255), 3)
    startButton = utils.Button(gaussian, [xcenter-100, ycenter-37], "START!", [200, 75])
    cv.putText(gaussian, "Created By - ", (xcenter-100, ycenter+100), cv.FONT_HERSHEY_PLAIN, 1.35, (255, 255, 255), 2)
    cv.putText(gaussian, "Prajwal Shenoy", (xcenter, ycenter+120), cv.FONT_HERSHEY_PLAIN, 1.25, (255, 255, 255), 1)
    cv.putText(gaussian, "Prerana", (xcenter, ycenter+140), cv.FONT_HERSHEY_PLAIN, 1.25, (255, 255, 255), 1)
    cv.putText(gaussian, "Pranav Ajay Desai", (xcenter, ycenter+160), cv.FONT_HERSHEY_PLAIN, 1.25, (255, 255, 255), 1)
    startButton.draw()
    #cv.imshow("Start Screen", gaussian)
    return gaussian, startButton
'''
frame = cv.imread("cats.jpg")
drawStartScreen(frame, 17, 17)
cv.waitKey(0)
'''