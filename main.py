1#imports
import cv2
import matplotlib.pyplot as plt
from getMSE import getMSE
from getSNR import getSNR
from wienerAndMedianFilter import wienerAndMedianFilter
from bilateralAndMedianFilter import bilateralAndMedianFilter
from he import he
from clahe import clahe
from DHE import dhe
def getEfficiencyParameters(imgA,imgB):
    mse = getMSE()

def denoise(img):
    choice1 = input("Enter 1 for Wiener filter or 2 for bilateral filter: ")
    if choice1 == 1:
        img = wienerAndMedianFilter(img)
    else: 
        img = bilateralAndMedianFilter(img)
    return img
if __name__ == "__main__":
    # read image from dataset
    img = cv2.imread('dataset/1.png')
    print(f'SNR of input image is: {getSNR(img)}' )
    plt.imshow(img)
    choice1 = input("Enter 'yes' to apply denoising filter: ")
    if choice1 == 'yes':
        img = denoise(img)
    figure_size = 10
    plt.figure(figsize=(figure_size,figure_size))
    heResult =  he(img)
    print(getSNR(heResult))
    plt.subplot(1, 3, 1),plt.imshow(heResult)
    plt.title('HE Image'), plt.xticks([]), plt.yticks([])
    claheResult = clahe(img)
    plt.subplot(1, 3, 2),plt.imshow(claheResult)
    plt.title('CLAHE Image'), plt.xticks([]), plt.yticks([])
    dheResult = dhe(img)
    plt.subplot(1, 3, 3),plt.imshow(dheResult)
    plt.title('DHE Image'), plt.xticks([]), plt.yticks([])

