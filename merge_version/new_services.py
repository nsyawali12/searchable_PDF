import os
import json
from re import search
from cv2 import merge
from flask import Flask, flash, request, redirect, url_for, jsonify, render_template, Response
from flask.helpers import make_response
from werkzeug.utils import  secure_filename, send_from_directory
from werkzeug.wrappers import response
import searchable
import merger_pdf
from searchable import searchable_preprocess, result_search
from merger_pdf import merging_pdf_to_file
import PyPDF2
from PyPDF2 import PdfFileMerger

UPLOAD_FOLDER = './upload'
ALLOWED_EXTENSIONS = set(['pdf','PDF', 'jpg', 'png'])

path_to_img_pdf = "output_path/"

app = Flask(__name__, template_folder='web_merge')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def pdf_to_searchable(filename_for_searchable):
    get_pdf_img = searchable_preprocess(filename_for_searchable)
    get_result_search = result_search(get_pdf_img)

    path_to_img_pdf = "output_path/"
    # merge_each_img = merging_pdf_to_file(path_to_img_pdf)
    
    # return merge_each_img
    return get_result_search

@app.route('/', methods=['GET'])
def search_merge_index():
    return render_template('merge_service.html')

@app.route('/api/merge_search', methods=['POST'])
def upload_file():
    print("proses sedang di upload")

    #check if the post request has file part
    try:
        print(request.files)
        print("request satu lancar")
    except Exception as e:
        print(e)
    
    if 'file' not in request.files:
        return "request 2 fail, No file in part"
    
    file = request.files['file']

    if file.filename == '':
        return "Filename salah"

    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        do_pdf_to_searchable = pdf_to_searchable(file_path)

        # now = timezone.now()

        print("request ke 3 aman")

        print('Goes Merging')

        num_dir = os.listdir(path_to_img_pdf)
        num_files = len(num_dir)

        pdf_file = path_to_img_pdf + "homeland_searchablePDF_%d.pdf"

        merger = PdfFileMerger()

        for item in range(0, len(num_dir)):
            items_pdf = pdf_file %item
            if items_pdf.endswith('.pdf'):
                merger.append(items_pdf)
        
        # result_merger = 'search_result.pdf'

        # response = make_response(merger.write(result_merger))
        # response.headers["Content-Disposition"] = "attachment;filename=search_result.pdf"
        # response.headers.set('Content-Type', 'application/pdf')
        
        respon_pdf = merger.write('searchable_result.pdf')
        response = Response(respon_pdf, content_type='application/pdf')
        response.headers["Content-Disposition"] = "attachment;filename=searchable_pdf.pdf"

        # merger.write(response)
        merger.close()

        print("Request PDF Searchable aman")

        return response

app.run()