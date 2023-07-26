import random
import os
import json
import sys
from colorama import init, Fore, Style, Back

from variables import *
from utils import clear, autosave_game, load_game, die

#PARTS
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

def check():
    global items, progress, level, player, tools
    if player["Усталость"] < 0:
        player["Усталость"] = 0
    if player["Жажда"] < 0:
        player["Жажда"] = 0
    if player["Голод"] < 0:
        player["Голод"] = 0
    if player["Здоровие"] > health_max:
        player["Здоровие"] = health_max
    
    if player["Усталость"] >= 100:
        clear()
        print(Fore.RED + "Вы умерли от усталости.")
        print()
        die()
    if player["Голод"] >= 100:
        clear()
        print(Fore.RED + "Вы умерли от голода.")
        print()
        input(Fore.RED + "Нажми Enter чтобы закрить окно: ")
        print()
        die()
    if player["Жажда"] >= 100:
        clear()
        print(Fore.RED + "Вы умерли от жажды.")
        print()
        die()
    if player["Здоровие"] <= 0:
        print("Вы умерли")
        print()
        die()
    
    if tools["Топор"]["Прочность"] <= 0:
        tools["Топор"]["Количество"] -= 1
        tools["Топор"]["Прочность"] = 100
    if tools["Кирка"]["Прочность"] <= 0:
        tools["Кирка"]["Количество"] -= 1
        tools["Кирка"]["Прочность"] = 100
    if tools["Меч"]["Прочность"] <= 0:
        tools["Меч"]["Количество"] -= 1
        tools["Меч"]["Прочность"] = 100
    if tools["Ведро"]["Прочность"] <= 0:
        tools["Ведро"]["Количество"] -= 1
        tools["Ведро"]["Прочность"] = 100
    if tools["Лодка"]["Прочность"] <= 0:
        tools["Лодка"]["Количество"] -= 1
        tools["Лодка"]["Прочность"] = 100
    if tools["Удочка"]["Прочность"] <= 0:
        tools["Удочка"]["Количество"] -= 1
        tools["Удочка"]["Прочность"] = 100
    if progress >= 100:
        level += 1
        progress = 0.0
        lootbox_quantity = random.randint(1, 5)
        items["Лутбокс"] += lootbox_quantity
        clear()
        print(Fore.LIGHTGREEN_EX + f"Поздравляем! Твой уровень повышен до {level}")
        print(f"Ты получил {lootbox_quantity} лутбокс")
        print()
        input("Нажми ENTER, чтобы продолжить...")
        clear()
        profile()
    if tools["Топор"]["Количество"] <= 0:
        tools["Топор"]["Количество"] = 0
    if tools["Кирка"]["Количество"] <= 0:
        tools["Кирка"]["Количество"] = 0
    if tools["Меч"]["Количество"] <= 0:
        tools["Меч"]["Количество"] = 0
    if tools["Ведро"]["Количество"] <= 0:
        tools["Ведро"]["Количество"] = 0
    if tools["Лодка"]["Количество"] <= 0:
        tools["Лодка"]["Количество"] = 0
    if tools["Удочка"]["Количество"] <= 0:
        tools["Удочка"]["Количество"] = 0