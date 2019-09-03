

# ---------------------------- Imports ------------------------------ #

import numpy as np 
# from PIL import Image		#careful: even if you install the "pillow" module, you still need to import PIL. Lmao
import cv2
from matplotlib import pyplot as plt

import rlsa





# ------------------ Short cv2 manual --------------------------- #

#		Basics
# img=cv2.imread('---.jpg') 				to load image. It gets stored as a numpy array
# img[100,100] = [255 255 255] 		to modify single pixel (inefficient)
# img[100,100,0] = 255 					to modify single channel of pixel (0: blue, 1:green, 2:red)
# img.item(100, 100, 0) 					to access channel of pixel (more efficient)
# img.itemset((100,100,0), 255) 		to set value (more efficient
# print img.shape 							prints (height, width, number of channels)
# print img.size 							prints number of pixels
# print img.dtype
# area = img[100:120, 200:300] 		select a portion of the image

#		Filters https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html
# cv2.filter2D()								convolve the image with a kernel defined by the user
# cv2.blur(img,(5,5))						returns the average of pixels in an area of the chosen size
# cv2.GaussianBlur(img,(5,5),0)			same as above but with gaussian average. Defining a gaussian kernel by hand is also possible
# cv2.medianBlur(img,5)					median filter (always returns a value already present in the image)
# cv2.bilateralFilter(img,9,75,75)		edge-preserving filter (slow)


# --------------------- Loading image ---------------------------- #

img = cv2.imread( '09_060.jpg' )			#open image 
#print img										#print the array 
print( img.shape )								#Note: needs parenthesis in python3

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)			#converting the image to greyscale
#print gray										
print( gray.shape )



# ----------- Preprocessing 0: Median Filter --------------- # 

#blur = cv2.medianBlur(gray,3)
#blur = cv2.bilateralFilter(img,9,75,75)

# Filtering notes
# A medianBlur filter AFTER thresholding results in disaster, even at the lower size.
# A medianBlur filter before thresholding gives slightly better results, but still unsatisfactory (fragmented edges).
# A bilateral filter before thresholding produces better results, but still seems to cause some bubble disgregation.
# A bilateral filter AFTER thresholding does absolutely nothing.
# Running the image through Waifu2x (an online noise removal thing used by CLs), then thresholding also gave pretty much the same result

# I just skipped this part for now, probably we can do better by changing those parameters
# However, when we have bubbles with edges only 1-2 pixels thick, it might be impossible to preserve them and still remove a significant amount of noise...?



# ----------- Preprocessing 1: Thresholding --------------- # 

ret,thr = cv2.threshold(gray,127,255,cv2.THRESH_BINARY)		#thresholding the image. Note: the first return value is used to determine the optimal thresholding value, in any case it must be there or it will give an error.
print( thr.shape )





# --------------- Preprocessing 2:RLSA ----------------------- # 

# This algorithm is used to connect regions of black pixels to better categorize them later on.

# There's someone working on an implementation of the algorithm in python here: https://github.com/Vasistareddy/pythonRLSA
# But I didn't understand how to install it, so I wrote my own version.

# The first parameter is the maximum distance at which black pixels are joined in the horizontal direction, the second applies to the vertical direction.
joined = rlsa.rlsa( thr, 5, 30 )	
			





titles = ['Original Image', 'Thresholded', 'Rlsaed']
images = [img, thr, joined]

for i in range(3):					#Note: xrange deprecated in python3
    plt.subplot(1,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()





























