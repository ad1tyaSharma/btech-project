import cv2
import numpy as np

# Load the original image
original_image = cv2.imread('original_image.png')

# Perform some processing or compression on the image
processed_image = ... # Replace with your processing or compression method

# Compute the mean squared error between the original and processed images
mse = np.mean((original_image - processed_image) ** 2)

# Compute the maximum pixel value of the image
max_pixel = np.max(original_image)

# Compute the PSNR
psnr = 20 * np.log10(max_pixel / np.sqrt(mse))

print('PSNR:', psnr)
