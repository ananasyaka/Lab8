from PIL import Image
img = Image.open('pic1.jpeg')
print(img.size)
im_crop = img.crop((0,548,736,1096))
im_crop.show()
im_crop.save('cropped_pic1.jpg')