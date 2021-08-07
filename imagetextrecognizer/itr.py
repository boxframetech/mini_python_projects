import pytesseract
import os 
from PIL import Image

def imagerecognizer():
    img = Image.open('r.jpg')
    text = pytesseract.image_to_string(img)
    print(text)

imagerecognizer()