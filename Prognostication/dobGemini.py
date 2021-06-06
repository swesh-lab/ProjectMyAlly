# "1. Aries
# "2. Taurus
# "3. Gemini
# "4. Cancer
# "5. Leo
# "6. Virgo
# "7. Libra
# "8. Scorpio
# "9. Sagittarius
# "10. Capricorn
# "11. Aquarius
# "12. Pisces


def zodiac_sign(day, month):
    if month == 'december':
        return 9 if (day < 22) else 10

    elif month == 'january':
        return 10 if (day < 20) else 11

    elif month == 'february':
        return 11 if (day < 19) else 12

    elif month == 'march':
        return 12 if (day < 21) else 1

    elif month == 'april':
        return 1 if (day < 20) else 2

    elif month == 'may':
        return 2 if (day < 21) else 3

    elif month == 'june':
        return 3 if (day < 21) else 4

    elif month == 'july':
        return 4 if (day < 23) else 5

    elif month == 'august':
        return 5 if (day < 23) else 6

    elif month == 'september':
        return 6 if (day < 23) else 7

    elif month == 'october':
        return 7 if (day < 23) else 8

    elif month == 'november':
        return 8 if (day < 22) else 9
