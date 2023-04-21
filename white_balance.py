import cv2
import numpy as np



# Calculate the color balance using gray world algorithm
def white_balance(img):
 avg_color = np.average(img, axis=(0,1))
 grey_world_balance = np.array([124, 124, 124]) / avg_color

 # Apply the color balance to the image
 corrected_img = np.zeros_like(img)
 for i in range(3):
    corrected_img[:,:,i] = cv2.multiply(img[:,:,i], grey_world_balance[i])

 # Display the original and corrected image

 blurred = cv2.GaussianBlur(corrected_img, (3,3), 0)

# calculate the unsharp mask by subtracting the blurred image from the original image
 unsharp_mask = cv2.addWeighted(corrected_img, 1.5, blurred, -0.5, 0)
 return unsharp_mask
