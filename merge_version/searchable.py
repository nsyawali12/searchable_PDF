import numpy
import easyocr
import pdf2image, img2pdf
import pytesseract
import cv2
import PIL
from PIL import Image
from fpdf import FPDF
import matplotlib.pyplot as plt
import glob

import os
from os import listdir
from os.path import isfile, join

from merger_pdf import merging_pdf_to_file


def image_conversion(inpath, image_path):
    print("Converting to image")
    OUTPUT_FOLDER = None
    FIRST_PAGE = None
    LAST_PAGE = None
    FORMAT = 'jpg'
    USERPWD = None
    USE_CROPBOX = False
    STRICT = False

    pil_images = pdf2image.convert_from_path(inpath,
                                             output_folder = OUTPUT_FOLDER,
                                             first_page=FIRST_PAGE,
                                             last_page=LAST_PAGE,
                                             userpw=USERPWD,
                                             use_cropbox=USE_CROPBOX,
                                             strict=STRICT)
    
    image_counter = 1

    for image in pil_images:
        filename = "img_homeland_" + str(image_counter) + ".jpg"
        image.save(image_path + filename)

        image_counter = image_counter + 1

# inpath coba data tanah

inpath = "inpath/data1.PDF" # ini harus nerima jadi inputan user
image_path = "image_path/" # image path tetep yang ini nnti masuk ke function
# image path bisa jadi disimpen di main.py


image_conversion(inpath, image_path)

""" Convert to PDF """

import cv2
import pytesseract

## directory cmd tergantung installing tesseract nya dimana

## directory bisa jadi disimpen di main.py juga
pytesseract.pytesseract.tesseract_cmd = 'C://Program Files//Tesseract-OCR//tesseract.exe'
TESSDATA_PREFIX = 'C://Program Files//Tesseract-OCR'
tessdata_dir_config = '--tessdata-dir "C://Program Files//Tesseract-OCR//tessdata"'

input_dir = image_path + "img_homeland_%d.jpg"
try_img = list(glob.glob(image_path + "*.jpg"))

def open_image(path):
    try:
        image = cv2.imread(path)
        return image
    except:
        return []

# print(len(try_img))

results = []
  
for img_name in try_img:
    img = open_image(img_name)
    # try_img.append(img)   

    res = pytesseract.image_to_pdf_or_hocr(img, lang="eng",
                                            config=tessdata_dir_config)
    result = bytearray(res)
    results.append(result)

# print(len(results))

pdf_counter = 0

for save_pdf in range(0, len(results)):
    pdf_filename = open("output_path/homeland_searchablePDF_" + str(pdf_counter) + ".pdf", "w+b")
    pdf_filename.write(results[save_pdf])
    pdf_filename.close()

    pdf_counter = pdf_counter + 1

path_to_pdf = "output_path/"
merging_pdf_to_file(path_to_pdf)