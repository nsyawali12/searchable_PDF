import numpy
import easyocr
import pdf2image
import pytesseract
import cv2
import PIL

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


    for image in pil_images:
        image.save(image_path+'image_converted.jpg')

inpath = "C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/inpath/sample.pdf"
image_path = "C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/image_path/"
image_conversion(inpath, image_path)

""" Convert to PDF """

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files//Tesseract-OCR//tesseract.exe'
TESSDATA_PREFIX = 'C://Program Files//Tesseract-OCR'
tessdata_dir_config = '--tessdata-dir "C://Program Files//Tesseract-OCR//tessdata"'

input_dir = "C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/image_path/image_converted.jpg"

img = cv2.imread(input_dir, 1)

result = pytesseract.image_to_pdf_or_hocr(img, lang="eng",
                                            config=tessdata_dir_config)

f = open("C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/output_path/searchablePDF.pdf", "w+b")
f.write(bytearray(result))
f.close()