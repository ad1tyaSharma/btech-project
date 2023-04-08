import cv2
def he(image):
    img_b, img_g, img_r = cv2.split(image)
    img_b =  cv2.equalizeHist(img_b)
    img_g = cv2.equalizeHist(img_g)
    img_r = cv2.equalizeHist(img_r)
    return cv2.merge((img_b, img_g, img_r))
