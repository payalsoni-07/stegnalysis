import main
import cv2  as cv
import os
import cv2
import os
import csv
import glob
num = 0
#path to frames folder
for img in glob.glob(r"C:\Users\user 1\Desktop\Intern\Project\videoAnalysis\frames\*.jpg"):
    #write text in a file
    with open('pixels.csv', 'a', newline='') as csvfile:
        thewriter = csv.writer(csvfile,delimiter=' ')
        thewriter.writerow("frame"  + str(num))
        
    cv_img = cv2.imread(img)
    main.QuadTree().insert(cv_img)
    num = num + 1
    