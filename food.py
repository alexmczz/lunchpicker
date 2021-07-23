import random
from tkinter import *
from os import system, name



foodchoice = [
    'Chik-Fil-A',
    'Dominos',
    'Mcdonalds',
    'KFC',
    'Popeyes',
    'Moes',
    'Taco Bell',
    'Burger King',
    'Sonic',
    'Five Guys',
    'Wendys'
    ]

def get_help():
    print("""
    Type 'Y' to get a singular choice
    Type 'TOF' to get 5 choices
    Type 'clear' to clear the console
    Type 'exit' to exit at any Time
    Type 'help' to see this message again
    """)

def three_outof_five():
    for i in range(0,5):
        print(random.choice(foodchoice)) 

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

def picker():
    while True:
        userchoice = input("Are you ready to start? Y|N? ")
        usrimp = userchoice.upper()
        if usrimp == 'Y':
            print(random.choice(foodchoice))
        elif usrimp == 'TOF':
            three_outof_five()
        elif usrimp == 'HELP':
            get_help()
        elif usrimp =='CLEAR':
            clear()
            continue
        elif usrimp == 'EXIT' or userchoice.upper() == 'N':
            break  
        else:
            print("Invalid input. Please Try again")
            continue



get_help()
picker()