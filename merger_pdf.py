from PyPDF2 import PdfFileMerger
import os 

def merging_pdf_to_file(path):

    pdf_file = path + "homeland_searchablePDF_%d.pdf"

    merger = PdfFileMerger()

    for item in range(1, 4):
        items_pdf = pdf_file %item
        if items_pdf.endswith('.pdf'):
            merger.append(items_pdf)

    merger.write("results_of_searchable.pdf")
    merger.close()

    return merger



