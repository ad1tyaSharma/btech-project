import numpy as np
import cv2
def getSNR(img):
    # Compute the mean and standard deviation of the image
    mean, std_dev = cv2.meanStdDev(img)
    # Compute the power of the signal
    signal_power = mean[0]**2
    # Compute the power of the noise
    noise_power = std_dev[0]**2
    # Compute the SNR
    snr = 10 * np.log10(signal_power / noise_power)
    return snr[0]

