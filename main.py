#imports
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
from gamma_low import gamma_low
from white_balance import white_balance

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
        
    heResult =  he(img)
    print("For HE")
    imgA = cv2.imread('dataset/3.png')
    getEfficiencyParameters( imgA, heResult)
    #getTimeComplexity(imgA, dhe)
    #plt.subplot(3, 2, 1),plt.imshow(heResult)
    #plt.title('HE Image',fontsize=35), plt.xticks([]), plt.yticks([])
    
    claheResult = clahe(img)
    print("For CLAHE")
    getEfficiencyParameters( imgA, claheResult)
    #plt.subplot(3, 2, 2),plt.imshow(claheResult)
    #plt.title('CLAHE Image',fontsize=35), plt.xticks([]), plt.yticks([])
    
    dheResult = dhe(img)
    print("For DHE")
    getEfficiencyParameters( imgA, dheResult)
    #plt.subplot(1, 3, 3),plt.imshow(dheResult)
    #plt.title('DHE Image'), plt.xticks([]), plt.yticks([])
    
    figure_size = 30
    plt.figure(figsize=(figure_size,figure_size))
    
     #print("Gamma low with unmasking(HE)")
    gamma_he=gamma_low(heResult)
    plt.subplot(321),plt.imshow(gamma_he)
    plt.title('Gamma with unmasking(HE)',fontsize=35),plt.xticks([]),plt.yticks([])
    
    #print("White_balance with unmasking(HE)")
    white_balance_method_1=white_balance(heResult)
    plt.subplot(322),plt.imshow(white_balance_method_1)
    plt.title('White Balance with unmask(HE)',fontsize=35),plt.xticks([]),plt.yticks([])
    
    
    
    
    #print("Gamma low with unmasking with CLAHE")
    gamma_clahe=gamma_low(claheResult)
    plt.subplot(3,2,3),plt.imshow(gamma_clahe)
    plt.title('Gamma-unmasking with CLAHE',fontsize=35),plt.xticks([]),plt.yticks([])
    
    
    
    #print("White_balance with unmasking with CLAHE")
    white_balance_method=white_balance(claheResult)
    plt.subplot(3,2,4),plt.imshow(white_balance_method)
    plt.title('White Balance-unmask with CLAHE',fontsize=35),plt.xticks([]),plt.yticks([])
    
    #print("Gamma low with unmasking with DHE")
    gamma_clahe=gamma_low(dheResult)
    plt.subplot(3,2,5),plt.imshow(gamma_clahe)
    plt.title('Gamma-unmasking with DHE',fontsize=35),plt.xticks([]),plt.yticks([])
    
    
    #print("White_balance with unmasking with DHE")
    white_balance_method=white_balance(dheResult)
    plt.subplot(3,2,6),plt.imshow(white_balance_method)
    plt.title('White Balance-unmask with DHE',fontsize=35),plt.xticks([]),plt.yticks([])
    
   