import cv2
import numpy as np
def gamma_low(claheResult):
 gamma = 1.5
 inv_gamma = 1.0 / gamma
 table = []
 for i in range(256):
    table.append(((i / 255.0) ** inv_gamma) * 255)
 table = np.array(table).astype("uint8")
 img_corrected = cv2.LUT(claheResult, table)

# Display the original and corrected images

 blurred = cv2.GaussianBlur(img_corrected, (3,3), 0)

# calculate the unsharp mask by subtracting the blurred image from the original image
 unsharp_mask = cv2.addWeighted(img_corrected, 1.5, blurred, -0.5, 0)
 return unsharp_mask
