import numpy
import easyocr
import pdf2image
import pytesseract
import cv2

def  image_conversion(inpath, image_path):
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
                                             userpw=USERPWD
                                             use_cropbox=USE_CROPBOX,
                                             strict=STRICT)


    for image in pil_images:
        images.save(image_path+'image_converted.jpg')

inpath = "C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/inpath"
image_path = "D:/My-Blog/Blog-1/image_path/"
image_conversion(inpath, image_path)

""" Convert to PDF """

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files//Tesseract-OCR//tesseract.exe'
TESSDATA_PREFIX = 'C://Program Files//Tesseract-OCR'
tessdata_dir_config = '--tessdata-dir "C://Program Files//Tesseract-OCR//tessdata"'

input_dir = "D:/My-Blog/Blog-1/image_path/image_converted.jpg"