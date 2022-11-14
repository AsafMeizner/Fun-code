from PIL import Image
import os

absolute_path = os.path.dirname(__file__)
relative_path = "assets/logo.png"
full_path = os.path.join(absolute_path, relative_path)
img = Image.open(full_path)
img = img.convert("RGB")

d = img.getdata()

new_image = []
for item in d:

	# change all white (also shades of whites)
	# pixels to yellow
	if  item[0] in list(range(30, 40)) and item[1] in list(range(30, 40)) and item[2] in list(range(30, 40)):
		new_image.append((255, 224, 100))
	else:
		new_image.append(item)
		
# update image data
img.putdata(new_image)

# save new image
img.save("logo_new.jpg")
