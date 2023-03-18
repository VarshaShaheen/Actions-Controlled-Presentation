import os
import cv2
import pyautogui
from cvzone.HandTrackingModule import HandDetector

# variables
width, height = pyautogui.size()
folderPath = "ppt"

# camera setup
cap = cv2.VideoCapture(0)
cap.set(3, width)  # set Width
cap.set(4, height)  # set Height

# presentation images
pathImages = sorted(os.listdir(folderPath), key=len)
print(pathImages)

# variables
imgNumber = 0
hs, ws = int(120 * 1.2), int(213 * 1.2)

# hand detector
detector = HandDetector(detectionCon=0.8, maxHands=1)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    pathFullImage = os.path.join(folderPath, pathImages[imgNumber])
    imgCurrent = cv2.imread(pathFullImage)

    # check if window is maximized
    if cv2.getWindowProperty("Slides", -1) == cv2.WINDOW_FULLSCREEN:
        # resize the image to fill the screen
        imgCurrent = cv2.resize(imgCurrent, (width, height), interpolation=cv2.INTER_AREA)

    hands, img = detector.findHands(img)

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        print(fingers)

        # Gesture 1
        if fingers == [1, 0 ,0 , 0, 0]:
            print ("Left")


    # Adding webcam image to the presentation
    imgSmall = cv2.resize(img, (ws, hs))
    h, w, _ = imgCurrent.shape
    imgCurrent[0:hs, w - ws:w] = imgSmall   # overlaying camera image

    cv2.imshow("Image", img)
    cv2.imshow("Slides", imgCurrent)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
