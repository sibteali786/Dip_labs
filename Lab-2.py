import cv2 as cv
import numpy as np

image = cv.imread(r'einstein.tif',cv.IMREAD_GRAYSCALE)
print("The width and height of image is \n",image.shape)
# width = image.shape[0]
# height = image.shape[1]
# # prints all the values from -1  i.e last column to first column in reverse direction
# # Flipping on y axis
# imageVertical = image[:,::-1]
# # Flipping on x axis
# imageHorizontal = image[::-1,:]
# # Flipping on both axis
# imageInvertedOnXYAxis = image[::-1,::-1]
# cv.imshow("Original",image)
# cv.imshow("Vertical Image",imageVertical)
# cv.imshow("Horizontal Image",imageHorizontal)
# cv.imshow("XYAxis Image",imageInvertedOnXYAxis)

# Task No 2
def fourSidedSquare(size):
    image = np.zeros([size,size,3],dtype=np.uint8)
    image.fill(255)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            if 0 <= i < (size * 0.1) and 0 <= j < (size * 0.1):
                image[i][j] = 0
            if (size-(size*0.1)) <= i < (size) and (size-(size*0.1)) <= j < size:
                image[i][j] = (0,255,0)
            if (size-(size*0.1)) <= i < (size) and 0 <= j < (size * 0.1):
                image[i][j] = (255,0,0)
            if (size-(size*0.1)) <= j < (size) and 0 <= i < (size * 0.1):
                image[i][j]= (0,0,255)

    return image

cv.imshow("Four Sided Boxes",fourSidedSquare(285))
cv.waitKey()


