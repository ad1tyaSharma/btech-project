import numpy as np
import cv2

# Load the image
image = cv2.imread('dataset/3.png',0)

# Compute the mean and standard deviation of the image
mean, std_dev = cv2.meanStdDev(image)

# Compute the power of the signal
signal_power = mean[0]**2

# Compute the power of the noise
noise_power = std_dev[0]**2

# Compute the SNR
snr = 10 * np.log10(signal_power / noise_power)

print('SNR:', snr)
