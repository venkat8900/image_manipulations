from PIL import Image

img = Image.open("images/one.jpg") # not an numpy array by default
img_2 = Image.open("images/two.jpg")

# resize
resize_img = img.resize((200, 300))
resize_img.save("images/one_resize.jpg")


img.thumbnail((200, 300)) # resizing in place, keeps the aspect ratio. It takes 200 and resizes accordingly. 
# it only looks at the width first and the resizes accordingly while maintaining aspect ratio.
img.save("images/one_thumbnail.jpg")
img_2.thumbnail((150,200))


# cropping
crop_img = img.crop((0, 0, 300, 300)) # start from (0, 0) to 300 pizels right and 300 pixels below 
crop_img.save("images/one_crop.jpg")

img_copy = img.copy()
img_copy.paste(img_2, (50, 50))
img_copy.save("images/pasted_img.jpg")

# rotations
img_90 = img.rotate(90) # at other angles, we might loose some part of image
img_90.save("images/one_rotate_90.jpg")

img_45 = img.rotate(45, expand = True) # we will not loose any pixels

img_flipL2R = img.transpose(Image.FLIP_LEFT_RIGHT)
img_flipL2R.save("images/one_flipL2R.jpg")


img_grey = img.convert("L")
img_grey.save("images/one_grey.jpg")


# automating to many images in folder.
import glob

path = "images/dogs/*"

for file in glob.glob(path):
	a = Image.open(file)
	rot_45 = a.rotate(45, expand = True)
	rot_45.save(file + "_rotated_45.png", "PNG")
	







