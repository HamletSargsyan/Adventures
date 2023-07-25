import random
import os
import json
import sys
from colorama import init, Fore, Style, Back

from main import _start_menu, _profile
from variables import *
from utils import clear, autosave_game, load_game, die

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

init(autoreset=True)

def fight():
    global items, progress, player, tools
    progress_count = random.uniform(5.0, 7.0)
    progress += progress_count
    clear()
    print(Fore.LIGHTYELLOW_EX + "Вы вступаете в бой с монстром!")
    if tools["Меч"]["Количество"] == 0:
        damage_taken = random.randint(10, 20)
        coin_count  = random.randint(10, 20)
        food_count  = random.randint(10, 20)
        player["Здоровие"] -= damage_taken
        items["Монеты"] += coin_count
        items["Еда"]["Яблоко"] += food_count
        autosave_game()
        print(Fore.YELLOW + f"Вы теряете {damage_taken} здоровья")
        print(Fore.LIGHTGREEN_EX + f"Вы получили {coin_count} ед. монет и {food_count} ед. еды")
        print()
        _profile.profile()
    elif tools["Меч"]["Количество"] >= 0:
        damage_taken = random.randint(5, 10)
        coin_count  = random.randint(20, 30)
        food_count  = random.randint(20, 30)
        player["Здоровие"] -= damage_taken
        items["Монеты"] += coin_count
        items["Еда"]["Яблоко"] += food_count
        tools["Меч"]["Прочность"] -= random.randint(10, 25)
        autosave_game()
        print(Fore.YELLOW + f"Вы теряете {damage_taken} здоровья.")
        print(Fore.LIGHTGREEN_EX + f"Вы получили {coin_count} ед. монет и {food_count} ед. еды")
        print()
        _profile.profile()