import pytesseract
from PIL import Image
import subprocess

import os
tesseract_cmd = 'tesseract.exe'
print(os.getcwd())
image = Image.open('D:/PythonSpider/1.jpg')
#text = pytesseract.image_to_string(image)
pytesseract.image_to_string(image)
#print(text)

def cleanFile():
    image = Image.open('2.jpg')
    image_new = image.point(lambda x:0 if x<143 else 255)
