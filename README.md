# voicebridge
a website for converting text to speech and speech to text
# 🎙️ VoiceBridge – Text ↔ Speech Converter

A simple and powerful web application that converts **Text to Speech (TTS)** and **Speech to Text (STT)** using Python and Flask, with a clean and modern user interface.

---

## 🚀 Features

* 🔊 Convert text into natural speech
* 🎤 Convert speech (audio file) into text
* 💻 Beautiful and responsive web interface
* ⚡ Fast and lightweight Flask backend
* 📁 Simple project structure (beginner-friendly)

---

## 🛠️ Tech Stack

* **Frontend:** HTML, CSS, JavaScript
* **Backend:** Python (Flask)
* **Libraries Used:**

  * `gTTS` (Google Text-to-Speech)
  * `SpeechRecognition`
  * `pydub`

---

## 📁 Project Structure

```
voicebridge/
│
├── app.py
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── outputs/
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```
git clone https://github.com/your-username/voicebridge.git
cd voicebridge
```

---

### 2️⃣ Install Dependencies

```
pip install flask gtts SpeechRecognition pydub
```

---

### 3️⃣ (Important) Install FFmpeg

Speech processing may require FFmpeg.

* Download: https://ffmpeg.org/download.html
* Add FFmpeg to system PATH

---

### 4️⃣ Run the Application

```
python app.py
```

---

### 5️⃣ Open in Browser

```
http://127.0.0.1:5000
```

---

## 🧪 How to Use

### 🔊 Text → Speech

1. Enter text in the input box
2. Click **Convert & Play**
3. Audio will be generated and played

### 🎤 Speech → Text

1. Upload a `.wav` audio file
2. Click **Upload & Convert**
3. Converted text will be displayed

---

## ⚠️ Notes

* Use `.wav` format for best speech recognition results
* Ensure microphone/audio is clear for accurate conversion
* Internet connection is required (Google API)

---

## 🌟 Future Enhancements

* 🎙️ Live microphone input (real-time speech recognition)
* 🌍 Multi-language support (Telugu, Hindi, etc.)
* 🎨 Dark/Light mode toggle
* 🤖 AI voice assistant integration
* 📊 Audio waveform visualization

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork this repository and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

* Google Text-to-Speech (gTTS)
* SpeechRecognition Library
* Flask Framework

---

## 👨‍💻 Author

**Bhanu Prasad**
📧 bhanuprasadlattupally@gmail.com

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
