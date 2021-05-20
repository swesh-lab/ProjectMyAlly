import requests
import json
from flask import jsonify
import main
from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)



@app.route('/')
def index():
    return render_template("index.html", result="")


@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    return main.mainMethod(userText)
    # print(type(result))
    # return render_template('index.html', res=result)


if __name__ == "__main__":
    app.run(debug=True)
