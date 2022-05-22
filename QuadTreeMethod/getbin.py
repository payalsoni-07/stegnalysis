import csv
import numpy as np
#read a csv file
k = 0
with open('stego.csv', 'r') as csvfile:
    #print data from file
    thereader = csv.reader(csvfile, delimiter=',')
    for row in thereader:
        r = format(int(row[0]),"b")
        g = format(int(row[1]),"b")
        b = format(int(row[2]),"b")
        with open('pixelBinRGB.txt','a',newline='') as f:
            f.write(r)
            f.write('\t')
            f.write(g)
            f.write('\t')
            f.write(b)
            f.write('\n')

        