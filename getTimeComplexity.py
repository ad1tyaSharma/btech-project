import cv2
import time
from he import he
from clahe import clahe
from DHE import dhe
import matplotlib.pyplot as plt
def getTimeComplexity(img,algo):
    times = []
    # Vary the size of the image and calculate the execution time for each size
    for i in range(100, 2000, 100):
        resized_img = cv2.resize(img, (i, i))
        start_time = time.time()
        equalized_img = algo(resized_img)
        end_time = time.time()
        times.append(end_time - start_time)
    
    # Plot the graph
    plt.plot(range(100, 2000, 100), times)
    plt.xlabel('Image Size')
    plt.ylabel('Execution Time (seconds)')
    plt.show()