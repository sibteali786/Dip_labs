# Task No 1
import numpy as np
import cv2 as cv
import math
# checking for a clear image and result is accurate
# def VertcialLineImage(imageSize,verticaLines):
#     img = np.zeros([imageSize,imageSize])
#     img.fill(0)
#     for t in range(1,verticaLines,2):
#         for i in range(0,imageSize):
#             for j in range((imageSize//verticaLines)*t,(imageSize//verticaLines)*(t+1)):
#                 img[i][j] = 255
#     return img
# image = VertcialLineImage(7*49,7)
# cv.imshow("Images",image)
# cv.waitKey()
# # image = cv.imread(r'pic_3_lab3.png',cv.IMREAD_GRAYSCALE)
# # cv.imshow("threshold",image)
# # cv.waitKey()
# # thresholding to consider only specific values
# # ret,image = cv.threshold(image,127,255,cv.THRESH_BINARY)
# # label
# label = 0
# # defining the v set for the CCA
# v = 1
# for i in range(image.shape[0]):
#     for j in range(image.shape[1]):
#         if image[i][j] == 255:
#             image[i][j] = 1
#
# # applying cca to label different part of the image
# image1 = np.zeros([image.shape[0],image.shape[1]],dtype=np.uint8)
# print(image1.shape)
# image = np.lib.pad(image,((1,1),(1,1)),mode='constant',constant_values=(0,0))
# print(image.shape)
# for i in range(1,image.shape[0]):
#     for j in range(1,image.shape[1]):
#         if image[i][j] != 0:
#             if image[i][j-1] == 0 and image[i-1][j] == 0:
#                 label = label + 1
#                 image1[i-1][j-1] = label
#             if image[i][j-1] == v:
#                 image1[i-1][j-1] = image1[i-1][(j-1)-1]
#             if image[i-1][j] == v:
#                 image1[i-1][j-1] = image1[(i-1)-1][j-1]
#             if image[i-1][j] == v and image[i][j-1] == v:
#                 image1[i-1][j-1] = min(image1[(i-1)-1][j-1],image1[i-1][(j-1)-1])
#
# print(label)

# The algorithm is working good for pictures with clear object boundaries


# Task No 2
def distancesChoiced(p1,p2,choice):
    x1,y1 = p1
    x2,y2 = p2
    # choice 1 is city block
    if choice == 1:
        return abs(x1-x2) + abs(y1-y2)
    # choice 2 chessboard distance
    if choice == 2:
        return max(abs(x1-x2),abs(y1-y2))
    # choice 3 euclidean
    if choice == 3:
        return math.sqrt((abs(x1-x2))**2 + (abs(y1-y2))**2)

res = distancesChoiced((1,3),(2,4),3)
print("The distance as per choice is {}".format(res))