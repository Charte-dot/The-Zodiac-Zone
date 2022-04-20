from datetime import date
import time

print(r'***********************************************************')
print(r'____________________        ______________________  ______ ')
print(r'|___  /    \ |  \ | |   /\  | ___||___   /    \|  \ | | __| ')
print(r'   / /| /\ | ||\ \| |  /  \ | |       / /| /\ ||   \| | |_  ')
print(r'  / / | || | || | | | / /\ \| |      / / | || || |\ \ | __| ')
print(r' / /__| \/ | ||/ /| |/ ____ \ |__   / /__| \/ || | \  | |_  ')
print(r'/_____\____/ |_ / |_/_/    \_\____|/_____\____/|_|  \ |___| ')
print(r'************************************************************')
print("")
print("")
print("")

print('Welcome to The Zodiac Zone\n')
print('The place to find out you Zodiac sign\n')
print('And get a personalized horoscope for your sign\n')
print('Please enter you name to begin\n')
name = input()
print('Hello ' + name)
print('Please enter your day and month of Birth\n')

"""
This function only excepts numbers from user input
for date of birth
"""


def month(int):
    """
This function only excepts numbers from user input
for month of birth
"""
    while True:
        try:
            month = int(input)
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if month(int) not in range(1, 13):
            return False
            print("Sorry, your response must be a number between 1 and 12.")
            continue
        else:
            break
    return month


month = int(input("What is your Month of birth?:\n"))


def day(int):
    """
This function only excepts numbers from user input
for day of birth
"""
    while True:
        try:
            day = int(input)
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if day(int) not in range(1, 32):
            return False
            print("Sorry, your response must be a number between 1 and 31.")
            continue
        else:
            break
    return day


day = int(input("What is your day of birth?: [ex: 10]\n"))

print("")
print('Thank you! I will now consult the cosmos and return your Zodiac sign\n')

"""
Depending on user input, if/elif statement will calculate which
sign to display after user inputs date of birth
"""

if ((int(month) == 1 and int(day) >= 20)
        or (int(month) == 2 and int(day) <= 18)):
    sign = ("Aquarius")

elif ((int(month) == 2 and int(day) >= 19)
        or (int(month) == 3 and int(day) <= 20)):
    sign = ("Pisces")
elif ((int(month) == 3 and int(day) >= 21)
        or (int(month) == 4 and int(day) <= 19)):
    sign = ("Aries")
elif ((int(month) == 4 and int(day) >= 20)
        or (int(month) == 5 and int(day) <= 20)):
    sign = ("Taurus")
elif ((int(month) == 5 and int(day) >= 21)
        or (int(month) == 6 and int(day) <= 20)):
    sign = ("Gemini")
elif ((int(month) == 6 and int(day) >= 21)
        or (int(month) == 7 and int(day) <= 22)):
    sign = ("Cancer")
elif ((int(month) == 7 and int(day) >= 23)
        or (int(month) == 8 and int(day) <= 22)):
    sign = ("Leo")
elif ((int(month) == 8 and int(day) >= 23)
        or (int(month) == 9 and int(day) <= 22)):
    sign = ("Virgo")
elif ((int(month) == 9 and int(day) >= 23)
        or (int(month) == 10 and int(day) <= 22)):
    sign = ("Libra")
elif ((int(month) == 10 and int(day) >= 23)
        or (int(month) == 11 and int(day) <= 21)):
    sign = ("Scorpio")
elif ((int(month) == 11 and int(day) >= 22)
        or (int(month) == 12 and int(day) <= 21)):
    sign = ("Sagittarius")
elif ((int(month) == 12 and int(day) >= 22)
        or (int(month) == 1 and int(day) <= 19)):
    sign = ("Capricorn")

print("Calculating...\n")
time.sleep(1)
print("Consulting the cosmos...\n")
time.sleep(1)
print("Searching the stars...\n")
time.sleep(1)
print("Diving deep into the Zodiac...\n")
time.sleep(1)
print('Your zodiac sign is ...' " " + sign)
print("")
time.sleep(2)
print('Generating horoscope for' " " + sign)
