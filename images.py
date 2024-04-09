from PIL import Image, ImageFilter

img = Image.open('large_image.jpg')

#new_img = img.resize((400,400))
new_img=img
new_img.thumbnail((400,400))
new_img.save("small_image.png",'png')
# img = Image.open('./Pokedex/pikachu.jpg')

# filtered_img = img.filter(ImageFilter.BLUR)

# filtered_img.save("blur.png", 'png')

# filtered_img2 = img.convert('L')
# filtered_img2.save("grey.png", 'png')

# #filtered_img.show()

# #filtered_img2.show()

# box = (100,100,400,400)
# region = filtered_img.crop(box)

# region.save("crop_pikachu.png",'png')

#region.show()
# filtered_img2.resize((300,300))
# filtered_img2.rotate(90)

