import random
import os
import json
import sys
from colorama import init, Fore, Style, Back

from variables import *
from utils import *

#PARTS
from parts._checks import *
from parts._craft import *
from parts._explore import *
from parts._lootbox import *
from parts._monster import *
from parts._rest import *
from parts._shop import *
from parts._eat import *
from parts._drink import *

init(autoreset=True)

class _start_menu:
    def start_menu():
        clear()
        print(Back.WHITE + Fore.BLACK + "\n Добро пожаловать в Adventures! " + Back.RESET)
        print("""

        1. Играть
        2. Обновления
        3. Помощь
        4. Выгрузить

        """)
        print(Fore.LIGHTBLACK_EX + 'Версия: ' + version)
        print()
        choice = input(Fore.WHITE + "Введите номер опции: ")

        if choice == "1":
            clear()
            _profile.profile()
        elif choice == "2":
            clear()
            _start_menu.updates()
        elif choice == "3":
            clear()
            help()
        elif choice == "4":
            clear()
            load_game()
        else:
            clear()
            print(Fore.RED + "Неправильный выбор. Попробуйте снова.")
            _start_menu.start_menu()

    def updates():
        clear()
        print(Fore.GREEN + "ОБНОВЛЕНИЯ:")
        print()
        print("Тут пока что пусто...")
        
        print("""

        1. Назад

        """)

        choice = input(Fore.LIGHTBLACK_EX + "Введите номер опции: ")
        if choice == "1":
            # Здесь вызываем функцию для начала игры
            _start_menu.start_menu()
        else:
            print(Fore.RED + "Неправильный выбор. Попробуйте снова.")
            _start_menu.start_menu()

    def help():
        clear()
        print(Fore.GREEN + "ПОМОЩЬ:")
        print()
        print("Тут пока что пусто...")
        
        print("""

        1. Назад

        """)

        choice = input(Fore.LIGHTBLACK_EX + "Введите номер опции: ")
        if choice == "1":
            # Здесь вызываем функцию для начала игры
            _start_menu.start_menu()
        else:
            print(Fore.RED + "Неправильный выбор. Попробуйте снова.")
            _start_menu.start_menu()

class _profile: #TODO
    def profile():
        global items, progress, level, player, tools
        check()
        
        autosave_game()

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
            _start_menu.start_menu()
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
            _profile.profile()

if __name__ == "__main__":
    _start_menu.start_menu()