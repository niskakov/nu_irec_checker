from flask import Flask, render_template, request
from utils import analyze_docx
import os

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route("/", methods=["GET", "POST"])
def index():
    report = None
    if request.method == "POST":
        file = request.files["file"]
        if file and file.filename.endswith(".docx"):
            filepath = os.path.join(UPLOAD_FOLDER, file.filename)
            file.save(filepath)
            report = analyze_docx(filepath)
    return render_template("index.html", report=report)

if __name__ == "__main__":
    app.run(debug=True)
