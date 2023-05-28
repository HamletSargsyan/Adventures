import random
from variables import *
from colorama import init, Fore, Style, Back

import main_functions._clear_screen as _clear_screen
import main_functions._profile as _profile

init(autoreset=True)


def rest():
    global items, progress, player, tools
    _clear_screen.clear()
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
    _profile.autosave_game()
    _profile.profile()