import os
import json
from flask import Flask, flash, request, redirect, url_for, jsonify, render_template, Response
from flask.helpers import make_response
from werkzeug.utils import  secure_filename, send_from_directory
import searchable
import merger_pdf
from searchable import searchable_preprocess, result_search
from merger_pdf import merging_pdf_to_file

UPLOAD_FOLDER = './upload'
ALLOWED_EXTENSIONS = set(['pdf','PDF'])

path_to_img_pdf = "output_path/"

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def pdf_to_searchable(filename_for_searchable):
    get_pdf_img = searchable_preprocess(filename_for_searchable)
    get_result_search = result_search(get_pdf_img)

    path_to_img_pdf = "output_path/"
    merge_each_img = merging_pdf_to_file(path_to_img_pdf)
    
    return merge_each_img

@app.route('/', methods=['GET'])
def search_merge_index():
    return render_template('webpages/merge_service.html')

@app.route('/api/merge_search', methods=['POST'])
def upload_file():
    print("proses sedang di upload")

    #check if the post request has file part
    try:
        print(request.files)
        print("request satu lancar")
    except Exception as e:
        print(e)
    
    # return "Gagal"

    if 'file' not in request.files:
          # flash('No file part')
          return "request 2 No file part"
          # print("sampai if 1 aman")
    file = request.files['file']

    # If the user does not select a file, the browser submits an
    # empty file without a filename.

    if file.filename == '':
        return "Filename salah"
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(file_path)

        searchable_file = pdf_to_searchable(file_path)
        print("Request ke 3 aman")

        respon_pdf = make_response(searchable_file)
        res_pdf = Response(respon_pdf, mimetype='application/pdf')
        res_pdf.headers["Content-Disposition"] = "attachment;filename=searchable_result.pdf"

        return res_pdf



    
