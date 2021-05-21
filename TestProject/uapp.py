import requests
import json
from flask import jsonify
import main
from flask import Flask, render_template, url_for, request, redirect
import os


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return render_template("upload.html")


@app.route("/upload", methods=["POST"])
def upload():
    target = os.path.join(APP_ROOT, 'resource/')
    print(target)
    if not os.path.isdir(target):
            os.mkdir(target)

    for upload in request.files.getlist("file"):
        filename = upload.filename
        target_location = "/".join([target, filename])
        upload.save(target_location)

    display = "Your file " + filename + " is successfully uploaded!"
    return render_template("upload.html", result=display)


if __name__ == "__main__":
    app.run(debug=True)
