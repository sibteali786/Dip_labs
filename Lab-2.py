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
# def fourSidedSquare(size):
#     image = np.zeros([size,size,3],dtype=np.uint8)
#     image.fill(255)
#     for i in range(image.shape[0]):
#         for j in range(image.shape[1]):
#             if 0 <= i < (size * 0.1) and 0 <= j < (size * 0.1):
#                 image[i][j] = 0
#             if (size-(size*0.1)) <= i < (size) and (size-(size*0.1)) <= j < size:
#                 image[i][j] = (0,255,0)
#             if (size-(size*0.1)) <= i < (size) and 0 <= j < (size * 0.1):
#                 image[i][j] = (255,0,0)
#             if (size-(size*0.1)) <= j < (size) and 0 <= i < (size * 0.1):
#                 image[i][j]= (0,0,255)
#
#     return image
#
# cv.imshow("Four Sided Boxes",fourSidedSquare(285))
# cv.waitKey()


# Task no 3
# Width,Height=image.shape #Width and Height
# Left_Adjust=int(Width/10); #10% Left Right Adjust
# Total_Left_Count=Width+(2*Left_Adjust);
# Coloumn_Adjust=Total_Left_Count-Height;
# Total_Coloumn_Count=Coloumn_Adjust+Height;
# print(Width,Height);
# Borderedimage=np.zeros([Total_Coloumn_Count,Total_Left_Count],dtype=np.uint8)
# print(Borderedimage.shape)
# Borderedimage[Left_Adjust:Total_Left_Count-Left_Adjust,int(Coloumn_Adjust/2):Total_Coloumn_Count-int(Coloumn_Adjust/2)-1]=image[:,:]
# cv.imshow('pp',Borderedimage)
# cv.waitKey()


# Task No 4
# rotatedImageClockwise = cv.rotate(image,cv.cv2.ROTATE_90_CLOCKWISE)
# cv.imwrite("rotatedEinstein.jpg",rotatedImageClockwise)
# cv.imshow("Clockwise Rotated Image",rotatedImageClockwise)
# cv.waitKey()

# Task No 5
scalePercent = 0.5
width = int(image.shape[1]*scalePercent)
height = int(image.shape[0]*scalePercent)
dimension = (width,height)
resized_InterArea = cv.resize(image,dimension,interpolation=cv.INTER_AREA)
resized_InterNearest = cv.resize(image,dimension,interpolation=cv.INTER_NEAREST)
resized_Linear = cv.resize(image,dimension,interpolation=cv.INTER_LINEAR)
resized_Cubic = cv.resize(image,dimension,interpolation=cv.INTER_CUBIC)

cv.imshow("Inter Area Interplotation",resized_InterArea)
cv.imshow("Inter Nearest Interplotation",resized_InterNearest)
cv.imshow("Linear Interplotation",resized_Linear)
cv.imshow("Cubix Interplotation",resized_Cubic)
cv.waitKey()


