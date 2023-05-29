import json
import sys

from variables import *
from colorama import init, Fore, Style, Back

from main_functions._clear_screen import clear
from main_functions._start_menu import *
from parts.explore import *
from parts.fight import *
from parts.craft import *
from parts.shop import *
from parts.lootbox import *
from parts.rest import *
from parts.eat import *
from parts.drink import *

init(autoreset=True)

def autosave_game():
    global version, health_max, level, progress, player, items, tools
    game_data = {
        "health_max": health_max,
        "level": level,
        "progress": progress,
        "player": player,
        "items": items,
        "tools": tools
        
    }
    with open("game_data.json", "w", encoding='utf-8') as f:
        json.dump(game_data, f, indent=4, ensure_ascii=False)


def load_game():
    global version, health_max, level, progress, player, items, tools
    clear()
    try:
        with open("game_data.json", "r", encoding='utf-8') as f:
            game_data = json.load(f)
            health_max = game_data[health_max]
            level = game_data[level]
            progress = game_data[progress]
            player = game_data[player]
            items = game_data[items]
            tools = game_data[tools]
            

        print(Fore.GREEN + "Игра загружена.")
    except FileNotFoundError:
        print(Fore.RED + "Файл сохранения не найден.")
    profile()

def die():
    autosave_game()
    input("Нажмите Enter, чтобы выйти из игры.")
    sys.exit()

def profile():
    global items, progress, player, tools
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
    if tools["Мечь"]["Прочность"] <= 0:
        tools["Мечь"]["Количество"] -= 1
        tools["Мечь"]["Прочность"] = 100
    if tools["Ведро"]["Прочность"] <= 0:
        tools["Ведро"]["Количество"] -= 1
        tools["Ведро"]["Прочность"] = 100
    if tools["Лодка"]["Прочность"] <= 0:
        tools["Лодка"]["Количество"] -= 1
        tools["Лодка"]["Прочность"] = 100
    if tools["Удочка"]["Прочность"] <= 0:
        tools["Удочка"]["Количество"] -= 1
        tools["Удочка"]["Прочность"] = 100

    if progress >= 100.0:
        level += 1
        progress = 0.0
        items["Лутбокс"] += 1
        clear()
        print(Fore.LIGHTGREEN_EX + f"Поздравляем! Твой уровень повышен до {level}")
        print("Ты получил 1 лутбокс")
        print()
        input("Нажми ENTER, чтобы продолжить...")
        clear()
        profile()

    if tools["Топор"]["Количество"] <= 0:
        tools["Топор"]["Количество"] = 0
    if tools["Кирка"]["Количество"] <= 0:
        tools["Кирка"]["Количество"] = 0
    if tools["Мечь"]["Количество"] <= 0:
        tools["Мечь"]["Количество"] = 0
    if tools["Ведро"]["Количество"] <= 0:
        tools["Ведро"]["Количество"] = 0
    if tools["Лодка"]["Количество"] <= 0:
        tools["Лодка"]["Количество"] = 0
    if tools["Удочка"]["Количество"] <= 0:
        tools["Удочка"]["Количество"] = 0
    
    autosave_game()

    print()
    print(Fore.GREEN + "ПРОФИЛЬ: ")
    print(player)
    print("-------------")
    print(Fore.GREEN + "РЕСУРСЫ: ")
    print(f'Монеты: {items["Монеты"]}')
    print(f'Дерево: {items["Дерево"]}')
    print(f'Вода: {items["Вода"]}')
    print(f'Еда: {items["Еда"]["Яблоко"]}')

    print(f'Угол: {items["Уголь"]}')
    print(f'Железо: {items["Железо"]}')
    print(f'Лутбокс: {items["Лутбокс"]}')
    print(f'Рыба: {items["Рыба"]}')
    print("-------------")
    print(Fore.GREEN + "ИНСТРУМЕНТЫ: ")
    print(f'Топор: {tools["Топор"]["Количество"]} прочность: {tools["Топор"]["Прочность"]}%')
    print(f'Кирка: {tools["Кирка"]["Количество"]} прочность: {tools["Кирка"]["Прочность"]}%')
    print(f'Меч: {tools["Мечь"]["Количество"]} прочность: {tools["Мечь"]["Прочность"]}%')
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
        start_menu()
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