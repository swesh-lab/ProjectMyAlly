import requests
import json
import time
import requests
from bs4 import BeautifulSoup


def newsHeadlines():
    myList = "I read today's top news headlines and they were "
    url = "http://newsapi.org/v2/top-headlines?country=in&apiKey=44ab7eef8ab842f58035edf16e209e3e"
    news = requests.get(url).text
    news_dict = json.loads(news)
    arts = news_dict["articles"]
    for i in range(4):
        myList += (arts[i]['title'] + "\n")
        myList += "\n"
    myList += (arts[4]['title'])
    return myList



def mainMethod(userText):
    response = userText
    if response == 'news':
       result = newsHeadlines()
       print(result)
    else:
       result = response

    return result
