# from flask import
from flask import Flask,render_template,abort

import os
import json
app = Flask(__name__)

files_folder = os.path.join(os.path.dirname(__file__),'files')
@app.route('/')
def index():
    files = os.listdir(files_folder)
    files = [x.split(".")[0] for x in files]
    return  render_template("index.html",files=files)

@app.route('/files/<filename>')
def file(filename):
    try:
        with open(files_folder+"/"+filename+".json", 'r') as load_f:
            load_dict = json.load(load_f)
            detail = load_dict
            return render_template("detail.html", detail=detail)
    except FileNotFoundError:
        abort(404)

@app.errorhandler(404)
def not_found(error):
    return render_template("404.html"),404
if __name__ == '__main__':
    app.run()
