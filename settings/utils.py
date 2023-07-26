import random
import os
import json
import sys
from colorama import init, Fore, Style, Back

from .variables import *

#PARTS
from parts._checks import *


init(autoreset=True)

def clear():
    check()
    os.system('cls' if os.name=='nt' else 'clear')

def autosave_game():
    check()
    global version, health_max, level, progress, player, items, tools
    game_data = {
        "health_max": health_max,
        "level": level,
        "progress": progress,
        "player": player,
        "items": items,
        "tools": tools
        
    }
    with open("game_data.json", "w", encoding='utf-8') as f:
        json.dump(game_data, f, indent=4, ensure_ascii=False)


def load_game():
    global version, health_max, level, progress, player, items, tools
    clear()
    try:
        with open("game_data.json", "r", encoding='utf-8') as f:
            game_data = json.load(f)
            health_max = game_data['health_max']
            level = game_data['level']
            progress = game_data['progress']
            player = game_data['player']
            items = game_data['items']
            tools = game_data['tools']
            

        print(Fore.GREEN + "Игра загружена.")
        check()
    except FileNotFoundError:
        print(Fore.RED + "Файл сохранения не найден.")
        
    # main._profile.profile()

def die():
    check()
    autosave_game()
    input("Нажмите Enter, чтобы выйти из игры.")
    sys.exit()