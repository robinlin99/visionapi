import io
import os
import time
from os import listdir
from os.path import isfile, join
from PIL import Image

# Imports the Google Cloud client library
from google.cloud import vision
from google.cloud.vision import types

def classify():
	# Instantiates a client
	client = vision.ImageAnnotatorClient()
	# The name of the image file to annotate
	mypath = "/Users/robinlin/Desktop/Code/visionapi"
	onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
	jpg = []
	for i in onlyfiles:
		if ".jpg" in i:
			jpg.append(i)
	print(jpg)
	for i in jpg:
		file_name = os.path.abspath(i)
		# Loads the image into memory
		with io.open(file_name, 'rb') as image_file:
		    content = image_file.read()
		img = Image.open(i)
		img.show()
		img.close()
		time.sleep(1)
		image = types.Image(content=content)
		# Performs label detection on the image file
		response = client.landmark_detection(image=image)
		landmarks = response.landmark_annotations
		print(landmarks[0].description)
		print("Latitude")
		print(landmarks[0].locations[0].lat_lng.latitude)
		print("Longitude")
		print(landmarks[0].locations[0].lat_lng.longitude)
		print('-------------')
classify()