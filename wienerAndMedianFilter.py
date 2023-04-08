import cv2
# Load the image
def wienerAndMedianFilter(img):
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

    # Split the YUV image into its three components
    y, u, v = cv2.split(img_yuv)

    # Apply Wiener filter to the Y component
    y_filtered = cv2.filter2D(y, -1, np.ones((3, 3))/9)

    # Merge the filtered Y component with the original U and V components
    img_yuv_filtered = cv2.merge((y_filtered, u, v))

    # Convert the filtered image back to the BGR color space
    img_filtered = cv2.cvtColor(img_yuv_filtered, cv2.COLOR_YUV2BGR)
    median_filtered = cv2.medianBlur(img_filtered, 5)
    return median_filtered

