from variables import *
from colorama import init, Fore, Style, Back

import main_functions._clear_screen as _clear_screen
import main_functions._profile as _profile

init(autoreset=True)


def eat():
    global items, progress, player, tools
    _clear_screen.clear()
    if items["Еда"]["Яблоко"] < 10:
        print(Fore.RED + "Недастатично еды")
    elif items["Еда"]["Яблоко"] >= 10:
        if player["Голод"] == 0:
            print(Fore.YELLOW + "Ты уже сыт")
        else:
            player["Голод"] -= 10
            items["Еда"]["Яблоко"] -= 10
            print(Fore.LIGHTGREEN_EX + "Вы съедаете еду и уменьшаете голод")
    if player["Голод"] < 0:
        player["Голод"] = 0
    _profile.autosave_game()
    _profile.profile()