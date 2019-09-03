from PIL import Image

img = Image.open('d://1.jpg')
 
out_img = img.transpose(Image.FLIP_LEFT_RIGHT)

out_img.save("d://output.jpg", "JPEG")
