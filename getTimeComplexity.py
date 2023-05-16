import cv2
import time
from he import he
from clahe import clahe
from DHE import dhe
import matplotlib.pyplot as plt
from bilateralAndMedianFilter import bilateralAndMedianFilter
from white_balance import white_balance
def getTimeComplexity():
    img = cv2.imread('dataset/10.png')
    times = []
    # Vary the size of the image and calculate the execution time for each size
    for i in range(1, 10000, 100):
        resized_img = cv2.resize(img, (i, i))
        start_time = time.time()
        img = bilateralAndMedianFilter(img)
        
        heResult =  he(img)   
        claheResult = clahe(img)
       
        alpha = 0.8
        fusedImg = cv2.addWeighted(claheResult, alpha, heResult, 1 - alpha, 0) 

        white_balance (fusedImg)
        end_time = time.time()
        times.append(end_time - start_time)
    
    # Plot the graph
    plt.plot(range(1, 10000, 100), times)
    plt.xlabel('Image Size')
    plt.ylabel('Execution Time (seconds)')
    plt.title('Time complexity')
    plt.show()
#getTimeComplexity()
