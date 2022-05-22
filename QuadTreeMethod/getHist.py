import matplotlib.pyplot as plt
import numpy as np
#plot diff.csv data into histogram
def getHist(fileName):
    data = np.loadtxt(fileName, delimiter=',')
    plt.hist(data, bins=100)
    plt.show()

getHist('diff.csv')