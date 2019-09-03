#!/usr/bin/python

import cv2
import sys
import os

if len(sys.argv) == 1:
  print 'Usage:',sys.argv[0],'<filename>'
  exit()

directory = 'opencv_lsb_channels'

if not os.path.exists(directory):
    os.makedirs(directory)

img = cv2.imread(sys.argv[1])
height, width, channels = img.shape
print "Image contains "+str(channels)+" layers"
layers = cv2.split(img)
lay_no = 0;
for layer in layers:
  lay_no += 1;
  for mask in xrange(8):
    binmask = 1 << mask
    masked_layer = layer & binmask;
    ret,tresh = cv2.threshold(masked_layer,1,255,cv2.THRESH_BINARY)
    cv2.imwrite(directory+'/'+str(lay_no)+'-'+str(binmask)+'.png',tresh)
