import cv2 as cv
import numpy as np
import utils
import handtracker
import startscreen
import sudoku_solver

winx = 650
winy = 1200
frame = np.zeros((winx, winy, 3), dtype='uint8')
keypad=[]
tracker = handtracker.handTracking()
solver = sudoku_solver.solver()
current = 0
run = True
startScreen = True
mainScreen = False

while run:
  tracker.getCapture(winy, winx)
  tracker.drawLandmark()
  cor, state = tracker.ifClicked()
  frame = tracker.returnProcessedVideoFeed()
  #utils.Grid.drawGrid(frame, 600, 600, 0, 0)

  if(startScreen):
    frame, startbutton = startscreen.drawStartScreen(frame, 17, 17)
    if(startbutton.withinButton(cor, state)):
      startScreen = False
      mainScreen = True

  if(mainScreen):
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

    utils.Grid.drawGrid(frame, 600, 600, 596, 23)

    #cv.imshow("Sudoku Air", cv.bitwise_or(videoFeed, frame)
    
  cv.imshow("Sudoku Air", frame)

  if cv.waitKey(20) & 0xFF==ord('d'):
    tracker.stopRender()
    break
