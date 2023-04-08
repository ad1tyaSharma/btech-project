1#imports
import cv2
import matplotlib.pyplot as plt
from getMSE import getMSE
from getSNR import getSNR
from getPSNR import getPSNR
from getTimeComplexity import getTimeComplexity
#from wienerAndMedianFilter import wienerAndMedianFilter
from bilateralAndMedianFilter import bilateralAndMedianFilter
from he import he
from clahe import clahe
from DHE import dhe

def getEfficiencyParameters(imgA,imgB):
    print(f'SNR: {getSNR(imgB)}')
    print(f'MSE: {getMSE(imgA,imgB)}')
    print(f'PSNR: {getPSNR(imgA,imgB)}')

if __name__ == "__main__":
    # read image from dataset
    img = cv2.imread('dataset/3.png')
    print(f'SNR of input image is: {getSNR(img)}' )
    plt.imshow(img)
    choice1 = input("Enter 'yes' to apply denoising filter: ")
    if choice1 == 'yes':
        img = bilateralAndMedianFilter(img)
    figure_size = 20
    plt.figure(figsize=(figure_size,figure_size))
    heResult =  he(img)
    print("For HE")
    imgA = cv2.imread('dataset/1.png')
    getEfficiencyParameters( imgA, heResult)
    #getTimeComplexity(imgA, dhe)
    plt.subplot(1, 3, 1),plt.imshow(heResult)
    plt.title('HE Image'), plt.xticks([]), plt.yticks([])
    claheResult = clahe(img)
    
    print("For CLAHE")
    getEfficiencyParameters( imgA, claheResult)
    plt.subplot(1, 3, 2),plt.imshow(claheResult)
    plt.title('CLAHE Image'), plt.xticks([]), plt.yticks([])
    """
    dheResult = dhe(img)
    print("For DHE")
    getEfficiencyParameters( imgA, dheResult)
    plt.subplot(1, 3, 3),plt.imshow(dheResult)
    plt.title('DHE Image'), plt.xticks([]), plt.yticks([])
    """
