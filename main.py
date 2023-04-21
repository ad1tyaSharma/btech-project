#imports
import cv2
import matplotlib.pyplot as plt
from getMetrics import getMetrics
from getTimeComplexity import getTimeComplexity
#from wienerAndMedianFilter import wienerAndMedianFilter
from bilateralAndMedianFilter import bilateralAndMedianFilter
from he import he
from clahe import clahe
from DHE import dhe
from gamma_low import gamma_low
from white_balance import white_balance
from ying import Ying

if __name__ == "__main__":
    # read image from dataset
    figure_size = 30
    plt.figure(figsize=(figure_size,figure_size))
    img = cv2.imread('dataset/2.png')
    plt.subplot(321),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.title('Input Image',fontsize=35),plt.xticks([]),plt.yticks([])
    imgRef = cv2.imread('high/22.png')

    img = bilateralAndMedianFilter(img)
    plt.subplot(322),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.title('Image after denoise',fontsize=35),plt.xticks([]),plt.yticks([])
    heResult =  he(img)   
    claheResult = clahe(img)
    plt.subplot(323),plt.imshow(cv2.cvtColor(claheResult,cv2.COLOR_BGR2RGB))
    plt.title('Image after CLAHE',fontsize=35),plt.xticks([]),plt.yticks([])
    alpha = 0.8
    fusedImg = cv2.addWeighted(claheResult, alpha, heResult, 1 - alpha, 0) 
    plt.subplot(324),plt.imshow(cv2.cvtColor(fusedImg,cv2.COLOR_BGR2RGB))
    plt.title('Image after fusion',fontsize=35),plt.xticks([]),plt.yticks([])
    
    """
    gammaResult=gamma_low(fusedImg)
    plt.subplot(325),plt.imshow(gammaResult)
    plt.title('After Gamma CC & IS ',fontsize=35),plt.xticks([]),plt.yticks([])
    """ 
    white_balance=white_balance(fusedImg)
    plt.subplot(325),plt.imshow(cv2.cvtColor(white_balance,cv2.COLOR_BGR2RGB))
    plt.title('After White CC & IS ',fontsize=35),plt.xticks([]),plt.yticks([])
    plt.subplot(326),plt.imshow(cv2.cvtColor(imgRef,cv2.COLOR_BGR2RGB))
    plt.title('Expected Output ',fontsize=35),plt.xticks([]),plt.yticks([])
    getMetrics(imgRef, white_balance)
        