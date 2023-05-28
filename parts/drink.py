from variables import *
from colorama import init, Fore, Style, Back

import main_functions._clear_screen as _clear_screen
import main_functions._profile as _profile

init(autoreset=True)


def drink():
    global items, progress, player, tools
    _clear_screen.clear()
    if items["Вода"] < 10:
        print(Fore.RED + "Недастатично воды")
    elif items["Вода"] >= 10:
        if player["Жажда"] == 0:
            print(Fore.YELLOW + "Тебе ненужно пить")
        else:
            player["Жажда"] -= 10
            items["Вода"] -= 10
            print(Fore.LIGHTGREEN_EX + "Вы пьете воду и уменьшаете жажду")
    if player["Жажда"] < 0:
        player["Жажда"] = 0
    _profile.autosave_game()
    _profile.profile()