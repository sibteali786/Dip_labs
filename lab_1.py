import cv2 as cv
import numpy as np
def VertcialLineImage(imageSize,verticaLines):
    img = np.zeros([imageSize,imageSize])
    img.fill(0)
    for t in range(1,verticaLines,2):
        for i in range(0,imageSize):
            for j in range((imageSize//verticaLines)*t,(imageSize//verticaLines)*(t+1)):
                img[i][j] = 255
    return img
img = VertcialLineImage(7*49,7)  # the size of image should be integral multiple of vertical lines
cv.imshow("VerticalLines",img)


def boxImage(imageSize,noOfBoxes):
    img = np.zeros([imageSize, imageSize])
    img.fill(0)
    for u in range(0,noOfBoxes,2):
        for v in range(0,noOfBoxes,2):
            for i in range(v*(imageSize//noOfBoxes),(v+1)*(imageSize//noOfBoxes)):
                for j in range(u*(imageSize//noOfBoxes),(u+1)*(imageSize//noOfBoxes)):
                    img[i][j] = 255
    return img
imgVertHori = boxImage(400,10);
cv.imshow("Vertical And Horizontal Lines",imgVertHori)
cv.waitKey()