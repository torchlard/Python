import numpy as np
import cv2

H_MIN,H_MAX,S_MIN,S_MAX,V_MIN,V_MAX  = 0,256,0,256,0,256
FRAME_WIDTH, FRAME_HEIGHT = 640, 480
MAX_NUM_OBJECTS = 50
MIN_OBJECT_AREA = 20*20
MAX_OBJECT_AREA  = FRAME_WIDTH*FRAME_HEIGHT/1.5

windowName = "Original Image"
windowName1 = "HSV Image"
windowName2 = "Thershold Image"
windowName3 = "After Morphological Operation"
trackbarWindowName = "Trackbars"

def on_trackbar(pos): return None
def createTrackbars():      # create tracker window
    cv2.namedWindow(trackbarWindowName,0)
    TrackbarName = ''
    print(TrackbarName, 'H_MIN', H_MIN)
    print(TrackbarName, 'H_MAX', H_MAX)
    print(TrackbarName, 'S_MIN', S_MIN)
    print(TrackbarName, 'S_MAX', S_MAX)
    print(TrackbarName, 'V_MIN', V_MIN)
    print(TrackbarName, 'V_MAX', V_MAX)
    cv2.createTrackbar("H_MIN", trackbarWindowName, H_MIN, H_MAX, on_trackbar )
    cv2.createTrackbar("H_MAX", trackbarWindowName, H_MAX, H_MAX, on_trackbar )
    cv2.createTrackbar("S_MIN", trackbarWindowName, S_MIN, S_MAX, on_trackbar )
    cv2.createTrackbar("S_MAX", trackbarWindowName, S_MAX, S_MAX, on_trackbar )
    cv2.createTrackbar("V_MIN", trackbarWindowName, V_MIN, V_MAX, on_trackbar )
    cv2.createTrackbar("V_MAX", trackbarWindowName, V_MAX, V_MAX, on_trackbar )

def drawObject(x,y, frame):
    cv2.circle(frame, (x,y), (x,y-25), (0,255,0),2 )
    cv2.line(frame,(x,y),(x,max(y-25,0)),(0,255,0),2)   #top
    cv2.line(frame,(x,y),(x,min(y+25,FRAME_HEIGHT)),(0,255,0),2)    #bottom
    cv2.line(frame,(x,y),(max(0,x-25),y),(0,255,0),2) #left
    cv2.line(frame,(x,y),(min(FRAME_WIDTH,x+25),y),(0,255,0),2) #right
    cv2.putText(frame, str(x)+','+str(y), (x,y+30), 1,1,(0,255,0), 2 )

def morphOps(thresh):
    erodeElement = cv2.getStructuringElement(cv2.MORPH_RECT,(3,3))
    dilateElement = cv2.getStructuringElement(cv2.MORPH_RECT,(8,8))
    cv2.erode(thresh, thresh, erodeElement)
    cv2.erode(thresh, thresh, erodeElement)
    cv2.dilate(thresh, thresh, dilateElement)
    cv2.dilate(thresh, thresh, dilateElement)

def trackFilteredObject(x,y,threshold,cameraFeed):
    temp, contours, hierarchy = np.empty([]), np.empty([]), np.empty([])
    threshold.copyTo(temp)
    cv2.


def main():
    createTrackbars()
    cv2.waitKey()
    cv2.destroyAllWindows()

main()













