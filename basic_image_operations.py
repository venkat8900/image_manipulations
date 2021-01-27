from skimage import io
import numpy as np
from matplotlib import pyplot as plt 
from skimage import img_as_float # convert integers(of images) into floating point

my_image = io.imread("images/one.jpg")
print(my_image) # prints a numpy array # unsigned 8 bit
plt.imshow(my_image)

float_img = img_as_float(my_image)
print(my_float_img.min(), my_float_img.max())
plt.imshow(float_img)

rand_img = np.ranom.random([250, 250])
plt.imshow(rand_img)
print(rand_img) # floating point
print(rand_img.min(), rand_img.max())

my_image[20:250, 10: 250, :] = [255, 255, 0] # draw a yellow box
plt.imshow(my_image)

##############################################

from PIL import Image

img = Image.open("images/one.jpg")
print(type(img)) # image is not a numpy library

img_1 = np.asarray(img) # convert imported image using pillow into numpy array

###############################################

import matplotlib.image as mpimg
import matplotlib.pyplot as plt

img = mping.imread("images/one.jpg") # imports as numpy array. 


##############################################

# scikit-image: can be used gor geometric transformation, segmentation, color manipulation, analysis, filtering, feature detection etc. 
from skimage import io, img_as_float, img_as_ubyte

image = io.imread("images/one.jpg")
print(type(image)) # numpy array
image_float = img_as_float(image)
print(image_float)

############################################

import cv2
# cv2 handles images as BGR

img = cv2.imread("images/one.jpg")
grey_img = cv2.imread("images/one.jpg", 0) # grey image
color_img = cv2.imread("images/one.jpg", 1) # color image

cv2.imshow("Greyscale Image:", grey_img)
cv.waitKey(0)# if you mention some time(in ms), it will kill it after that time, else it will kill after we press the close button
cv2.destroyAllWindows()

################################################
# For czi files - these can be 5D images - 5th dimeniosn is time. 

import czifile

img = czifile.imread("images/test_image.czi")
print(img.shape) # we get (1, 512, 512, 3) where 1 is time frame. 

################################################
# OME - TIFF - 5Dimage and has an XML embedded
# pip install apeer-ometiff-library

from apeer_ometiff_library import io

(img2, omexml) = io.read_ometiff("images/test_img.ome.tif")
print(img2.shape) # deimensions = (1, 1, 3, 512, 559) ---> (time series, num_dim, RGB, x, y)

################################################
# reading images in sub folders

import cv2
import glob

path = "images/test_images/dogs/*"

for file in glob.glob(path):
	print(file) # goes into each and every file in the path. We get the file name
	a = cv2.imread(file)
	print(a)
	


