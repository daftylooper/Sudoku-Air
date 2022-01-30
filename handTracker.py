import cv2 as cv
import time
import mediapipe as mp
import math
import numpy
import os

class handTracking:
    def __init__(self):
        #OS keeps switching the index of cameras, this finds the right one.
        cameraFound = False
        n = 0
        while not(cameraFound) and n<10:
            self.capture = cv.VideoCapture(n)
            time.sleep(0.1)
            isTrue, self.frame = self.capture.read()
            time.sleep(0.1)
            if(isTrue): cameraFound=True
            n+=1
            print(n)

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.coords = tuple((0, 0))

        self.pTime = 0
        self.cTime = 0

    def getCapture(self, width, height):
        self.isTrue, self.frame = self.capture.read()
        self.frame = cv.resize(cv.flip(self.frame, 1), (width, height), interpolation=cv.INTER_CUBIC)
        self.rgbframe = cv.cvtColor(self.frame, cv.COLOR_BGR2RGB)

    def drawLandmark(self):
        self.result = self.hands.process(self.rgbframe)
        if self.result.multi_hand_landmarks:
            for handLandmarks in self.result.multi_hand_landmarks: #Loop through ladnmark data that the model fetches
                self.indexFingerCor = self.getLandmarkCor(handLandmarks, 8)
                self.coords = self.indexFingerCor
                self.thumbFingerCor = self.getLandmarkCor(handLandmarks, 4)
                self.middleFingerCor = self.getLandmarkCor(handLandmarks, 12)

                cv.line(self.frame, self.thumbFingerCor, self.middleFingerCor, (255, 0, 0), thickness=2)
                cv.line(self.frame, self.thumbFingerCor, self.indexFingerCor, (255, 0, 0), thickness=2)
                cv.line(self.frame, self.indexFingerCor, self.middleFingerCor, (255, 0, 0), thickness=2)

                cv.circle(self.frame, self.indexFingerCor, 15, (0,255,255), thickness=-1)

                self.mpDraw.draw_landmarks(self.frame, handLandmarks, self.mpHands.HAND_CONNECTIONS)

        self.cTime = time.time()
        fps = 1/(self.cTime-self.pTime)
        self.pTime = self.cTime

        cv.putText(self.frame, str(int(fps)), (20, 625), cv.FONT_ITALIC, 3, (0, 0, 255), 3)

    def getLandmarkCor(self, handLandmarks, id=0): #Returns Tuple containing coordinates of specified landmark
        Finger = handLandmarks.landmark[id]
        height, width, channel = self.frame.shape
        FingerCor = tuple((int(Finger.x*width), int(Finger.y*height)))
        return FingerCor

    def getCoords(self):
        return self.coords

    def ifClicked(self):
        dist = ((self.middleFingerCor[0]-self.thumbFingerCor[0])*(self.thumbFingerCor[1]-self.indexFingerCor[1]) - (self.thumbFingerCor[0]-self.indexFingerCor[0])*(self.middleFingerCor[1]-self.thumbFingerCor[1]))/math.hypot(self.middleFingerCor[0]-self.thumbFingerCor[0], self.middleFingerCor[1]-self.thumbFingerCor[1])
        if(dist<=10): #  For now 0 is the threshold, it can even be a +ve num so the user doesn't have to bend finger too low
            return tuple((self.indexFingerCor[0], self.indexFingerCor[1])), True
        return tuple((0, 0)), False

    def returnProcessedVideoFeed(self):
        return self.frame

    def stopRender(self):
        self.capture.release()
        cv.destroyAllWindows()
