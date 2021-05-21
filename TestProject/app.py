import requests
import json
from flask import jsonify
import main
from flask import Flask, render_template, url_for, request, redirect


app = Flask(__name__)
app.secret_key = "myally"


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["nm"]
        date_month = request.form["dm"]
        session["username"] = username
        return render_template("index.html", result=username)
    else:
        return render_template("login.html")


@app.route('/')
def index():
    if "username" in session:
        username = session["username"]
        return render_template("index.html", result=username)
    else:
        return redirect(url_for("login"))


@app.route('/get')
def get_bot_response():
    userText = request.args.get('msg')
    return main.mainMethod(userText)
    # print(type(result))
    # return render_template('index.html', res=result)


if __name__ == "__main__":
    app.run(debug=True)
