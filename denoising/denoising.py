from skimage import io, img_as_float # for image processing make sure you import img as float
from scipy import ndimage as nd
from matplotlib import pyplot as plt
from skimage.restoration import denoise_nl_means, estimate_sigma
import numpy as np

img = img_as_float(io.imread("images/noisy_images/noisy_img.jpg"))
img_gaus = nd.gaussian_filter(img, sigma = 3) # image gets blurred and edges are not preserved
# however, noise is removed
plt.imsave("images/noisy_images/Gaussian.jpg", img_gaus)

img_med = nd.median_filter(img, size = 3) # size is the size of kernel
plt.imsave("images/noisy_images/median.jpg", img_med) 
# median filter preserved edges.

# denoising
# non local means filter
sigma_est = np.mean(estimate_sigma(img, multichannel = True))
nlm = denoise_nl_means(img, h = 1.15 * sigma_est, fast_mode = True, patch_size = 5,
                          patch_distance = 3, multichannel = True)
# edeges is preserved, noise is removed
# when we use fast_mode = True/False we cannot tell the difference
# fast_mode = True is faster
plt.imsave("images/noisy_images/nlm.jpg", nlm) 