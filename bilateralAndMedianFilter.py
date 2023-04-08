import cv2
# Load the image
def bilateralAndMedianFilter(img):
    # Apply bilateral filter
    bilateral_filtered = cv2.bilateralFilter(img, 5, 50, 50)
    # Apply median filter to the bilateral-filtered image
    median_filtered = cv2.medianBlur(bilateral_filtered, 3)
    return median_filtered
