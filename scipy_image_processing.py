from scipy import misc
from skimage import io, img_as_ubyte
from scipy import ndimage 
import numpy as np
from matplotlib import pyplot as plt


# img = misc.images("images/one.jpg") # np array 

img = io.imread("images/one.jpg")

# print(img.shape, img.dtype) # RGB image

img1 = io.imread("images/one.jpg", as_gray = True) # takes in gray scale image, float 64
img1 = img_as_ubyte(io.imread("images/one.jpg")) # converts back the image into unsigned 8 bit

mean_grey = img1.mean()
min_val = img1.min()
max_val = img1.max()

# basic geometric transformations

flip_LR = np.fliplr(img1) # flip left right
flip_UD = np.flipud(img1) #  flip upsite down

plt.subplot(2,2,1)
plt.imshow(img1, cmap = "Greys") # plots in gray scale
plt.subplot(2,2,3)
plt.imshow(flip_LR, cmap = "Blues") # plots in blue scale
plt.subplot(2,2,4)
plt.imshow(flip_UD, cmap = "hsv")

rotate = ndimage.rotate(img1, 45, reshape = "False") # rotate by 45 degrees without reshape
plt.imshow(rotate)

# filters

uni_filter = ndimage.uniform_filter(img1, size = 9) # type of blurring filter
plt.imshow(uni_filter)

gau_filter = ndimage.gaussian_filter(img1, sigma = 3)   # smooth the noise in genral, but edges will be affected if sigma is high
plt.imshow(gau_filter)

med_filter = ndimage.median_filter(img1, 3) # preserves the edges
plt.imshow(med_filter)

sob_filter = ndimage.sobel_filter(img1) # detects the edges in the images
plt.imshow(sob_filter)