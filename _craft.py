import random
import os
import json
import sys
from colorama import init, Fore, Style, Back

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
from _profile import *

init(autoreset=True)

def craft():
    global items, progress, player, tools
    print(Fore.WHITE + "Что вы хотите скрафтить?")
    print("""
    0. Назад
    1. Топор
    2. Кирка
    3. Меч
    4. Ведро
    5. Лодка
    6. Удочка
    """)
    choice = input()
    if choice == "0":
        clear()
        profile()
    elif choice == "1":
        if items["Дерево"] >= 5 and items["Железо"] >= 3:
            print(Fore.GREEN + "Вы создали топор")
            tools["Топор"]["Количество"] += 1
            items["Дерево"] -= 5
            items["Железо"] -= 3
            progress_count = random.uniform(3.0, 5.0)
            progress += progress_count
            autosave_game()
        else:
            print(Fore.RED + "Недостаточно материалов для создания топора")
    elif choice == "2":
        if items["Железо"] >= 5 and items["Дерево"] >= 3:
            print(Fore.GREEN + "Вы создали кирку")
            tools["Кирка"]["Количество"] += 1
            items["Железо"] -= 5
            items["Дерево"] -= 3
            progress_count = random.uniform(5.0, 8.0)
            progress += progress_count
            autosave_game()
        else:
            print(Fore.RED + "Недостаточно материалов для создания кирки")

    elif choice == "3":
        if items["Железо"] >= 2 and items["Дерево"] >= 1:
            print(Fore.GREEN + "Вы создали меч")
            tools["Меч"]["Количество"] += 1
            items["Железо"] -= 2
            items["Дерево"] -= 1
            progress_count = random.uniform(5.0, 9.0)
            progress += progress_count
            autosave_game()
        else:
            print(Fore.RED + "Недостаточно материалов для создания меча")
    elif choice == "4":
        if items["Железо"] >= 3:
            print(Fore.GREEN + "Вы создали ведро")
            tools["Ведро"]["Количество"] += 1
            items["Железо"] -= 3
            progress_count = random.uniform(5.0, 9.0)
            progress += progress_count
            autosave_game()
        else:
            print(Fore.RED + "Недостаточно материалов для создания ведра")
    elif choice == "5":
        if items["Железо"] >= 2 and items["Дерево"] >= 5:
            print(Fore.GREEN + "Вы создали лодку")
            tools["Лодка"]["Количество"] += 1
            items["Дерево"] -= 5
            items["Железо"] -= 2
            progress_count = random.uniform(5.0, 9.0)
            progress += progress_count
            autosave_game()
        else:
            print(Fore.RED + "Недостаточно материалов для создания лодки")
    elif choice == "6":
        if items["Железо"] >= 5:
            print(Fore.GREEN + "Вы создали удочку")
            tools["Удочка"]["Количество"] += 1
            items["Железо"] -= 5
            progress_count = random.uniform(5.0, 9.0)
            progress += progress_count
            autosave_game()
        else:
            print(Fore.RED + "Недостаточно материалов для создания удочки")
    else:
        print(Fore.RED + "Неверный ввод. Попробуйте еще раз.")
        craft()
    autosave_game()
    profile()