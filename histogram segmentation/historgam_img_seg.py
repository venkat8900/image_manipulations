from skimage import io, img_as_float, img_as_ubyte # for image processing make sure you import img as float
from scipy import ndimage as nd
from matplotlib import pyplot as plt
from skimage.restoration import denoise_nl_means, estimate_sigma
import numpy as np

img = img_as_float(io.imread("images/noisy.jpg"))
sigma_est = np.mean(estimate_sigma(img, multichannel = True))
denoise= denoise_nl_means(img, h = 1.15 * sigma_est, fast_mode = True, patch_size = 5,
                          patch_distance = 3, multichannel = True)

# convert the iamge ack to 8 bits
denoise_ubyte = img_as_ubyte(denoise)
plt.hist(denoise_ubyte.flat, bins = 100, range = (0, 80)) # flat flattens 2D int 1D

# define segments
seg_one =  (denoise_ubyte < 55)# binay image where all the pixels are extracted from the denoise ubyte image
# and all are coming from gray level< 55
seg_two = (denoise_ubyte > 55) & (denoise_ubyte <= 100)
seg_three = (denoise_ubyte > 100) & (denoise_ubyte <= 200)
seg_four = (denoise_ubyte > 200)

segments = np.zeros((denoise_ubyte.shape[0], denoise_ubyte.shape[1], 3)) # creaate an image of same size of denoise image

# now fill one by one

segments[seg_one] = (1, 0, 0)
segments[seg_two] = (0, 0, 1)
segments[seg_three] = (1, 1, 0)
segments[seg_four] = (1, 0, 1)
plt.imsave("images/hist_segmented.jpg", segments)

# binary opening takes care of straight pixels, closing takes place of voids
seg_one_open = nd.binary_opening(seg_one, np.ones((3, 3)))
seg_one_close  = nd.binary_closing(seg_one_open, np.ones((3, 3)))

seg_two_open = nd.binary_opening(seg_two, np.ones((3, 3)))
seg_two_close  = nd.binary_closing(seg_two_open, np.ones((3, 3)))

seg_three_open = nd.binary_opening(seg_three, np.ones((3, 3)))
seg_three_close  = nd.binary_closing(seg_three_open, np.ones((3, 3)))

seg_four_open = nd.binary_opening(seg_four, np.ones((3, 3)))
seg_four_close  = nd.binary_closing(seg_four_open, np.ones((3, 3)))

seg_clean = np.zeros((denoise_ubyte.shape[0], denoise_ubyte.shape[1], 3))
seg_clean[seg_one_close] = (1, 0, 0)
seg_clean[seg_two_close] = (0, 0, 1)
seg_clean[seg_three_close] = (1, 1, 0)
seg_clean[seg_four_close] = (1, 0, 1)
plt.imsave("images/hist_segmented_clean.jpg", seg_clean)
