from flask import Flask, request, jsonify, send_from_directory, render_template
from elevenlabs.client import ElevenLabs
from elevenlabs import save
import os
import time
from pydub import AudioSegment
import subprocess  # For checking FFmpeg

app = Flask(__name__)

# Configure upload folder
UPLOAD_FOLDER = os.path.join(os.getcwd(), "export")
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def check_ffmpeg():
    try:
        subprocess.run(["ffmpeg", "-version"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
        return True
    except:
        return False

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-audio', methods=['POST'])
def generate_audio():
    data = request.json
    api_key = data.get('apiKey')
    voice_name_or_id = data.get('voice')
    text = data.get('text')

    if not check_ffmpeg():
        return jsonify({
            'success': False,
            'message': "FFmpeg not found. Please install FFmpeg and add it to PATH."
        }), 500

    try:
        client = ElevenLabs(api_key=api_key)
        timestamp = str(int(time.time()))
        output_mp3 = os.path.join(UPLOAD_FOLDER, f"output_{timestamp}.mp3")
        output_wav = os.path.join(UPLOAD_FOLDER, f"output_{timestamp}.wav")

        audio = client.generate(text=text, voice=voice_name_or_id)
        save(audio, output_mp3)

        # Convert MP3 to WAV
        AudioSegment.from_mp3(output_mp3).export(output_wav, format="wav")

        return jsonify({
            'success': True,
            'mp3_url': f'/export/output_{timestamp}.mp3',
            'wav_url': f'/export/output_{timestamp}.wav',
            'message': 'Audio generated successfully'
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'message': str(e)
        }), 500

@app.route('/export/<filename>')
def serve_export(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

if __name__ == '__main__':
    if not check_ffmpeg():
        print("⚠️ Warning: FFmpeg not found. WAV conversion will fail.")
    app.run(debug=True, port=5000)