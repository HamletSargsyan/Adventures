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

def eat():
    global items, progress, player, tools
    clear()
    if items["Еда"]["Яблоко"] < 10:
        print(Fore.RED + "Недостатично еды")
    elif items["Еда"]["Яблоко"] >= 10:
        if player["Голод"] == 0:
            print(Fore.YELLOW + "Ты уже сыт")
        else:
            player["Голод"] -= 10
            items["Еда"]["Яблоко"] -= 1
            print(Fore.LIGHTGREEN_EX + "Вы съедаете еду и уменьшаете голод")
    if player["Голод"] < 0:
        player["Голод"] = 0
    autosave_game()
    profile()