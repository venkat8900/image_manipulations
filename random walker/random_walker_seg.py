from skimage import io, img_as_float
import matplotlib.pyplot as plt
import numpy as np
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import exposure # contains functions for CLAHE
from skimage.segmentation import random_walker

# solves anisotropic diffusion equation to calcuate local diffusivity coefficient
# then it decides whether a particular pixel is a part of segment A or segment B
# historgram doesn't work well as there are regions where the intensities of pixels are different

# read image
img = img_as_float(io.imread("images/random_walker/Alloy_noisy.jpg"))

# plot histogram
# plt.hist(img.flat, bins = 100, range = (0, 1))
# concentrated only at one end

# we need to try removing the noise and checking histogram once
# can use non local mean
sigma_est = np.mean(estimate_sigma(img, multichannel = True))
denoise= denoise_nl_means(img, h = 1.15 * sigma_est, fast_mode = True, patch_size = 5,
                          patch_distance = 3, multichannel = True)

# plt.hist(denoise.flat, bins = 100, range = (0, 1))
# still cannot use thresholding as there are bunch of values between the peaks were we have lot of overlap

# Conteast limited adaptive histogram equalisation CLAHE
equa_img = exposure.equalize_adapthist(denoise)
# but not good enough for histogram based segmentation
plt.hist(equa_img.flat, bins = 100, range = (0, 1))
plt.imsave("images/random_walker/CLAHE_equa_img.jpg", equa_img, cmap = 'gray')

markers = np.zeros(img.shape, dtype = np.uint)
# we need to put the markers in the region where we know we are highly confident

# define the markers within these regions
markers[(equa_img < 0.6) & (equa_img > 0.3)] = 1
markers[(equa_img > 0.8) & (equa_img < 0.99)] = 2

# plt.imshow(markers)
plt.imsave("images/random_walker/markers.jpg", markers, cmap = 'gray')

labels = random_walker(equa_img, markers, beta = 10, mode = 'bf') # beta is penalization coefficient
# creates a label image of value 0 and 1
plt.imshow(labels)
plt.imsave("images/random_walker/random_walker.jpg", labels, cmap = 'gray')

seg_one = (labels == 1)
seg_two = (labels == 2)

segments = np.zeros((equa_img.shape[0], equa_img.shape[1], 3))
segments[seg_one] = (1, 0, 0)
segments[seg_two] = (0, 1, 1)
plt.imshow(segments)
plt.imsave("images/random_walker/random_walker_segments.jpg", segments, cmap = 'gray')

