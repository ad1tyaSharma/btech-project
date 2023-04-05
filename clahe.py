import cv2
def clahe(image):
    img_b, img_g, img_r = cv2.split(image)
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
    img_b = clahe.apply(img_b)
    img_g = clahe.apply(img_g)
    img_r = clahe.apply(img_r)
    return cv2.merge((img_b, img_g, img_r))
    
image = cv2.imread('dataset/1.png')
img_clahe = clahe (image)

cv2.imshow("CLAHE Image",img_clahe)
cv2.waitKey(0)
cv2.destroyAllWindows()