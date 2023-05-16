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
import time
if __name__ == "__main__":
    # read image from dataset
    
    
    figure_size = 30
    plt.figure(figsize=(figure_size,figure_size))
    start_time = time.time()
    
    img = cv2.imread('dataset/6.png')
    plt.subplot(131),plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
    plt.title('Input Image',fontsize=35),plt.xticks([]),plt.yticks([])
    
    imgRef = cv2.imread('high/6.png')

    img = bilateralAndMedianFilter(img)
    
    heResult =  he(img)   
    claheResult = clahe(img)
   
    alpha = 0.8
    fusedImg = cv2.addWeighted(claheResult, alpha, heResult, 1 - alpha, 0) 

    white_balance=white_balance (fusedImg)
    end_time = time.time()
    print(f'Time taken: {end_time - start_time}')
    getMetrics(imgRef, white_balance)
    plt.subplot(132),plt.imshow(cv2.cvtColor(white_balance,cv2.COLOR_BGR2RGB))
    plt.title('After White CC & IS ',fontsize=35),plt.xticks([]),plt.yticks([])
    plt.subplot(133),plt.imshow(cv2.cvtColor(imgRef,cv2.COLOR_BGR2RGB))
    plt.title('Expected Output ',fontsize=35),plt.xticks([]),plt.yticks([])
    