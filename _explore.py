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

def explore():
    clear()
    print("Куда пойдём?")
    print("""
    0. Назад
    1. Лес
    2. Шахта
    3. Колодец
    4. Озеро
    """)
    choice = input(Fore.LIGHTBLACK_EX + "Введите номер: ")
    if choice == "0":
        clear()
        _profile.profile()
    elif choice == "1":
        clear()
        forest()
    elif choice == "2":
        clear()
        mineshaft()
    elif choice == "3":
        clear()
        well()
    elif choice == "4":
        clear()
        lake()
    else:
        clear()
        print(Fore.RED + "Неверный ввод. Попробуйте еще раз.")
        explore()
def forest():
    global items, progress, player, tools
    progress_count = random.uniform(0.1, 5.0)
    progress += progress_count
    if tools["Топор"]['Количество'] == 0:
        player["Усталость"] += random.randint(5, 15)
        player["Голод"] += random.randint(5, 10)
        player["Жажда"] += random.randint(10, 15)
        wood_count = random.randint(1, 15)
        water_count = random.randint(1, 10)
        food_count = random.randint(1, 10)
        coin_count = random.randint(1, 3)
        
        items["Монеты"] += coin_count
        items["Дерево"] += wood_count
        items["Вода"] += water_count
        items["Еда"]["Яблоко"] += food_count
        clear()
        print(Fore.GREEN + f"Вы добили {wood_count} ед. дерево, {water_count} ед. воды и {food_count} ед. еды")
        autosave_game()
        _profile.profile()
    elif tools["Топор"]['Количество'] > 0:
        wood_count = random.randint(20, 30)
        water_count = random.randint(1, 10)
        food_count = random.randint(1, 10)
        player["Усталость"] += random.randint(5, 15)
        player["Голод"] += random.randint(5, 10)
        player["Жажда"] += random.randint(5, 15)
        coin_count = random.randint(1, 3)
        items["Монеты"] += coin_count
        items["Еда"]["Яблоко"] += food_count
        tools["Топор"]["Прочность"] -= random.randint(5, 10)
        items["Вода"] += water_count
        items["Дерево"] += wood_count
        clear()
        autosave_game()
        print(Fore.GREEN + f"Вы добили {wood_count} ед. дерево, {water_count} ед. воды и {food_count} ед. еды, прочность топора: {tools['Топор']['Прочность']}%")
        _profile.profile()
def mineshaft():
    global items, progress, player, tools
    if level >= 2:
        progress_count = random.uniform(2.0, 5.0)
        progress += progress_count
        if tools["Кирка"]["Количество"] == 0:
            iron_count = random.randint(1, 5)
            coal_count = random.randint(1, 5)
            coin_count = random.randint(5, 10)
            items["Железо"] += iron_count
            items["Уголь"] += coal_count
            player["Усталость"] += random.randint(10, 20)
            player["Голод"] += random.randint(10, 15)
            player["Жажда"] += random.randint(10, 15)
            items["Монеты"] += coin_count
            autosave_game()
            clear()
            print(Fore.GREEN + f"Вы добили {iron_count} ед. железа и {coal_count} ед. угля")
            _profile.profile()
        elif tools["Кирка"]["Количество"] > 0:
            iron_count = random.randint(20, 30)
            coal_count = random.randint(20, 30)
            coin_count = random.randint(5, 15)
            items["Железо"] += iron_count
            items["Уголь"] += coal_count
            tools["Кирка"]["Прочность"] -= random.randint(5, 1)
            player["Усталость"] += random.randint(10, 20)
            player["Голод"] += random.randint(10, 15)
            player["Жажда"] += random.randint(10, 15)
            items["Монеты"] += coin_count
            autosave_game()
            clear()
            print(Fore.GREEN + f'Вы добили {coal_count} ед. железа и {iron_count} ед. железа, прочность кирки: {tools["Кирка"]["Прочность"]}%')
            _profile.profile()
    elif level < 2:
        clear()
        print(Fore.RED + "Чтобы пойти в шахту нужен 2 уровень")
    _profile.profile()
def well():
    global items, progress, player, tools
    if level >= 5 and tools["Ведро"]["Количество"] >= 1:
        progress_count = random.uniform(5.0, 10.0)
        progress += progress_count
        water_count = random.randint(10, 30)
        tools["Ведро"]["Прочность"] -= random.randint(10, 15)
        items["Вода"] += water_count
        player["Голод"] += random.randint(10, 20)
        player["Жажда"] += random.randint(10, 20)
        player["Усталость"] += random.randint(5, 15)
        print(Fore.GREEN + f"+ {water_count} ед. воды")
    elif level < 5:
        clear()
        print(Fore.RED + "Чтобы пойти к колодцу нужен 5 уровень")
    elif tools["Ведро"]["Количество"] == 0:
        clear()
        print(Fore.RED + "Чтобы пойти к колодцу нужен ведро")
    _profile.profile()
def lake():
    global items, progress, player, tools
    if level >= 10 and tools["Лодка"]["Количество"] >= 1 and tools["Удочка"]["Количество"] >= 1:
        
        progress_count = random.uniform(10.0, 20.0)
        progress += progress_count
        fish_count = random.randint(10, 30)
        tools["Лодка"]["Прочность"] -= 5
        tools["Удочка"]["Прочность"] -= 10
        items["Рыба"] += fish_count
        player["Голод"] += random.randint(10, 20)
        player["Жажда"] += random.randint(10, 20)
        player["Усталость"] += random.randint(5, 15)
        print(Fore.GREEN + f"Ты поймал {fish_count} ед. рыбы")
    elif level < 10:
        clear()
        print(Fore.RED + "Чтобы пойти в озеро нужен 10 уровень")
    elif tools["Лодка"]["Количество"] == 0:
        clear()
        print(Fore.RED + "Чтобы пойти в озеро нужна лодка")
    elif tools["Удочка"]["Количество"] == 0:
        print(Fore.RED + "Чтобы пойти в озеро нужна удочка")
    _profile.profile()