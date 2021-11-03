import numpy
import easyocr
import pdf2image, img2pdf
import pytesseract
import cv2
import PIL
from PIL import Image
from fpdf import FPDF
import matplotlib.pyplot as plt

from PyPDF2 import PdfFileMerger

import os
from os import listdir
from os.path import isfile, join


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
        
# inpat sample pdf
# inpath = "C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/inpath/sample.pdf"

# inpath coba data tanah

inpath = "C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/inpath/data1.PDF"
image_path = "C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/image_path/"
image_conversion(inpath, image_path)

""" Convert to PDF """

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = 'C://Program Files//Tesseract-OCR//tesseract.exe'
TESSDATA_PREFIX = 'C://Program Files//Tesseract-OCR'
tessdata_dir_config = '--tessdata-dir "C://Program Files//Tesseract-OCR//tessdata"'

input_dir = image_path + "img_homeland_%d.jpg"

def open_image(path):
    try:
        image = cv2.imread(path)
        return image
    except:
        return []

try_img = []
results = []

# range gambarnya ada 3 gambar, untuk percobaan sementara   
for i in range(1,4):
    img = open_image(input_dir % i)
    # try_img.append(img)

    res = pytesseract.image_to_pdf_or_hocr(img, lang="eng",
                                            config=tessdata_dir_config)
    result = bytearray(res)
    results.append(result)
# plt.imshow(try_img[0])
# plt.show()

# print(len(results))
# print(results[1])
# print(bytearray(results[1]))

# plt.imshow(results[0])
# plt.show()
    

# for res in try_img:
#     result = pytesseract.image_to_pdf_or_hocr(try_img[res], lang="eng",
#                                             config=tessdata_dir_config)
    
#     results.append(result)

# pdf1_filename = open("C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/output_path/homeland_searchablePDF.pdf", "w+b")

# im.save(pdf1_filename, "PDF" ,resolution=100.0, save_all=True, append_images=result_img)


f = open("C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/output_path/homeland_searchablePDF_1.pdf", "w+b")
f.write(results[0])
f.close()

g = open("C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/output_path/homeland_searchablePDF_2.pdf", "w+b")
g.write(results[1])
g.close()

h = open("C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/output_path/homeland_searchablePDF_3.pdf", "w+b")
h.write(results[2])
h.close()


# output_path = 'C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/output_path/'

# for each_file in listdir(output_path):
#     if isfile(join(output_path, each_file)):
#         pdf_path = os.path.join(output_path,each_file)
#         merger_path = os.path.join(output_path,each_file.rsplit('.', 1)[0]+'.pdf')
#         pdf_img = Image(pdf_path)
#         pdf_img.write(merger_path)

# with open("C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/output_path/homeland_searchablePDF.pdf", "w+b") as f:
#     for n in range(0, 3):
#         f.write(results[n])
