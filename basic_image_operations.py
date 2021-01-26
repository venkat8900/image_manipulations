from skimage import io
import numpy as np
from matplotlib import pyplot as plt 
from skimage import img_as_float # convert integers(of images) into floating point

my_image = io.imread(images/one.jpg)
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