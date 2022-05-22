from PIL import Image
import csv
cover = Image.open('flowers.jpeg')
stego = Image.open('stegFlower.jpeg')
c = cover.load()
s = stego.load()
h = cover.height
w = cover.width
print(h,w)
with open('difference.csv', 'w', newline='') as csvfile:
    thewriter = csv.writer(csvfile, delimiter=',')
    thewriter.writerow(['x', 'y', 'cover', 'stego'])
    for x in range(w):
        for y in range(h):
            r = c[x,y][0]
            g = c[x,y][1]
            b = c[x,y][2]
            ci = [r, g, b]
            r1 = s[x,y][0]
            g1 = s[x,y][1]
            b1 = s[x,y][2]
            si = [r1, g1, b1] 
            if(si != ci):
                thewriter.writerow([x, y, ci, si])
