from flask import Flask, render_template, request
from audio_downloader import download_audio

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    message = ''
    if request.method == 'POST':
        url = request.form.get('url')
        try:
            download_audio(url)
            message = "✅ Download completed successfully!"
        except Exception as e:
            message = f"❌ Error: {str(e)}"
    return render_template('index.html', message=message)

if __name__ == '__main__':
    app.run()
