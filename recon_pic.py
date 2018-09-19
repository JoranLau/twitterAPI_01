
import io
import os

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

# Instantiates a client
client = vision.ImageAnnotatorClient()

for x in range(1,11):
# The name of the image file to annotate
	file_name = '/media/sf_EC601_Product_Design/twitter_pics/%d.jpg'%x

# Loads the image into memory
	with io.open(file_name, 'rb') as image_file:
		content = image_file.read()

	image = types.Image(content=content)

# Performs label detection on the image file
	response = client.label_detection(image=image)
	labels = response.label_annotations

	f = open("/media/sf_EC601_Product_Design/twitter_pics/%drecog.txt"%x, "w")
	print(('pic%d_Labels:'%x+'\n'),file = f )
	for label in labels:
		print((label.description),file = f )
	print(('\n'),file = f)
	f.close()