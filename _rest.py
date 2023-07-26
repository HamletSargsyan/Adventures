import random
import os
import json
import sys
from colorama import init, Fore, Style, Back

from variables import *
from utils import *

#PARTS
from _checks import *
from _craft import *
from _explore import *
from _lootbox import *
from _monster import *
from _rest import *
from _shop import *
from _eat import *
from _drink import *
from _profile import *

init(autoreset=True)

def rest():
    global items, progress, player, tools
    clear()
    health_gain = random.randint(5, 10)
    fatigue_reduction = random.randint(5, 15)
    player["Здоровие"] += health_gain
    player["Усталость"] -= fatigue_reduction
    print(Fore.LIGHTGREEN_EX + f"Вы отдыхаете и восстанавливаете {health_gain} здоровья и уменьшаете усталость на {fatigue_reduction}")
    print()
    if player["Усталость"] < 0:
        player["Усталость"] = 0
    if player["Здоровие"] > health_max:
        player["Здоровие"] = health_max
    autosave_game()
    profile()