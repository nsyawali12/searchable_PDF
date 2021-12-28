import os
import json
from flask import Flask, flash, request, redirect, url_for, jsonify, render_template, Response
from werkzeug.utils import  secure_filename, send_from_directory
import main
import merger_pdf

UPLOAD_FOLDER = './upload'
ALLOWED_EXTENSIONS = set(['pdf','PDF'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
    
# Define main merger       