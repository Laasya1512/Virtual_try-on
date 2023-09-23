import os

import cvzone
import cv2
from cvzone.PoseModule import PoseDetector

cap = cv2.VideoCapture("Resources/Videos/m4.mp4")
detector = PoseDetector()

shirtFolderPath = "Resources/Shirts"
listShirts = os.listdir(shirtFolderPath)
# print(listShirts)
fixedRatio = 262 / 190  # widthOfShirt/widthOfPoint11to12
shirtRatioHeightWidth = 581 / 440
imageNumber = 0
imgButtonRight = cv2.imread("Resources/button.png", cv2.IMREAD_UNCHANGED)
imgButtonLeft = cv2.flip(imgButtonRight, 1)
counterRight = 0
counterLeft = 0
selectionSpeed = 10

# Load shirt images for display in the top right corner
shirtImages = []
for shirt in listShirts:
    shirtImg = cv2.imread(os.path.join(shirtFolderPath, shirt))
    shirtImg = cv2.resize(shirtImg, (50, 75))  # Resize for display
    shirtImages.append(shirtImg)

while True:
    success, img = cap.read()
    img = detector.findPose(img)
    # img = cv2.flip(img,1)
    lmList, bboxInfo = detector.findPosition(img, bboxWithHands=False, draw=False)
    if lmList:
        # center = bboxInfo["center"]
        lm11 = lmList[11][1:3]
        lm12 = lmList[12][1:3]
        imgShirt = cv2.imread(os.path.join(shirtFolderPath, listShirts[imageNumber]), cv2.IMREAD_UNCHANGED)

        widthOfShirt = int((lm11[0] - lm12[0]) * fixedRatio)
        print(widthOfShirt)
        imgShirt = cv2.resize(imgShirt, (widthOfShirt, int(widthOfShirt * shirtRatioHeightWidth)))
        currentScale = (lm11[0] - lm12[0]) / 190
        offset = int(44 * currentScale), int(48 * currentScale)

        try:
            img = cvzone.overlayPNG(img, imgShirt, (lm12[0] - offset[0], lm12[1] - offset[1]))
        except:
            pass

        img = cvzone.overlayPNG(img, imgButtonRight, (1074, 293))
        img = cvzone.overlayPNG(img, imgButtonLeft, (72, 293))

        if lmList[16][1] < 300:
            counterRight += 1
            cv2.ellipse(img, (139, 360), (66, 66), 0, 0,
                        counterRight * selectionSpeed, (0, 255, 0), 20)
            if counterRight * selectionSpeed > 360:
                counterRight = 0
                if imageNumber < len(listShirts) - 1:
                    imageNumber += 1
        elif lmList[15][1] > 900:
            counterLeft += 1
            cv2.ellipse(img, (1138, 360), (66, 66), 0, 0,
                        counterLeft * selectionSpeed, (0, 255, 0), 20)
            if counterLeft * selectionSpeed > 360:
                counterLeft = 0
                if imageNumber > 0:
                    imageNumber -= 1

        else:
            counterRight = 0
            counterLeft = 0

    # Display shirt images in the top right corner
    y_offset = 10
    for i, shirtImg in enumerate(shirtImages):
        x_offset = img.shape[1] - 60 - (i * 60)
        img[y_offset:y_offset + shirtImg.shape[0], x_offset:x_offset + shirtImg.shape[1]] = shirtImg
        if i == imageNumber:
            cv2.rectangle(img, (x_offset, y_offset), (x_offset + shirtImg.shape[1], y_offset + shirtImg.shape[0]),
                          (0,204,102), 3)

    cv2.imshow("Image", img)
    cv2.waitKey(1)