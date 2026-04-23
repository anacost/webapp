import os
from flask import Flask, render_template


app = Flask(__name__)
IMG_folder = os.path.join("static", "IMG")
app.config["UPLOAD_FOLDER"] = IMG_folder

@app.route('/')
def index():
    IMG_LIST = os.listdir("static/IMG")
    IMG_LIST = ["IMG/" + i for i in IMG_LIST]
    return render_template('index.html', imagelist=IMG_LIST)
    
@app.route('/cakes')
def cakes():
    return render_template('cakes.html')

if __name__ == '__main__':
    app.run(debug = True)
