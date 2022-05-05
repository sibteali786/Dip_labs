import cv2 as cv

image = cv.imread(r'einstein.tif',cv.IMREAD_GRAYSCALE)
print("The width and height of image is \n",image.shape)
width = image.shape[0]
height = image.shape[1]
# prints all the values from -1  i.e last column to first column in reverse direction
# Flipping on y axis
imageVertical = image[:,::-1]
# Flipping on x axis
imageHorizontal = image[::-1,:]
# Flipping on both axis
imageInvertedOnXYAxis = image[::-1,::-1]
cv.imshow("Original",image)
cv.imshow("Vertical Image",imageVertical)
cv.imshow("Horizontal Image",imageHorizontal)
cv.imshow("XYAxis Image",imageInvertedOnXYAxis)
cv.waitKey()

