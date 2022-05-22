import numpy as np
import cv2 as cv
import os
import matplotlib.pyplot as plt
from operator import add
from functools import reduce
import csv 
img = cv.imread('stegFlower.jpeg') #picture  name should be written
try:
    os.remove('difference.csv')
except OSError:
    pass
def split4(image):
    half_split = np.array_split(image, 2)
    res = map(lambda x: np.array_split(x, 2, axis=1), half_split)
    return reduce(add, res)
def concatenate4(north_west, north_east, south_west, south_east):
    top = np.concatenate((north_west, north_east), axis=1)
    bottom = np.concatenate((south_west, south_east), axis=1)
    return np.concatenate((top, bottom), axis=0)

def calculate_mean(img):
    return np.mean(img, axis=(0, 1))

def checkEqual(myList):
    first=myList[0]
    return all((x==first).all() for x in myList)

class QuadTree:
    
    def insert(self, img, level = 0):
        self.level = level
        self.mean = calculate_mean(img).astype(int)  
        self.resolution = (img.shape[0], img.shape[1])
        self.final = True
        if not checkEqual(img):
            split_img = split4(img)
            self.final = False
            self.north_west = QuadTree().insert(split_img[0], level + 1)
            self.north_east = QuadTree().insert(split_img[1], level + 1)
            self.south_west = QuadTree().insert(split_img[2], level + 1)
            self.south_east = QuadTree().insert(split_img[3], level + 1)
            self.nwm = self.north_west.mean
            self.nem = self.north_east.mean
            self.swm = self.south_west.mean
            self.sem = self.south_east.mean
            self.r = (self.nwm[0]+self.nem[0]+self.swm[0]+self.sem[0])//4
            self.g = (self.nwm[1]+self.nem[1]+self.swm[1]+self.sem[1])//4
            self.b = (self.nwm[2]+self.nem[2]+self.swm[2]+self.sem[2])//4
            self.final_mean = [self.r,self.g,self.b] 
            flag = 0
            for x in range(2):
                if(self.mean[x] == self.final_mean[x]):
                    flag = 1
                else:
                    flag = 0
                    break
            if(flag == 1):
                with open('difference.csv', 'a', newline='') as csvfile:
                    thewriter = csv.writer(csvfile,delimiter=',')
                    thewriter.writerow(self.mean)
            
        return self
    def get_image(self, level):
        if(self.final or self.level == level):
            return np.tile(self.mean, (self.resolution[0], self.resolution[1], 1))
        
        return concatenate4(
            self.north_west.get_image(level), 
            self.north_east.get_image(level),
            self.south_west.get_image(level),
            self.south_east.get_image(level))
   
    
quadtree = QuadTree().insert(img)

plt.imshow(quadtree.get_image(5))
plt.show()
