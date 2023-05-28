import random
from variables import *
from colorama import init, Fore, Style, Back

import main_functions._clear_screen as _clear_screen
import main_functions._profile as _profile

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
    """)
    choice = input()
    if choice == "0":
        _clear_screen.clear()
        _profile.profile()
    elif choice == "1":
        if items["Дерево"] >= 5 and items["Железо"] >= 3:
            print(Fore.GREEN + "Вы создали топор")
            tools["Топор"]["Количество"] += 1
            items["Дерево"] -= 5
            items["Железо"] -= 3
            progress_count = random.uniform(3.0, 5.0)
            progress += progress_count
            _profile.autosave_game()
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
            _profile.autosave_game()
        else:
            print(Fore.RED + "Недостаточно материалов для создания кирки")
  
    elif choice == "3":
        if items["Железо"] >= 2 and items["Дерево"] >= 1:
            print(Fore.GREEN + "Вы создали меч")
            tools["Мечь"]["Количество"] += 1
            items["Железо"] -= 2
            items["Дерево"] -= 1
            progress_count = random.uniform(5.0, 9.0)
            progress += progress_count
            _profile.autosave_game()
        else:
            print(Fore.RED + "Недостаточно материалов для создания меча")
    elif choice == "4":
        if items["Железо"] >= 3:
            print(Fore.GREEN + "Вы создали ведро")
            tools["Ведро"]["Количество"] += 1
            items["Железо"] -= 3
            progress_count = random.uniform(5.0, 9.0)
            progress += progress_count
            _profile.autosave_game()
        else:
            print(Fore.RED + "Недостаточно материалов для создания ведра")
    else:
        print(Fore.RED + "Неверный ввод. Попробуйте еще раз.")
        craft()
    _profile.autosave_game()
    _profile.profile()