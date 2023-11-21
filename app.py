from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload-audio', methods=['POST'])
def upload_audio():
    if 'audio_data' not in request.files:
        return 'No audio data', 400
    file = request.files['audio_data']
    if file:
        filename = secure_filename(file.filename)
        save_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(save_path)
        
    return f'File saved at {save_path}'

if __name__ == '__main__':
    app.run(debug=True)
