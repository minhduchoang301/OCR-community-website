from flask import Flask, jsonify, request
import os 
from flask_cors import CORS
from main import main

app = Flask(__name__)
CORS(app)

UPLOAD_FOLDER = '/Users/dl/Documents/OCR_Imgs'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        resp = jsonify({'message': 'No file part in the request'})
        resp.status_code = 400
        return resp 
    file = request.files['file']
    if file.filename == '':
        resp = jsonify({'message': 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    if file and allowed_file(file.filename):
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'file_uploaded'))
        result = main(os.path.join(UPLOAD_FOLDER, 'file_uploaded'), '/Users/dl/Desktop/OCR_Project/OCR-community-website/content/model')
        # result = jsonify({'message': 'Upload successfully'})
        return result
    else:
        resp = jsonify({'message': 'Allowed file types are png, jpg, jpeg'})
        resp.status_code = 400
        return resp

if __name__ == '__main__':
    app.run(port=3001, debug=True)