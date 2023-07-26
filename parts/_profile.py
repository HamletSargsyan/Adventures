import random
import os
import json
import sys
from colorama import init, Fore, Style, Back

from settings.variables import *
from settings.utils import clear, autosave_game, load_game, die

#PARTS
from _checks import check
from _craft import craft
from _explore import explore
from _lootbox import lootbox_menu
from _monster import fight
from _rest import rest
from _shop import shop
from _eat import eat
from _drink import drink

init(autoreset=True)


def profile():
    global items, progress, level, player, tools
    check()
    
    load_game()
    print()
    print(Fore.GREEN + "ПРОФИЛЬ: ")
    print(f'Здоровие: {player["Здоровие"]}')
    print(f'Голод: {player["Голод"]}')
    print(f'Жажда: {player["Жажда"]}')
    print(f'Усталость: {player["Усталость"]}')
    print(f'Уровень: {level}')
    print(f'Опыт: {progress:.1f}%/100%')
    print("-------------")
    print(Fore.GREEN + "РЕСУРСЫ: ")
    print(f'Монеты: {items["Монеты"]}')
    print(f'Дерево: {items["Дерево"]}')
    print(f'Вода: {items["Вода"]}')
    print(f'Яблоко: {items["Еда"]["Яблоко"]}')
    print(f'Угол: {items["Уголь"]}')
    print(f'Железо: {items["Железо"]}')
    print(f'Лутбокс: {items["Лутбокс"]}')
    print(f'Рыба: {items["Рыба"]}')
    print("-------------")
    print(Fore.GREEN + "ИНСТРУМЕНТЫ: ")
    print(f'Топор: {tools["Топор"]["Количество"]} прочность: {tools["Топор"]["Прочность"]}%')
    print(f'Кирка: {tools["Кирка"]["Количество"]} прочность: {tools["Кирка"]["Прочность"]}%')
    print(f'Меч: {tools["Меч"]["Количество"]} прочность: {tools["Меч"]["Прочность"]}%')
    print(f'Ведро: {tools["Ведро"]["Количество"]} прочность: {tools["Ведро"]["Прочность"]}%')
    print(f'Лодка: {tools["Лодка"]["Количество"]} прочность: {tools["Лодка"]["Прочность"]}%')
    print(f'Удочка: {tools["Удочка"]["Количество"]} прочность: {tools["Удочка"]["Прочность"]}%')
    print()
    print(Fore.WHITE + "Выберите действие: ")
    print("""
        ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
        ┃ 0. назад        |   5. выпить    ┃
        ┃ 1. исследовать  |   6. крафтить  ┃
        ┃ 2. сражаться    |   7. лутбокс   ┃
        ┃ 3. отдыхать     |   8. выгрузить ┃
        ┃ 4. поесть       |   9. магазин   ┃
        ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
    """)
    choice = input()
    if choice == "0":
        clear()
        # _start_menu.start_menu() #FIXME
    elif choice == "1":
        clear()
        explore()
    elif choice == "2":
        clear()
        fight()
    elif choice == "3":
        clear()
        rest()
    elif choice == "4":
        clear()
        eat()
    elif choice == "5":
        clear()
        drink()
    elif choice == "6":
        clear()
        craft()
    elif choice == "7":
        lootbox_menu()
    elif choice == "8":
        clear()
        load_game()
    elif choice == "9":
        clear()
        shop()    
    else:
        clear()
        print(Fore.RED + "Неправылный ввод. Попробуйте ещё")
        profile()