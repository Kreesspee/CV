from flask import Flask
import os
from flask import render_template
from flask import url_for, send_from_directory


app = Flask(__name__)

def get_path():
    path = os.path.abspath(__file__)
    path = os.path.dirname(path)
    path = os.path.join(path, "files")
    return path


@app.route("/")
def main():
    return render_template("main.html", name=None)


@app.route("/about")
def about():
    return render_template("about.html", name=None)


@app.route("/social")
def social():
    return render_template("social.html", name=None)


@app.route("/download")
def download():
    path = get_path()
    file_lst = os.listdir(path)
    url = url_for("download", _external=True)
    return render_template("investigations.html", file_list=file_lst, url=url)


@app.route("/download/<file_name>")
def download_file(file_name):
    path = get_path()
    return send_from_directory(path, file_name)


if __name__ == '__main__':
    app.run(debug=True)
