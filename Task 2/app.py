from flask import Flask, render_template, request
import pytesseract
from PIL import Image
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# For Windows (uncomment if needed)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted_text = ""
    image_path = None

    if request.method == 'POST':
        if 'image' not in request.files:
            return render_template('index.html', error="No file part")

        file = request.files['image']
        if file.filename == '':
            return render_template('index.html', error="No selected file")

        if file:
            filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(filepath)
            image_path = filepath

            image = Image.open(filepath)
            extracted_text = pytesseract.image_to_string(image)

    return render_template('index.html', text=extracted_text, image_path=image_path)

if __name__ == '__main__':
    app.run(debug=True)
