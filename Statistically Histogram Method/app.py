import cv2 as cv
import matplotlib.pyplot as plt
import numpy 
fig = plt.figure(figsize=(10, 10))
#reading images
cover = cv.imread('cover.jpg')
stego = cv.imread('pic.jpeg')

#plotting 1st sub plot as cover image
fig.add_subplot(3, 2, 1)
plt.imshow(cover)
#plotting 1st sub plot as stego image
fig.add_subplot(3, 2, 2)
plt.imshow(stego)
#plotting 1st sub plot as cover histogram
fig.add_subplot(3, 2, 3)
# calculate mean value from RGB channels and flatten to 1D array
vals = cover.mean(axis=2).flatten()
# plot histogram with 255 bins
values, bins, patches = plt.hist(vals, 255)
areaCover = sum(numpy.diff(bins)*values)
#plotting 1st sub plot as stego histogram
fig.add_subplot(3, 2, 4)
vals = stego.mean(axis=2).flatten()
values, bins, patches=plt.hist(vals, 255)
areaStego = sum(numpy.diff(bins)*values)

# calculating statistics
mc = cover.mean() #mean of cover image
ms = stego.mean() #mean of stego image
sds = stego.std() #standard deviation of stego image
sdc = cover.std() #standard deviation of cover image
print("mean of cover: ",mc)
print("mean of stego: ",ms)
print("std of cover: ",sdc)
print("std of stego: ",sds)
print("Area of Cover: ",areaCover)
print("Area of Stego: ",areaStego)
plt.show()