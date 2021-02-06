from skimage import io
from matplotlib import pyplot as plt
from skimage.transform import rescale, resize, downscale_local_mean
from skimage.filters import roberts, sobel, scharr, prewitt

img = io.imread("images/one.jpg", as_gray = "True")

img_rescale = rescale(img, 1.0/4.0, anti_aliasing = "True") # recale by factor of 4

img_resize = resize(img, (220, 220)) # resize to 220 x 200

img_downscale = downscale_local_mean(img, (4,3)) # downscaling by 4 x 3 block, withing that block it is using mean value


# edge detection and deconvolution

edge_roberts = roberts(img)  # float 64
edge_sobel = sobel(img)
edge_scharr = scharr(img)
edge_prewitt = prewitt(img)

# canny edge detector -> found in skimage.feature module
from skimage.feature import canny # it does edge detection, noise reduction , gradient calculations
edge_canny = canny(img, sigma = 3)

# deconvolution -> requires original image, poiint spread function. It sharpens the image
from skimage import restoration
import numpy as np

psf = np.ones((3,3))/9 # 3 x 3 images with 9 ones
deconvolved, _ = restoration.unsupervised_weiner(img, psf) # point spread function define why we think image is blurred. its a matrix

# we can also use gaussian kernel for psf
import scipy.stats as st
def gkern(kernlen = 21, nsig =2):
	lim = kernlen//2 + (kernlen % 2)/2
	x = np.linspace(-lim, lim, kernlen + 1)
	kern1d = np.diff(st.norm.cdf(x))
	kern2d = np.outer(kern1d, kern1d)
	return kern2d/kern2d.sum()

psf = gkern(5,3)



plt.imshow(edge_canny)
plt.imsave("images/deconvolved.jpg", deconvolved, cmap = "gray")





