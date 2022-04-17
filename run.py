import random
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


def Month():
    
    Month = int(input("What's your month of birth?: [ex: 10]\n"))
    

def Day():
    
    Day = int(input("What is the  day of birth?: [ex: 10]\n"))    


while True:
    try:
        Month = int(input("What's your month of birth?: [ex: 10]\n"))
        Day = int(input("What is the day of your birth?: [ex: 10]\n"))
        break
    except ValueError:
        print("Error please input numbers only...")
    continue

print("")
print('Thank you! I will now consult the cosmos and return your Zodiac sign\n')

"""
Depending on user input, if/elif statement will calculate which
sign to display after user inputs date of birth
"""

if ((int(Month) == 1 and int(Day) >= 20)
        or (int(Month) == 2 and int(Day) <= 18)):
    sign = ("Aquarius")

elif ((int(Month) == 2 and int(Day) >= 19)
        or (int(Month) == 3 and int(Day) <= 20)):
    sign = ("Pisces")
elif ((int(Month) == 3 and int(Day) >= 21)
        or (int(Month) == 4 and int(Day) <= 19)):
    sign = ("Aries")
elif ((int(Month) == 4 and int(Day) >= 20)
        or (int(Month) == 5 and int(Day) <= 20)):
    sign = ("Taurus")
elif ((int(Month) == 5 and int(Day) >= 21)
        or (int(Month) == 6 and int(Day) <= 20)):
    sign = ("Gemini")
elif ((int(Month) == 6 and int(Day) >= 21)
        or (int(Month) == 7 and int(Day) <= 22)):
    sign = ("Cancer")
elif ((int(Month) == 7 and int(Day) >= 23)
        or (int(Month) == 8 and int(Day) <= 22)):
    sign = ("Leo")
elif ((int(Month) == 8 and int(Day) >= 23)
        or (int(Month) == 9 and int(Day) <= 22)):
    sign = ("Virgo")
elif ((int(Month) == 9 and int(Day) >= 23)
        or (int(Month) == 10 and int(Day) <= 22)):
    sign = ("Libra")
elif ((int(Month) == 10 and int(Day) >= 23)
        or (int(Month) == 11 and int(Day) <= 21)):
    sign = ("Scorpio")
elif ((int(Month) == 11 and int(Day) >= 22)
        or (int(Month) == 12 and int(Day) <= 21)):
    sign = ("Sagittarius")
elif ((int(Month) == 12 and int(Day) >= 22)
        or (int(Month) == 1 and int(Day) <= 19)):
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
