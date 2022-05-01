import cv2 as cv
import numpy as np
def blackAndWhite(imageSize,verticaLines):
    img = np.zeros([imageSize,imageSize])
    img.fill(0)
    for t in range(1,verticaLines,2):
        for i in range(0,imageSize):
            for j in range((imageSize//verticaLines)*t,(imageSize//verticaLines)*(t+1)):
                img[i][j] = 255
    return img
img = blackAndWhite(7*49,7)  # the size of image should be integral multiple of vertical lines
cv.imshow("VerticalLines",img)
cv.waitKey()

