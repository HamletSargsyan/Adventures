import random
import os
import json
import sys
from colorama import init, Fore, Style, Back

from settings.variables import *
from settings.utils import clear, autosave_game, load_game, die

#PARTS
from parts._checks import check
from parts._craft import craft
from parts._explore import explore
from parts._lootbox import lootbox_menu
from parts._monster import fight
from parts._rest import rest
from parts._shop import shop
from parts._eat import eat
from parts._drink import drink
from parts._profile import profile

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
            profile()
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


if __name__ == "__main__":
    _start_menu.start_menu()