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


def lootbox_open():
    global items, progress, player, tools
    loots = ["монеты", "дерево", "вода", "яблоко", "железо", "уголь"]
    items["Лутбокс"] -= 1
    print(Fore.LIGHTGREEN_EX + "Ты открыл лутбокс и получил:")
    print()
    for i in range(random.randint(1, 5)):
        loot = random.choice(loots)
        quantity = random.randint(1, 10)
        print(f"{loot}: {quantity}".capitalize())
        if loot == "монеты":
            items["Монеты"] += quantity
        elif loot == "дерево":
            items["Дерево"] += quantity
        elif loot == "вода":
            items["Вода"] += quantity
        elif loot == "яблоко":
            items["Еда"]["Яблоко"] += quantity
        elif loot == "железо":
            items["Железо"] += quantity
        elif loot == "уголь":
            items["Уголь"] += quantity
        autosave_game()
    print()
    input("Нажми ENTER, чтобы продолжить...")
    clear()
    _profile.profile()
def lootbox_menu():
    clear()
    print("Хочешь открить лутбокс?")
    print("""
    1. да
    2. нет
    """)
    choice = input().lower()
    if choice == "1":
        if items["Лутбокс"] >= 1:
            clear()
            lootbox_open()
        else:
            clear()
            print(Fore.RED + "У тебя нет лутбокса")
            _profile.profile()
    elif choice == "2":
        clear()
        _profile.profile()
    else:
        clear()
        print(Fore.RED + "Неправылный ввод. Попробуйте ещё")
        lootbox_menu()
