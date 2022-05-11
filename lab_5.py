import numpy as np
import matplotlib.pyplot as plt
import cv2

img = cv2.imread(r"lab5/washed_out_pollen_image.tif",0)
img = cv2.resize(img,(0,0),fx = 0.5,fy = 0.5)
cv2.imshow("Original",img)


# finding percentiles
minimum = np.percentile(img,5)
maximum = np.percentile(img,95)
height,width = img.shape
binaryArrayRange = np.arange(2**8)
# Histogram of original Image grayscale
def histogram(img):
    histogramImage = np.zeros(256)
    value = 0
    for i in range(img.shape[0]):
        for j in range(img.shape[1]):
            value = img[i][j]
#             Adding each time same pixels comes in observation accross image pixels
            histogramImage[value] = histogramImage[value] + 1
    return histogramImage
# plt.plot(binaryArrayRange,histogram(img))

# Task No 1
# Applyting percentiles
# imgPercntiled = np.zeros([img.shape[0],img.shape[1]],dtype=np.uint8)
# for i in range(height):
#     for j in range(width):
#         if (img[i][j] <= minimum):
#             imgPercntiled[i][j] = 0
#         elif (img[i][j] >= maximum):
#             imgPercntiled[i][j] = 255
#         else:
#             imgPercntiled[i][j] = ((img[i][j]-minimum)/(maximum-minimum))*255
# img = img.astype(np.uint8)
# cv2.imshow("Contrast Stretched with percentile",imgPercntiled)
# cv2.waitKey()
# # Its histogram
# plt.plot(binaryArrayRange,histogram(imgPercntiled))
# plt.show()


# Task 2
# Histogram Equalization

# histogram
histogramImage = histogram(img)
plt.plot(binaryArrayRange,histogramImage)
plt.xlabel("Image Pixels")
plt.ylabel("Image Pixels Counts")
plt.title("Histogram")

# Pdf of the histogram counts
# pdf = Image Histogram / Rows * Columns
pdf_Img = histogramImage/(img.shape[0]*img.shape[1])
# plt.figure(2)
# plt.plot(binaryArrayRange,pdf_Img)
# plt.xlabel("Pixels")
# plt.ylabel("PDF")
# plt.title("PDF_Histogram")
# plt.show()

# Cdf of the image
cdfArr = np.zeros(len(pdf_Img))
for i in range(1,255):
    cdfArr[i] = cdfArr[i-1] + pdf_Img[i]
# plt.figure(3)
# plt.plot(binaryArrayRange,cdfArr)
# plt.xlabel("Pixels")
# plt.ylabel("CDF")
# plt.title("CDF_Histogram")
# plt.show()

# Transformation function
transformationFucntion = np.around(cdfArr * 255)
# plt.figure(4)
# plt.plot(binaryArrayRange,transformationFucntion)
# plt.xlabel("Pixels")
# plt.ylabel("CDF")
# plt.title("transformation Function Histogram")
# plt.show()

# Applying transformation function to original image
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        holder = img[i][j]
        img[i][j] = transformationFucntion[holder]

cv2.imshow("Contrast Enhanced Using Histogram Euqlaization",img)
cv2.waitKey()

# Histogram
plt.plot(binaryArrayRange,histogram(img))
plt.show()