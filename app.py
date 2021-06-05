import imghdr
import os
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from werkzeug.utils import secure_filename
import extract_zip as ez
import compare_util as cu
import zipfile


app = Flask(__name__)
app.config['MAX_CONTENT_LENGTH'] = 2 * 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'uploads'


@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_PATH'])
    return render_template('index.html', files=files)

@app.route('/', methods=['POST'])
def upload_files():
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
    return '', 204

@app.route('/uploads/<filename>')
def upload(filename):
    return send_from_directory(app.config['UPLOAD_PATH'], filename)
    
@app.route('/extract')
def imported_task():
    ez.extract_zip('uploads/client.zip')
    cu.startpy()
    create_zip()
    return send_file('client_data_compared.zip', as_attachment=True)

def get_all_file_paths(directory):
    file_paths = []
    for root, directories, files in os.walk(directory):
        for filename in files:
            filepath = os.path.join(root, filename)
            file_paths.append(filepath)
    return file_paths   

def create_zip():
    directory = 'results'
    file_paths = get_all_file_paths(directory)
    print('Following files will be zipped:')
    for file_name in file_paths:
        print(file_name)
    with zipfile('client_data_compared.zip','w') as zip:
        for file in file_paths:
            zip.write(file)
    print('All files zipped successfully!')

if __name__ == '__main__':
    app.run(debug=True)

