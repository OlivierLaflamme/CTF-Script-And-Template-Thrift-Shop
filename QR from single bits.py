#if i get QR code but single pxl make it scanable increase pxl size 

from PIL import Image

img = Image.open('NAMEIMAGE.png')
pixels = img.load()

(w,h) = img.size
outimg_b = Image.new('RGB', (outw,outh), "white")
pixels_b = outimg_b.load()

wout = -1
hout = -1
for i in range(1,w,6):
  wout += 1
  hout = -1
  for j in range(1,h,6):
    hout+=1
    (r,g,b) = pixels[i,j]
    if not b&1:
        pixels_b[wout,hout] = (0,0,0)

outimg_b = outimg_b.resize((10*outw,10*outh))
outimg_b.save("outimg_b.png")
