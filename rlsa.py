

import numpy as np
import cv2
from matplotlib import pyplot as plt


# definition of horizontal rlsa; whenever the horizontal distance between two
# black pixels is less than lim, all white pixels in between are turned black.
def hor_rlsa2(img, lim):

    img_out = np.copy(img)						# makes a copy of img
    # cicles through rows (shape[0] is the height of the image)
    for i in range(img.shape[0]):

        acc = 0										# sets up a counter for white pixels
        # ciclyng along the i-th row (shape[1] is the widht of the image)
        for j in range(img.shape[1]):

            if img[i, j] == 255:
                acc += 1								# counting white pixels
            else:
                if acc < lim: 							# if there are not enough white pixels in between, all are turned black
                    for k in range(acc):
                        img_out[i, j - k - 1] = 0
                acc = 0								# counter reset

    return img_out

# definition of vertical rlsa, which works exactly the same


def ver_rlsa2(img, lim):

    img_out = np.copy(img)
    for j in range(img.shape[1]):

        acc = 0
        for i in range(img.shape[0]):

            if img[i, j] == 255:
                acc += 1
            else:
                if acc < lim:
                    for k in range(acc):
                        img_out[i - k - 1, j] = 0
                acc = 0

    return img_out

# definition or rlsa itself. The function is fed an horizontal and a vertical
# limit, executes the algorithm in the two directions separately, then proceeds
# to overlap the images.


def rlsa(img, h_lim, v_lim):

    img_h = hor_rlsa2(img, h_lim)
    img_v = ver_rlsa2(img, v_lim)

    # it's minimum becaus black pixels are 0s, duh
    return np.minimum(img_h, img_v)
