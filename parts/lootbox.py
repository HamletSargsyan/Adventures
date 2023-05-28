import random
from variables import *
from colorama import init, Fore, Style, Back

import main_functions._clear_screen as _clear_screen
import main_functions._profile as _profile

init(autoreset=True)


def lootbox_open():
    global items, progress, player, tools
    items = ["монеты", "дерево", "вода", "еда", "железо", "уголь", "топор", "кирка", "меч"]

    items["Лутбокс"] -= 1
    print(Fore.LIGHTGREEN_EX + "Ты открыл лутбокс и получил:")
    print()
    for i in range(3):
        item = random.choice(items)
        quantity = random.randint(1, 10)
        print(f"{item}: {quantity}".capitalize())
        if item == "монеты":
            items["Монеты"] += quantity
            _profile.autosave_game()
        elif item == "дерево":
            items["Дерево"] += quantity
            _profile.autosave_game()
        elif item == "вода":
            items["Вода"] += quantity
            _profile.autosave_game()
        elif item == "еда":
            items["Еда"]["Яблоко"] += quantity
            _profile.autosave_game()
        elif item == "железо":
            items["Железо"] += quantity
            _profile.autosave_game()
        elif item == "уголь":
            items["Уголь"] += quantity
            _profile.autosave_game()
        elif item == "топор":
            tools["Топор"]["Количество"] += quantity
            _profile.autosave_game()
        elif item == "кирка":
            tools["Кирка"]["Количество"] += quantity
            _profile.autosave_game()
        elif item == "меч":
            tools["Мечь"]["Количество"] += quantity
            _profile.autosave_game()
    print()
    input("Нажми ENTER, чтобы продолжить...")
    _clear_screen._clear_screen.clear()
    _profile.profile()


def lootbox_menu():
    _clear_screen._clear_screen.clear()
    print("Хочешь открить лутбокс?")
    print("""
    1. да
    2. нет
    """)
    choice = input().lower()

    if choice == "1":
        if items["Лутбокс"] >= 1:
            _clear_screen._clear_screen.clear()
            lootbox_open()
        else:
            _clear_screen._clear_screen.clear()
            print(Fore.RED + "У тебя нет лутбокса")
            _profile.profile()
    elif choice == "2":
        _clear_screen._clear_screen.clear()
        _profile.profile()
    else:
        _clear_screen._clear_screen.clear()
        print(Fore.RED + "Неправылный ввод. Попробуйте ещё")
        lootbox_menu()