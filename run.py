import os
import random
import time
from datetime import date
from random import randint


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

first = [
        "Today is perfect for new endeavors.",
        "Today is the day to cherish and embrace others.",
        "The tensions of this week will feel heavier today than yesterday.",
        "Making yourself useful is a main component of a successful day.",
        "Today, exercise caution when crossing the street.\n"]

second = [
        "Remember that good things come to those who work hard. ",
        "Dont let the circumstances bring you down."
        "Patience is key, but sometimes a little push can get the job done.",
        "A smile can get you a long way.\n"]

third = [
        "Looking ahead may seem like a waste, but it pays off in the end.",
        "Luck favors those who mind the risks and take them. ",
        "Today is the day for that thing you always wanted to do. ",
        "Luck is on your side today, so seize it! ",
        "Things are looking up for you!\n"]

color = [
        "Red", "Green", "Orange", "White", "Black", "Purple", "Silver",
        "Brown", "Gray", "Pink", "Cream", "Gold", "Teal", "Navy Blue",
        "Turquoise", "Amber", "Mint"]

star = [
        "An Aries", "A Taurus", "A Gemini", "A Cancer", " A Leo", "A Virgo",
        "A Libra", " A Scorpio", "A Sagittarius", "A Capricorn", "An Aquarius",
        "A Pisces"]


def month():
    """
This function only excepts numbers from user input
for month of birth
"""
    while True:
        try:
            month = int(input("What is your month of birth?[eg.10]\n"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if month not in range(1, 13):
            print("Sorry, your response must be a number between 1 and 12.")
            continue
        else:
            break
    return month


month = month()

# month = int(input("What is your month of birth?\n"))


def day():
    """
This function only excepts numbers from user input
for day of birth
"""
    while True:
        try:
            day = int(input("What is your day of birth?:[eg.12]\n"))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if day not in range(1, 32):
            print("Sorry, your response must be a number between 1 and 31.")
            continue
        else:
            break
    return day


day = day()

print("")
print('Thank you! I will now consult the cosmos and return your Zodiac sign\n')
time.sleep(3)
os.system('cls||clear')


def sign(day, month):

    """
    Depending on user input, if/elif statement will calculate which
sign to display after user inputs date of birth
"""
# returns Aquarius if user input is within month and day parameters

    if ((int(month) == 1 and int(day) >= 20)
            or (int(month) == 2 and int(day) <= 18)):
        sign = ("Aquarius")

    # returns Pisces if user input is within month and day parameters
    elif ((int(month) == 2 and int(day) >= 19)
            or (int(month) == 3 and int(day) <= 20)):
        sign = ("Pisces")

    # displays Aries if user input is within month and day parameters
    elif ((int(month) == 3 and int(day) >= 21)
            or (int(month) == 4 and int(day) <= 19)):
        sign = ("Aries")

    # displays Taurus if user input is within month and day parameters
    elif ((int(month) == 4 and int(day) >= 20)
            or (int(month) == 5 and int(day) <= 20)):
        sign = ("Taurus")

    # displays Gemini if user input is within month and day parameters
    elif ((int(month) == 5 and int(day) >= 21)
            or (int(month) == 6 and int(day) <= 20)):
        sign = ("Gemini")

    # displays Cancer if user input is within month and day parameters
    elif ((int(month) == 6 and int(day) >= 21)
            or (int(month) == 7 and int(day) <= 22)):
        sign = ("Cancer")

    # displays Leo if user input is within month and day parameters
    elif ((int(month) == 7 and int(day) >= 23)
            or (int(month) == 8 and int(day) <= 22)):
        sign = ("Leo")

    # displays Virgo if user input is within month and day parameters
    elif ((int(month) == 8 and int(day) >= 23)
            or (int(month) == 9 and int(day) <= 22)):
        sign = ("Virgo")

    # displays Libra if user input is within month and day parameters
    elif ((int(month) == 9 and int(day) >= 23)
            or (int(month) == 10 and int(day) <= 22)):
        sign = ("Libra")

    # displays Scorpio if user input is within month and day parameters
    elif ((int(month) == 10 and int(day) >= 23)
            or (int(month) == 11 and int(day) <= 21)):
        sign = ("Scorpio")

    # displays Sagittarius if user input is within month and day parameters
    elif ((int(month) == 11 and int(day) >= 22)
            or (int(month) == 12 and int(day) <= 21)):
        sign = ("Sagittarius")

    # displays Capricorn if user input is within month and day parameters
    elif ((int(month) == 12 and int(day) >= 22)
            or (int(month) == 1 and int(day) <= 19)):
        sign = ("Capricorn")

    # count down display
    print("Calculating...\n")
    time.sleep(1)
    print("Consulting the cosmos...\n")
    time.sleep(1)
    print("Searching the stars...\n")
    time.sleep(1)
    print("Diving deep into the Zodiac...\n")
    time.sleep(2)
    print('Your zodiac sign is ...' " " + sign)
    print("")
    time.sleep(2)
    print('Generating horoscope for' " " + sign)
    time.sleep(4)
    print("")


sign(day, month)

# Current date calculator
today = date.today()
date = today.strftime("%d/%m/%Y")

# Print random generated horoscope
print(
    "Your Horoscope for:\n", date,
    random.choice(first), random.choice(second),
    random.choice(third))

print("")
time.sleep(2)

# prints  6 random generated lotto numbers
print("You Lucky Lotto numbers for your sign are...\n")

lotto = random.sample(range(0, 48), 6)
print(lotto)

print("")
time.sleep(2)

# prints lucky color
print(
    "Your luck color for today is....\n",
    random.choice(color))

print("")
time.sleep(2)


# prints a sign to for user to get to know
print(
    "The sign to get flirty with today is...\n",
    random.choice(star))
time.sleep(5)
print("Would you like another Horoscope?")


def replay():
    
    """
    asks player if they want to play again. If yes, program restarts,
    if no program exits
"""
