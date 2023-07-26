import random
import os
import json
import sys
from colorama import init, Fore, Style, Back

from settings.variables import *
from settings.utils import clear, autosave_game, load_game, die

#PARTS
from _checks import *
from _profile import *

init(autoreset=True)

def drink():
    global items, progress, player, tools
    clear()
    if items["Вода"] < 1:
        print(Fore.RED + "Недостатично воды")
    elif items["Вода"] >= 1:
        if player["Жажда"] == 0:
            print(Fore.YELLOW + "Тебе ненужно пить")
        else:
            player["Жажда"] -= 10
            items["Вода"] -= 1
            print(Fore.LIGHTGREEN_EX + "Вы пьете воду и уменьшаете жажду")
    if player["Жажда"] < 0:
        player["Жажда"] = 0
    autosave_game()
    profile()