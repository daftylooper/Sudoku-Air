import cv2 as cv
import numpy as np
import utils
import handtracker
import startscreen
import sudoku_solver
import random

winx = 650
winy = 1200
frame = np.zeros((winx, winy, 3), dtype='uint8')
keypad=[]
sudokuGrid = np.zeros((9, 9), dtype=int)
tracker = handtracker.handTracking()
solver = sudoku_solver.solver()
pickler = utils.pickler(sudokuGrid)
pickler.unpickle() #Load all the levels
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
    reset=utils.Button(frame, [5,285], "RESET", [200,70])
    solve=utils.Button(frame, [5,375], "SOLVE", [200,70])
    newpuzzle=utils.Button(frame, [5,465], "NEW", [200,70])

    k=1
    for x in range(0, 3):
      for y in range(0, 3):
        keypad.append(utils.Button(frame, [70*y+5, 70*x+5], str(k)))
        k+=1

    #DRAW THE BUTTONS AND GRID
    for key in keypad:
      key.draw()
      #key.highlightButton()

    reset.draw()
    solve.draw()
    newpuzzle.draw()

    utils.Grid.drawGrid(frame, 600, 600, 596, 23)

    if(reset.withinButton(cor, state)):
      sudokuGrid = np.zeros((9, 9))
    if(solve.withinButton(cor, state)):
      solver.solve(sudokuGrid)
      solutions = solver.solutions()
      solver = solutions[0]
    if(newpuzzle.withinButton(cor, state)):
      #Unpickle puzzle'th puzzle in stored sudoku's
      unpickledpuzzles = pickler.unpickle()
      puzzle = random.randint(0, len(unpickledpuzzles)-1) #Put of a limit from 0-n, where there are n-1 grids pickled and stored
      sudokuGrid = unpickledpuzzles[puzzle]

    #cv.imshow("Sudoku Air", cv.bitwise_or(videoFeed, frame)
    
  cv.imshow("Sudoku Air", frame)

  if cv.waitKey(20) & 0xFF==ord('d'):
    tracker.stopRender()
    break
