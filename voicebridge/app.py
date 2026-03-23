from flask import Flask, render_template, request, jsonify, send_file
from gtts import gTTS
import speech_recognition as sr
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# Ensure outputs folder exists
if not os.path.exists("outputs"):
    os.makedirs("outputs")

# ---------------- TEXT TO SPEECH ----------------
@app.route('/tts', methods=['POST'])
def tts():
    try:
        data = request.get_json()
        text = data.get('text', '')

        if text.strip() == '':
            return jsonify({'error': 'No text provided'})

        tts = gTTS(text=text, lang='en')
        output_path = "outputs/audio.mp3"
        tts.save(output_path)

        return send_file(output_path, mimetype="audio/mpeg")

    except Exception as e:
        return jsonify({'error': str(e)})

# ---------------- SPEECH TO TEXT ----------------
@app.route('/stt', methods=['POST'])
def stt():
    try:
        if 'audio' not in request.files:
            return jsonify({'text': 'No file uploaded'})

        file = request.files['audio']

        recognizer = sr.Recognizer()

        with sr.AudioFile(file) as source:
            audio = recognizer.record(source)

        text = recognizer.recognize_google(audio)
        return jsonify({'text': text})

    except Exception as e:
        return jsonify({'text': f'Error: {str(e)}'})

# ---------------- HOME ----------------
@app.route('/')
def home():
    return render_template('index.html')

# ---------------- RUN ----------------
if __name__ == '__main__':
    app.run(debug=True)