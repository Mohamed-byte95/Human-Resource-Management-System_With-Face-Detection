import cv2 as cv

img = cv.imread("PICS/Lady.jpg")

cv.imshow("Display window",img)
cv.waitKey(0)