from colorama import init, Fore, Style, Back

import main_functions._clear_screen as _clear_screen
import main_functions._profile as _profile

from variables import *

init(autoreset=True)

def start_menu():
    _clear_screen.clear()
    print(Back.WHITE + Fore.BLACK + "\n Добро пожаловать в Adventures! " + Back.RESET)
    print("""

    1. Играть
    2. Обновления
    3. Помощь
    
    """)
    print(Fore.LIGHTBLACK_EX + 'Версия: ' + version)
    print()
    choice = input(Fore.WHITE + "Введите номер опции: ")

    if choice == "1":
        # Здесь вызываем функцию для входа в аккаунт
        _clear_screen.clear()
        _profile.profile()
    elif choice == "2":
        # Здесь вызываем функцию для регистрации
        _clear_screen.clear()
        updates()

    elif choice == "3":
        # Здесь показываем обновления новой версии
        _clear_screen.clear()
        help()
    else:
        _clear_screen.clear()
        print(Fore.RED + "Неправильный выбор. Попробуйте снова.")
        start_menu()

def updates():
    _clear_screen.clear()
    print(Fore.GREEN + "ОБНОВЛЕНИЯ:")
    print()
    print("Тут пока что пусто...")
    
    print("""

    1. Назад

    """)

    choice = input(Fore.LIGHTBLACK_EX + "Введите номер опции: ")
    if choice == "1":
        # Здесь вызываем функцию для начала игры
        start_menu()
    else:
        print(Fore.RED + "Неправильный выбор. Попробуйте снова.")
        start_menu()

def help():
    _clear_screen.clear()
    print(Fore.GREEN + "ПОМОЩЬ:")
    print()
    print("Тут пока что пусто...")
    
    print("""

    1. Назад

    """)

    choice = input(Fore.LIGHTBLACK_EX + "Введите номер опции: ")
    if choice == "1":
        # Здесь вызываем функцию для начала игры
        start_menu()
    else:
        print(Fore.RED + "Неправильный выбор. Попробуйте снова.")
        start_menu()