import cv2
import numpy as np
from detect_objects import *


#Import detector, load image and define contours
detector = BackgroundDetector()

img = cv2.imread("set.jpg")

contours = detector.detect_objects(img)


#Object boundaries
for cnt in contours:
    #Get rectangle
    rect = cv2.minAreaRect(cnt)
    (x, y), (w, h), angle = cv2.minAreaRect(cnt)

    
    #Display box
    box = cv2.boxPoints(rect)
    box = np.int0(box)
    cv2.circle(img, (int(x), int(y)), 5, (0, 255, 0), -1)
    cv2.polylines(img, [box], True, (255, 0, 0), 3)
    cv2.putText(img, "Width {}".format(round(w, 2)), (int(x - 100),int(y-20)), cv2.FONT_ITALIC, 1, (0, 150, 255), 2)
    cv2.putText(img, "Height {}".format(round(h, 2)), (int(x- 100),int(y+20)), cv2.FONT_ITALIC, 1, (0, 150, 255), 2)

cv2.imshow("Sample image", img)
cv2.waitKey(0)