from PyPDF2 import PdfFileMerger
import os 

path_to_pdf = "C:/Users/Wallsk/Documents/working-stuff/Projects/searchable_PDF/output_path/"

pdf_file = path_to_pdf + "homeland_searchablePDF_%d.pdf"

merger = PdfFileMerger()

for item in range(1, 4):
    items_pdf = pdf_file %item
    if items_pdf.endswith('.pdf'):
        merger.append(items_pdf)

merger.write("results_of_searchable.pdf")
merger.close()



