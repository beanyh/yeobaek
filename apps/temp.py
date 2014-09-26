from flask import Flask, render_template, request, redirect, url_for
from pytesseract import *
from StringIO import StringIO

app = Flask(__name__)
text = ""
ALLOWED_EXTENSIONS = ['jpg', 'png', 'jpeg', 'gif', 'tif']

def allowed_file(filename):
    return '.' in filename.lower() and filename.lower().rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/")
def index():
    return render_template('main.html', text = text)

@app.route('/write', methods=['GET', 'POST'])
def write():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filestream = file.read()
            im = Image.open(StringIO(filestream))
            text = image_to_string(im)
            return render_template('main.html', text = text)
    return render_template("write.html")


@app.route("/search", methods=['GET','POST'])
def search():
    return render_template('search.html', text = text)


if __name__ == "__main__":
    app.run(debug=True)