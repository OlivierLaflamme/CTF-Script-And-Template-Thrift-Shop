#!/usr/bin/python

import cv2
import sys
import os

if len(sys.argv) == 1:
  print 'Usage:',sys.argv[0],'<filename>'
  exit()

directory = 'opencv_single_channels'

if not os.path.exists(directory):
    os.makedirs(directory)

img = cv2.imread(sys.argv[1])
height, width, channels = img.shape
print "Image contains "+str(channels)+" layers"
layers = cv2.split(img)
lay_no = 0;
for layer in layers:
  lay_no = lay_no+1;
  for i in xrange(255):
    ret,tresh = cv2.threshold(layer,i,255,cv2.THRESH_BINARY)
    tresh_new = tresh
    if i > 0:
      tresh = tresh-old_tresh
    cv2.imwrite(directory+'/'+str(lay_no)+'-'+str(i)+'.png',tresh_new)
    old_tresh = tresh_new
