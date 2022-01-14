import cv2 as cv
import numpy as np
import utils
import handtracker

winx = 650
winy = 1200
frame = np.zeros((winx, winy, 3), dtype='uint8')
run = True
keypad=[]
tracker = handtracker.handTracking()

# DEFINE ALL THE BUTTONS
myreset=utils.Button(frame, [5,285], "RESET", [200,70])
mysolve=utils.Button(frame, [5,375], "SOLVE", [200,70])
myquit=utils.Button(frame, [5,465], "QUIT", [200,70])

k=1
for x in range(0, 3):
  for y in range(0, 3):
    keypad.append(utils.Button(frame, [70*y+5, 70*x+5], str(k)))
    k+=1

#DRAW THE BUTTONS AND GRID
for key in keypad:
  key.draw()

myreset.draw()
mysolve.draw()
myquit.draw()

utils.Grid.drawGrid(frame, 600, 600)

while run:
  tracker.getCapture(winy, winx)
  videoFeed = tracker.returnProcessedVideoFeed()
  cv.imshow("Sudoku Air", cv.bitwise_or(videoFeed, frame))

  if cv.waitKey(20) & 0xFF==ord('d'):
    tracker.stopRender()
    break
