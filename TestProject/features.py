from typing import List, Any

import requests
import json
import os
import sys
import time
import datetime
import subprocess
from datetime import datetime
import pytz
import random
import numpy as np
import webbrowser
from urllib.request import urlopen
from bs4 import BeautifulSoup
from flask import Flask, render_template, url_for, request, redirect
import pyttsx3


def wordMeaningDefinition(response):
    myList = []
    word = requests.get(response).text
    word_dict = json.loads(word)
    meanings = word_dict[0]["meanings"]
    i = 1
    for definition in meanings:
        for defi in definition['definitions']:
            i += 1
            myList.append(defi['definition'])

    print(myList)
    return myList


def newsHeadlines():
    myList = []

    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=44ab7eef8ab842f58035edf16e209e3e"
    # news = requests.get(url).text
    # news_dict = json.loads(news)
    # arts = news_dict["articles"]
    news = requests.get(url)
    data = news.json()
    # for i in range(4):
    #     myarticles = arts[i]
    #     myList.append(myarticles['title'])
    #
    # myList.append(arts[4]['title'])
    # print(myList)
    # return myList
    get_news = ''
    for i in range(5):
        title = data["articles"][i]["title"]
        description = data["articles"][i]["description"]
        link = data["articles"][i]["url"]
        get_news += "*" + title + " :* _" + description + "_ \n" + "\n\n"

    return get_news
    # print(get_news)





def searchQueriesAndVideos(response):
    webbrowser.open("https://google.com/search?q="+response)
    webbrowser.open("https://youtube.com/results?search_query="+response)
    return "There you go"


def mainMethod(query):
    result = None
    if query == 'meaning':
       result = wordMeaningDefinition(query)
    elif query == 'news':
        result = "here it goes"
    elif query == 'search':
       result = searchQueriesAndVideos(query)
    else:
        print("END")
