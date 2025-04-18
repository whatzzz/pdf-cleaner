from flask import Flask, render_template, request, send_file, abort
import os
from utils import remove_blank_pages, remove_specified_pages, parse_pages
from werkzeug.utils import secure_filename
from cleaner import start_cleanup_timer
from urllib.parse import quote

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# 设置允许上传的文件类型
ALLOWED_EXTENSIONS = {'pdf'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# 固定的复杂路径
SECRET_PATH = "cleaner-xyuiox1892yz123"

@app.route(f"/{SECRET_PATH}", methods=["GET"])
def home():
    return render_template("index.html")

@app.route(f"/{SECRET_PATH}/clean_auto", methods=["POST"])
def clean_auto():
    if 'file' not in request.files:
        return "没有文件部分", 400
    file = request.files["file"]
    if file.filename == '':
        return "没有选择文件", 400
    if not allowed_file(file.filename):
        return "只允许上传 PDF 文件", 400

    original_filename = file.filename
    safe_filename = secure_filename(original_filename)
    filepath = os.path.join(UPLOAD_FOLDER, safe_filename)
    file.save(filepath)

    cleaned_path = remove_blank_pages(filepath)
    cleaned_name = original_filename.replace(".pdf", "_cleaned.pdf")
    encoded_name = quote(cleaned_name)

    response = send_file(cleaned_path, as_attachment=True)
    response.headers["Content-Disposition"] = f"attachment; filename*=UTF-8''{encoded_name}"
    return response

@app.route(f"/{SECRET_PATH}/clean_manual", methods=["POST"])
def clean_manual():
    if 'file' not in request.files:
        return "没有文件部分", 400
    file = request.files["file"]
    if file.filename == '':
        return "没有选择文件", 400
    if not allowed_file(file.filename):
        return "只允许上传 PDF 文件", 400

    page_input = request.form["pages"]

    original_filename = file.filename
    safe_filename = secure_filename(original_filename)
    filepath = os.path.join(UPLOAD_FOLDER, safe_filename)
    file.save(filepath)

    pages_to_delete = parse_pages(page_input)
    cleaned_path = remove_specified_pages(filepath, pages_to_delete)

    cleaned_name = original_filename.replace(".pdf", "_manual_cleaned.pdf")
    encoded_name = quote(cleaned_name)

    response = send_file(cleaned_path, as_attachment=True)
    response.headers["Content-Disposition"] = f"attachment; filename*=UTF-8''{encoded_name}"
    return response

if __name__ == "__main__":
    start_cleanup_timer(UPLOAD_FOLDER)
    print(f"/{SECRET_PATH}")
    app.run(host="0.0.0.0", port=8912)
