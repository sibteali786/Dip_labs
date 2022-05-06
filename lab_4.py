import numpy as np
import cv2 as cv

image = cv.imread(r'einstein.tif',cv.IMREAD_GRAYSCALE)
cv.imshow("Original Image",image)

height,width = image.shape
# Task No 1
# Negative Transformation
# negativeTransformation = 255 - image
# cv.imshow("Negative Transformation",negativeTransformation)
# # Log Transformation s = c * log(1+r)
# # r = image array
# # c = 255 / log(1+max(image))
# c = 255 / np.log(np.amax(image) + 1)
# logTransformation = c * np.log(1+image)
# logTransformation = logTransformation.astype(np.uint8)
# cv.imshow("Logarithmic Image",logTransformation)
# cv.waitKey()


# Task no 2


# meanImage = np.mean(image)
# def conditions(image,meanImage):
#     height,width = image.shape
#     image1 = np.zeros([height,width],dtype=np.uint8)
#     image2 = np.zeros([height,width],dtype=np.uint8)
#     image3 = np.zeros([height,width],dtype=np.uint8)
#
#     for i in range(height):
#         for j in range(width):
#             if (image[i][j] >= meanImage):
#                 image1[i][j] = 255
#                 image2[i][j] = 0
#             if (image[i][j] <= meanImage):
#                 image1[i][j] = 0
#                 image2[i][j] = 255
#             if meanImage + 20 >= image[i][j] >= meanImage - 20:
#                 image3[i][j] = 0
#             else:
#                 image3[i][j] = 255
#
#     cv.imshow("Condition a",image1)
#     cv.imshow("Condition b",image2)
#     cv.imshow("Condition c",image3)
# conditions(image,meanImage)
# cv.waitKey()



# Task No 3
# def gammaCorrection(image,gamma):
#     image1 = 255 * ((image/255) ** float(gamma))
#     image1 = image1.astype(np.uint8)
#     cv.imshow("PowerLaw",image1)
#     cv.waitKey()
#
# gammaCorrection(image,0.2)
# gammaCorrection(image,0.5)
# gammaCorrection(image,1.2)
# gammaCorrection(image,1.8)

# Task No 4
for i in range(height):
    for j in range(width):
        if (image[i][j]>=100) and (image[i][j]<=200):
            image[i][j] = 210

cv.imshow("Sliced Image",image)
cv.waitKey()