import random
import os
import json
import sys
from colorama import init, Fore, Style, Back

from main import *  #FIXME
from variables import * #FIXME
from utils import * #FIXME

#PARTS
from _craft import *
from _explore import *
from _lootbox import *
from _monster import *
from _rest import *
from _shop import *
from _eat import *
from _drink import *

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
    _profile.profile()