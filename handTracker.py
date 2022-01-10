import cv2 as cv
import time
import mediapipe as mp
import math

#OS keeps switching the index of cameras, this finds the right one.
capture = cv.VideoCapture(0)
mpHands=  mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

def getLandmarkCor(handLandmarks, id=0): #Returns Tuple containing coordinates of specified landmark
    Finger = handLandmarks.landmark[id]
    height, width, channel = frame.shape
    FingerCor = tuple((int(Finger.x*width), int(Finger.y*height)))
    return FingerCor


while True:
        isTrue, frame = capture.read()
        frame = cv.flip(frame, 1)
        rgbframe = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
        result = hands.process(rgbframe)
        #print(result.multi_hand_landmarks)

        if result.multi_hand_landmarks:
            for handLandmarks in result.multi_hand_landmarks: #Loop through ladnmark data that the model fetches
                indexFingerCor = getLandmarkCor(handLandmarks, 8)
                thumbFingerCor = getLandmarkCor(handLandmarks, 4)
                middleFingerCor = getLandmarkCor(handLandmarks, 12)

                cv.line(frame, thumbFingerCor, middleFingerCor, (255, 0, 0), thickness=2)
                cv.line(frame, thumbFingerCor, indexFingerCor, (255, 0, 0), thickness=2)
                cv.line(frame, indexFingerCor, middleFingerCor, (255, 0, 0), thickness=2)

                dist = ((middleFingerCor[0]-thumbFingerCor[0])*(thumbFingerCor[1]-indexFingerCor[1]) - (thumbFingerCor[0]-indexFingerCor[0])*(middleFingerCor[1]-thumbFingerCor[1]))/math.hypot(middleFingerCor[0]-thumbFingerCor[0], middleFingerCor[1]-thumbFingerCor[1])
                if(dist<=0):
                    print("Click Found")
                #base = tuple(((thumbFingerCor[0]+middleFingerCor[0])/2, (middleFingerCor[1]+middleFingerCor[1])/2))

                cv.circle(frame, indexFingerCor, 15, (0,255,255), thickness=-1)

                mpDraw.draw_landmarks(frame, handLandmarks, mpHands.HAND_CONNECTIONS)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv.putText(frame, str(int(fps)), (10, 70), cv.FONT_ITALIC, 3, (0, 0, 255), 3)

        if(isTrue):
            cv.imshow('Video', frame)

        if cv.waitKey(20) & 0xFF==ord('d'):
            break

capture.release()
cv.destroyAllWindows()
