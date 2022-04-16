import random
from datetime import date

print(r'______________________  ____  _____________________ ')
print(r'|__  _| | | | __|___   /    \ |  \ | |   /\   | ___|')
print(r' |  | | |_| | |_    / /| /\ | ||\ \| |  /  \  | |   ')
print(r' |  | | ___ | __|  / / | || | || | | | / /\ \ | |   ')
print(r' |  | | | | | |_  / /__| \/ | ||/ /| |/ ____ \| |__ ')
print(r' |__| |_| |_|___|/_____\____/ |_ / |_/_/    \_\____|\n')


print('Welcome to The Zodiac Zone\n')
print('The place to find out you Zodiac sign\n')
print('And get a personalized horoscope for your sign\n')
print('Please enter you name to begin\n')
name = input()
print('hello ' + name)
print('Please enter your Birthdate\n')

Year = input("What's your year of birth? [ex: 1980]\n")
Month = input("What's your month of birth? [ex: 10]\n")
Day = input("What's your day of birth? [ex: 01]\n")

print('Your Date of Birth is ', (Day + "/" + Month + "/" + Year))