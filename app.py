import datetime
import pytz
import Main
import os
from flask import Flask, render_template, url_for, request, redirect, session
import pdftotext
import PyPDF2
import pyttsx3
import aiml
from Prognostication import BirthZodiac
from urllib.request import urlopen
from bs4 import BeautifulSoup

app = Flask(__name__)
app.secret_key = "myally"

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
FOLDER_PATH = APP_ROOT + "\\resource"
AUDIO_PATH = APP_ROOT + "\\static\\PDF_Audio_Collections"

kernel = aiml.Kernel()
kernel.learn("AIML Files//std-startup.xml")
kernel.respond("load aiml b")


@app.route('/login', methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["nm"]
        date = request.form["dd"]
        month = request.form["mm"]
        session["username"] = username
        session["date"] = date
        session["month"] = month
        BirthZodiac.date = date
        BirthZodiac.month = month
        kernel.setPredicate('name', username)
        return redirect(url_for("home"))
    else:
        return render_template("login.html")


@app.route('/')
def index():
    if "date" in session:
        return redirect(url_for("home"))
    else:
        return redirect(url_for("login"))


@app.route("/home")
def home():
    username = session["username"]
    date = session["date"]
    month = session["month"]
    IST = pytz.timezone('Asia/Kolkata')
    hour = int(datetime.datetime.now(IST).hour)
    if hour >= 0 and (hour < 12):
        greet = "Good Morning"

    elif hour >= 12 and (hour < 18):
        greet = "Good Afternoon"

    else:
        greet = "Good Evening"
    return render_template("index.html", username=username, greet=greet, date=date, month=month)


@app.route("/uploadPDF")
def pdf():
    return render_template('pdf_reader.html', fileName="")


@app.route("/uploadPDF", methods=["POST"])
def uploadPDF():
    target = os.path.join(APP_ROOT, 'resource/')
    audioadd = os.path.join(APP_ROOT, 'static\music\\')
    audioFileList = os.listdir(AUDIO_PATH)
    print(target)
    print(audioadd)
    if not os.path.isdir(target):
            os.mkdir(target)

    for upload in request.files.getlist("file"):
        filename = upload.filename
        target_location = "/".join([target, filename])
        upload.save(target_location)

    display = "Your file " + filename + " is successfully uploaded!"
    return render_template("pdf_reader.html", result=display, audioFileList=audioFileList, audioadd=audioadd)



@app.route("/uploadPDF", methods=["POST"])
def uploadPDF():
    target = os.path.join(APP_ROOT, 'resource\PDF')
    # print(target)
    if not os.path.isdir(target):
            os.mkdir(target)

    for upload in request.files.getlist("file"):
        filename = upload.filename
        target_location = "/".join([target, filename])
        upload.save(target_location)

    result = ""
    with open("resource/PDF/" + filename, "rb") as f:  # open the file in reading (rb) mode and call it f
        pdf = pdftotext.PDF(f)  # store a text version of the pdf file f in pdf variable

    for text in pdf:
        result += text

    engine = pyttsx3.init()
    audiofile=filename.replace(".pdf","")+".mp3"
    # path= AUDIO_PATH+audiofile
    path = os.path.dirname(os.path.abspath(__file__))+"\\static\\PDF_Audio_Collections\\"
    audioPath=path+audiofile
    engine.save_to_file(result, audioPath)
    engine.runAndWait()

    display = "Your file " + filename + " is successfully uploaded!"
    audioFileList = os.listdir(path)
    # for audiofile in audiofile:
    #     print(audiofile) FOLDER_PATH+{{\\audioFile}}
    AUDIO_PATH="file:///"+FOLDER_PATH+audiofile
    return render_template("pdf_reader.html", result=display,audioFile=audiofile,folderPath=FOLDER_PATH,fileName="",audioFileList=audioFileList)



@app.route("/uploadWebArticle")
def webArticle():
    return render_template('web_article_reader.html', fileName="")
    # https://www.zdnet.com/article/what-is-ai-everything-you-need-to-know-about-artificial-intelligence/
    # url = 'http://webhome.auburn.edu/~vestmon/Gift_of_the_Magi.html'


@app.route("/uploadWebArticle", methods=["POST"])
def uploadWebArticle():
    url = request.form.get("url")
    fileName = request.form.get("file-name")+".mp3"
    html = urlopen(url).read()
    soup = BeautifulSoup(html, features="html.parser")
    for script in soup(["script", "style"]):
        script.extract()
    text = soup.get_text()
    print(text)

    engine = pyttsx3.init()
    path = os.path.dirname(os.path.abspath(__file__)) + "\\static\\Articles_Audio_Collections\\"
    audioPath = path + fileName
    engine.save_to_file(text, audioPath)
    engine.runAndWait()
    display = "Your file " + fileName + " is successfully uploaded!"
    articleFileList = os.listdir(path)
    return render_template("web_article_reader.html", result=display, folderPath=FOLDER_PATH, fileName=fileName,
                           articleFileList=articleFileList)


@app.route("/get")
def getBotResponse():
    userQuery = request.args.get('msg')
    aimlResponse = kernel.respond(userQuery)
    name = kernel.getPredicate('assist')
    print(name)
    kernel.setPredicate('assist', "")
    return Main.mainMethod(aimlResponse, name)


if __name__ == "__main__":
    app.run(debug=True)
