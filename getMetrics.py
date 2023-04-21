import numpy as np
import cv2
from skimage.metrics import mean_squared_error
from skimage.metrics import structural_similarity as ssim
import cv2
import numpy as np
from sewar import full_ref
from skimage import measure, metrics
"""
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

def getPSNR(imgA,imgB):
    return cv2.PSNR(imgA, imgB)

def mse(imgA, imgB):
    a = mean_squared_error(img1, img2)
    ssim_value = ssim(img1, img2, multichannel=True)
    ssim_value, _ = cv2.SSIM(img1, img2, full=True)
    vif_value = vif(img1, img2)
"""
def getMetrics(img1,img2):
    print(f'PSNR: {cv2.PSNR(img1, img2)}')
    print(f'MSE: {mean_squared_error(img1, img2)}')
    print(f'SSIM: {ssim(img1, img2, multichannel=True)}')
    print(f'VIF: {full_ref.vifp(img1, img2, sigma_nsq=2)}')