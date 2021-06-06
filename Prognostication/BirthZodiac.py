from Prognostication.dobGemini import zodiac_sign
from Prognostication.apiZodiac import horoscope

date = 0
month = ""
flag = 0
def prognostication():
    global flag
    if flag == 0:
        gemini = zodiac_sign(int(date), month)
        horoscope_text = horoscope(gemini, "today")

        horoscope_text = horoscope_text.replace("May 25, 2021 - ", "")
        prefix = "As per today's date, "
        flag = 1
        return prefix+horoscope_text
    else:
        return ""
