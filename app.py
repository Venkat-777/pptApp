from flask import Flask, render_template, request, send_file, redirect, url_for, send_from_directory
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from forms import MyForm
from pptFile import process_PPTfile
UPLOAD_FOLDER = '/Users/venkataneti/Desktop/pptApp/uploads'
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'pptx', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/hello', methods=["GET", "POST"])
def index():
    return "Hello!!!!"

@app.route('/', methods=["GET", "POST"])
def upload():
    fileForm = MyForm()
    if fileForm.validate_on_submit():
        uploadedFile = fileForm.file.data
        # Process and save the uploaded file
        processedFileName = process_PPTfile(uploadedFile)
        # Provide a download link for the user
        return redirect(url_for('download', processed_file_name=processedFileName))
    return render_template('upload.html', template_form=MyForm())

@app.route('/download/<processed_file_name>', methods=["GET"])
def download(processed_file_name):
    return render_template('download.html',filename=processed_file_name)
@app.route('/download_file/<processed_file_name>', methods=["GET"])
def download_file(processed_file_name):
    filename = processed_file_name
    return send_from_directory(app.config['UPLOAD_FOLDER'],
                               filename, as_attachment=True)

