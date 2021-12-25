from typing import Counter
from PyPDF2 import PdfFileMerger
import os 

def merging_pdf_to_file(path):

    num_dir = os.listdir(path)
    num_files = len(num_dir)

    pdf_file = path + "homeland_searchablePDF_%d.pdf"

    merger = PdfFileMerger()

    for item in range(0, len(num_dir)):
        items_pdf = pdf_file %item
        if items_pdf.endswith('.pdf'):
            merger.append(items_pdf)

    merger.write("results_of_searchable.pdf")
    merger.close()

    return merger



