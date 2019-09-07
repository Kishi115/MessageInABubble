

# ---------------------------- Imports ------------------------------ #

# import numpy as np
# from PIL import Image
import cv2
from matplotlib import pyplot as plt

import rlsa

from skimage import measure

# from skimage import filter as filters


# ------------------ Short cv2 manual --------------------------- #

# 		Basics
# img=cv2.imread('---.jpg') 	  to load image. It gets stored as a numpy array
# img[100,100] = [255 255 255] 	  to modify single pixel (inefficient)
# img[100,100,0] = 255 			  to modify single channel of pixel
# (0: blue, 1:green, 2:red)

# img.item(100, 100, 0) 		  to access channel of pixel (more efficient)
# img.itemset((100,100,0), 255)   to set value (more efficient
# print img.shape 				  prints (height, width, number of channels)
# print img.size 				  prints number of pixels
# print img.dtype
# area = img[100:120, 200:300] 	  select a portion of the image

# 		Filters
# https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_imgproc/py_filtering/py_filtering.html

# cv2.filter2D()				  convolve the image with a kernel defined by the user
# cv2.blur(img,(5,5))			  returns average of pixels in an area of chosen size
# cv2.GaussianBlur(img,(5,5),0)	  same as above but with gaussian average.
# Defining a gaussian kernel by hand is also possible

# cv2.medianBlur(img,5)			  median filter (always returns a value already
# present in the image)

# cv2.bilateralFilter(img,9,75,75) edge-preserving filter (slow)

def process_image(image):

    # --------------------- Loading image ---------------------------- #

    # open image
    img = cv2.imread(image)

    # print img
    # print the array
    print(img.shape)

    # converting the image to greyscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # print gray
    print(gray.shape)

    # ----------- Preprocessing 0: Median Filter --------------- #

    # blur = cv2.medianBlur(gray,3)
    # blur = cv2.bilateralFilter(img,9,75,75)

    # Filtering notes
    # A medianBlur filter AFTER thresholding results in disaster, even at the
    # lower size.
    # A medianBlur filter before thresholding gives slightly better results,
    # but still unsatisfactory (fragmented edges).
    # A bilateral filter before thresholding produces better results, but still
    # seems to cause some bubble disgregation.
    # A bilateral filter AFTER thresholding does absolutely nothing.
    # Running the image through Waifu2x (an online noise removal thing used by
    # CLs). then thresholding also gave pretty much the same result

    # I just skipped this part for now, probably we can do better by changing
    # those parameters
    # However, when we have bubbles with edges only 1-2 pixels thick, it might
    # be impossible to preserve them and still remove a significant amount
    # of noise...?

    # ----------- Preprocessing 1: Thresholding --------------- #

    # thresholding the image. Note: the first return value is used to determine
    # the optimal thresholding value, in any case it must be there or it will
    # give an error.
    ret, thr = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)
    print(thr.shape)

    # --------------- Preprocessing 2:RLSA ----------------------- #

    # This algorithm is used to connect regions of black pixels to better
    # categorize them later on.

    # There's someone working on an implementation of the algorithm in python
    # here: https://github.com/Vasistareddy/pythonRLSA
    # But I didn't understand how to install it, so I wrote my own version.

    # The first parameter is the maximum distance at which black pixels are
    # joined in the horizontal direction, the second applies to the vertical
    # direction.

    # joined = rlsa.rlsa( thr, 10, 30 )

    # One VERY EVIDENT PROBLEM is that, in the joining process,
    # a lot of white pixels are left stranded in the middle of black lines
    # (the image is separated into 1049 segments).

    joined = rlsa.rlsa(thr, 10, 30)
    joined = rlsa.rlsa(joined, 10, 30)

    # Running the algorithm a second time does a lot of good (the number of
    # segments is down to 147).

    # For now, setting a higher threshold and running the algorithm twice
    # greatly trims down the number of segments (about 60). However, this takes
    # a few seconds to compute, which is pretty long.

    # ------------- Preprocessing 3: Segmentation ------------ #

    # Some fancy stuff going on here. Just checking out how some existing
    # function works, and deciding if we should make our own.

    # joined =  cv2.bilateralFilter(joined,15,75,75)
    # ret,joined = cv2.threshold(joined,127,255,cv2.THRESH_BINARY)

    all_labels, num_labels = measure.label(joined, return_num=1)
    # return_num=1 is a boolean trigger to have the function print the number
    # of labels, to be stored in num_labels.
    # the default connectivity is the number of dimensions (this means that
    # diagonal pixels are considered as neighbors).

    print(num_labels)

    # It's also possible to manipulate the segments. Instructions here
    # https://scikit-image.org/docs/dev/api/skimage.measure.html

    # titles = ['Original Image', 'Thresholded', 'Rlsaed']
    # images = [img, thr, joined]

    titles = ['Original Image', 'Rlsaed', 'Segmented']
    images = [img, joined, all_labels]

    for i in range(2):  # Note: xrange deprecated in python3
        plt.subplot(1, 3, i + 1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]), plt.yticks([])
    plt.subplot(1, 3, 3), plt.imshow(images[2], cmap='hsv')
    plt.title(titles[2])
    plt.xticks([]), plt.yticks([])

    plt.show()

    return None
