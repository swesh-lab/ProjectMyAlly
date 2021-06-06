import os
import random
import requests
import json
import webbrowser
import subprocess
from datetime import datetime
import pytz
import wikipedia
from Prognostication import BirthZodiac

def wordMeaningDefinition(aimlResponse):
    randomList = ["So you want to know the meaning of this word.\n",
          "Well then let me tell you what does this word mean.\n",
          "Here is the explanation of the word you asked for.\n",
          "Well, you can define this word in this way.\n",
          "This is the definition of the word.\n"]
    result = randomList[random.randint(0, 4)]
    word = requests.get(aimlResponse).text
    word_dict = json.loads(word)
    meanings = word_dict[0]["meanings"]
    i = 1
    for definition in meanings:
        for defi in definition['definitions']:
            i += 1
            result += defi['definition']+"\n"
    return result

                      
def newsHeadlines():
    randomList = ["Well, a lot has been happening in the world. Here are the top news headlines for you.\n",
                  "So, you are looking for some world news. Well, here you go!\n",
                  "Well, here are the top news headlines for you.\n",
                  "These are some top news headlines for you. Hope it helps. \n"]
    result = randomList[random.randint(0, 3)]
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=44ab7eef8ab842f58035edf16e209e3e"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict["articles"]
    for i in range(5):
        result += arts[i]['title']+"\n"
    return result


def searchQueriesAndVideos(aimlResponse):
    result = ""
    webbrowser.open("https://google.com/search?q="+aimlResponse)
    webbrowser.open("https://youtube.com/results?search_query="+aimlResponse)
    result += "I have searched your query in both google and youtube."+"\n"
    return result


def reminder():
    result = ""
    subprocess.call('explorer.exe shell:Appsfolder\Microsoft.WindowsAlarms_8wekyb3d8bbwe!App')
    result += "Now you can set it"+"\n"
    return result


def currentTime():
    result = ""
    IST = pytz.timezone('Asia/Kolkata')
    now = datetime.now(IST)
    current_time = now.strftime("%I:%M %p")
    result += 'It is '+current_time+"\n"
    return result


def openYoutube():
    result = ""
    webbrowser.open('youtube.com')
    result += "There you go"+"\n"
    return result


def openGoogle():
    result = ""
    webbrowser.open('google.com')
    result += "There you go"+"\n"
    return result


def openCalculator():
    result = ""
    subprocess.call('calc.exe')
    result += "There you go"+"\n"
    return result


def openNotepad():
    result = ""
    subprocess.call('notepad.exe')
    result += "There you go"+"\n"
    return result


def music():
    result = ""
    music_loc = "C://Users//HP//Music//Playlists"
    music_list = os.listdir(music_loc)
    print(music_list)
    # randomSong=random.randint(0,4)
    os.startfile(os.path.join(music_loc, music_list[2]))
    result += "Sure, I hope you will enjoy this song..."
    return result


def searchWikipedia(aimlResponse):
    result = ""
    try:
        result += "According to Wikipedia, "+wikipedia.summary(aimlResponse, sentences=2)+"\n"
    except:
        result = "There are so many meanings. Wikipedia is confused. Please be more specific or you can see it on google which I have opened in next tab.\nSorry for inconvenience \n"
        webbrowser.open_new("https://google.com/search?q=" + aimlResponse)

    return result


def quotes():
    quote = requests.get("http://quotes.rest/qod.json?category=inspire")
    data = quote.json()
    result = data["contents"]["quotes"][0]["quote"]
    return result


def noAssistance(aimlResponse):
    result = str(aimlResponse)+"\n"
    print(result)
    return result


def mainMethod(aimlResponse, name):
    if name == 'meaning':
       botResponse = wordMeaningDefinition(aimlResponse)
    elif name == 'news':
       botResponse=newsHeadlines()
    elif name == 'search':
       botResponse = searchQueriesAndVideos(aimlResponse)
    elif name == 'reminder':
       botResponse = reminder()
    elif name == 'current time':
       botResponse = currentTime()
    elif name == 'open youtube':
       botResponse = openYoutube()
    elif name == 'open google':
       botResponse=openGoogle()
    elif name == 'open calculator':
       botResponse=openCalculator()
    elif name == 'open notepad':
       botResponse=openNotepad()
    elif name == 'wikipedia':
       botResponse = searchWikipedia(aimlResponse)
    elif name == 'quote':
       botResponse = quotes()
    elif name == 'foretell':
       botResponse = BirthZodiac.prognostication()
       if botResponse == "":
           return "I told you before. Hope you remember!"
    elif name == 'play music':
       botResponse = music()
    else:
       botResponse = noAssistance(aimlResponse)
    # print(botResponse)
    return botResponse
