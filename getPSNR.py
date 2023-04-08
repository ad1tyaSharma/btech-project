import numpy as np

def getPSNR(imgA,imgB):
    # Compute the mean squared error between the original and processed images
    mse = np.mean((imgA - imgB) ** 2)
    
    # Compute the maximum pixel value of the image
    max_pixel = np.max(imgA)
    
    # Compute the PSNR
    psnr = 20 * np.log10(max_pixel / np.sqrt(mse))
    
    return psnr
