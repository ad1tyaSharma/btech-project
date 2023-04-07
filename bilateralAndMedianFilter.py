import cv2
# Load the image
def bilateralAndMedianFilter(img):
    # Apply bilateral filter
    bilateral_filtered = cv2.bilateralFilter(image, 5, 50, 50)
    # Apply median filter to the bilateral-filtered image
    median_filtered = cv2.medianBlur(bilateral_filtered, 3)
    return median_filtered
# Display the original, bilateral-filtered, and median-filtered images side by side
image = cv2.imread('dataset/1.png')
filtered = bilateralAndMedianFilter(image)
cv2.imshow('Original Image', image)
cv2.imshow('Filtered Image', filtered)
cv2.waitKey(0)
cv2.destroyAllWindows()
