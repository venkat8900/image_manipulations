import cv2
from skimage.restoration import denoise_nl_means, estimate_sigma
import numpy as np

img = cv2.imread("C:/Users/Venkat M/Desktop/images/random_walker/Alloy_noisy.jpg", 0)
# img_eq = cv2.equalizeHist(img)
# plt.hist(img.flat, bins = 100, range = (0, 255))
# plt.hist(img_eq.flat, bins = 100, range = (0, 255))

# denoising
# non local means filter
sigma_est = np.mean(estimate_sigma(img, multichannel = True))
nlm = denoise_nl_means(img, h = 1.15 * sigma_est, fast_mode = True, patch_size = 5,
                          patch_distance = 3, multichannel = True)

clahe = cv2.createCLAHE(clipLimit = 2.0, tileGridSize = (8, 8))
# apply this on image
clahe_img = clahe.apply(img)
# plt.hist(clahe_img.flat, bins = 100, range = (0, 255))


ret, thres_1 = cv2.threshold(clahe_img, 190, 150, cv2.THRESH_BINARY) #190 is threshold value, 150 is max value
# ret, thres_2 = cv2.threshold(clahe_img, 190, 255, cv2.THRESH_BINARY_INV)
# OTSU based thresholding to segment automatically
ret2, thres_3 = cv2.threshold(clahe_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU) # OTSU finds the best place to seperate


# cv2.imshow("Equalised", img_eq)
cv2.imshow("CLAHE Image", clahe_img)
cv2.imshow("threshold img", thres_1)
# cv2.imshow("threshold inv image", thres_2)
cv2.imshow("OTSU image", thres_3)

cv2.waitKey(0)
cv2.destroyAllWindows()
