from flask import Flask, render_template, request, redirect, flash
from audio_downloader import download_audio
import os

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Needed for flashing messages

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form.get('url')
        if url:
            try:
                download_audio(url)
                flash('✅ Download successful!', 'success')
            except Exception as e:
                flash(f'❌ Error: {str(e)}', 'error')
        else:
            flash('⚠️ Please enter a valid URL.', 'error')
        return redirect('/')
    return render_template('index.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
