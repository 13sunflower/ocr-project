# 📷 OCR Text Extractor Web App

This Flask web app extracts text from uploaded images using Tesseract OCR. Users can upload any scanned image, and the extracted text is displayed instantly in a clean interface.

## 🚀 Features

- 🖼️ Upload image (.png, .jpg)
- 🔍 Extract printed text using Tesseract
- 💬 Display result in styled output
- 🌐 Simple, modern frontend using Bootstrap

## 🧠 Technologies Used

- Python 3
- Flask
- pytesseract
- Pillow (PIL)
- Bootstrap 5

## 📂 Folder Structure

```
ocr_text_extractor/
├── app.py
├── templates/
│   └── index.html
├── static/
│   └── uploads/
│       └── [uploaded images]
```

## 🛠️ How to Run

1. Clone the repo and navigate to `ocr_text_extractor`
2. Install dependencies:
   ```bash
   pip install flask pytesseract pillow
   ```
3. Install Tesseract:
   - **macOS**:  
     ```bash
     brew install tesseract
     ```
   - **Ubuntu**:  
     ```bash
     sudo apt install tesseract-ocr
     ```
4. (Optional) Set Tesseract path in `app.py`:
   ```python
   pytesseract.pytesseract.tesseract_cmd = "/opt/homebrew/bin/tesseract"
   ```
5. Start the app:
   ```bash
   python app.py
   ```
6. Visit: [http://127.0.0.1:5000](http://127.0.0.1:5000)

## ⚠️ Notes

- Works best with clear printed text (not handwriting)
- Only supports `.png` and `.jpg`
- PDF OCR requires a separate extension (can be added)

## 🙋‍♀️ Author

**Kashikaa Dhawan**  
Intern, Cantilever Labs  
[GitHub](https://github.com/kashikaadhawan)
