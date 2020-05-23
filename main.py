from flask import Flask, render_template, request, redirect
import os
from werkzeug import secure_filename
from app import app
import CODE

@app.route('/')
def render_home():
   return render_template('home.html')

@app.route('/uploader', methods = ['POST'])
def upload_file():
    if request.method == 'POST':
        if "file" not in request.files:
            print('No file part')
            return redirect(request.url)
        file = request.files["file"]
    # if user does not select file, browser also
    # submit a empty part without filename
        if file.filename == '':
            print('No selected file')
            return redirect(request.url)
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        print("Save sucessfully!")
        src = "static/Uploads/" + filename
        print(src)
        if (CODE.detect(src) == None):
            so_bien_so = "Khon"
        return render_template('result.html', src = src, kq = so_bien_so)


if __name__ == '__main__':
   app.run(debug = True)