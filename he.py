import cv2
def he(image):
    img_b, img_g, img_r = cv2.split(image)
    img_b =  cv2.equalizeHist(img_b)
    img_g = cv2.equalizeHist(img_g)
    img_r = cv2.equalizeHist(img_r)
    return cv2.merge((img_b, img_g, img_r))
#from matplotlib import pyplot as plt

image = cv2.imread('dataset/1.png')
img_he = he (image)

cv2.imshow("HE Image",img_he)
cv2.waitKey(0)
cv2.destroyAllWindows()