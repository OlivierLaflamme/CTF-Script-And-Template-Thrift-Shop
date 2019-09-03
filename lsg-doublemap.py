#coding:utf-8

import Image
import random

img1 = Image.open("00000000.png")
im1 = img1.load()

img2 = Image.open("00003754.png")
im2 = img2.load()


a=0
i=0
s=''

for x in range(img1.size[0]):
    for y in range(img1.size[1]):
        if(im1[x,y]!=im2[x,y]):
            print im1[x,y],im2[x,y]
            print im2[x,y][0]
            if i == 8:
                s=s+chr(a)
                a=0
                i=0

            a=im2[x,y][0]+a*2
            i=i+1

s=s+'}'
print s
