import requests
from dobGemini import zodiac_sign
from apiZodiac import horoscope

if __name__ == "__main__":
    print("Prognostication Test \n")
    # dob, month = input().split(maxsplit=1)
    dob, month = [x for x in input("May I know your date and month you born in?  ").split()]
    gemini = zodiac_sign(int(dob), month)
    print(dob, month)
    print("Choose some day:", "yesterday\t", "today\t", "tomorrow\t")
    day = input("day you wish to know: ")
    horoscope_text = horoscope(gemini, day)
    print(horoscope_text)

