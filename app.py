from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
import whisper
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

        # Process with Whisper for speech-to-text
        model = whisper.load_model("base")
        result = model.transcribe(save_path)
        transcription = result["text"]

        return f'Transcription: {transcription}'
    else:
        return 'No file uploaded', 400

if __name__ == '__main__':
    app.run(debug=True)
