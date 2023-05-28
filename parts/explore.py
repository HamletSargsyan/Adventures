import random
from variables import *
from colorama import init, Fore, Style, Back

import main_functions._clear_screen as _clear_screen
import main_functions._profile as _profile

init(autoreset=True)


def explore():
    _clear_screen.clear()
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
        _clear_screen.clear()
        _profile.profile()
    elif choice == "1":
        _clear_screen.clear()
        forest()
    elif choice == "2":
        _clear_screen.clear()
        mineshaft()
    elif choice == "3":
        _clear_screen.clear()
        well()
    elif choice == "4":
        _clear_screen.clear()
        lake()

    else:
        _clear_screen.clear()
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
        _clear_screen.clear()
        print(Fore.GREEN + f"Вы добили {wood_count} ед. дерево, {water_count} ед. воды и {food_count} ед. еды")
        _profile.autosave_game()
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
        tools["Топор"]["Прочность"] -= 5
        items["Вода"] += water_count
        items["Дерево"] += wood_count
        _clear_screen.clear()
        _profile.autosave_game()
        print(Fore.GREEN + f"Вы добили {wood_count} ед. дерево, {water_count} ед. воды и {food_count} ед. еды, прочность топора: {tools['Топор']['рочность']}%")
        _profile.profile()

def mineshaft():
    global items, progress, player, tools
    progress_count = random.uniform(2.0, 5.0)
    progress += progress_count
    if tools["Кирка"]["Количество"] == 0:
        iron_count = random.randint(1, 5)
        coal_count = random.randint(1, 5)
        coin_count = random.randint(1, 3)
        items["Железо"] += iron_count
        items["Уголь"] += coal_count
        
        player["Усталость"] += random.randint(10, 20)
        player["Голод"] += random.randint(10, 15)
        player["Жажда"] += random.randint(10, 15)
        
        items["Монеты"] += coin_count
        _profile.autosave_game()
        _clear_screen.clear()
        print(Fore.GREEN + f"Вы добили {iron_count} ед. железа и {coal_count} ед. угля")
        _profile.profile()
    elif tools["Кирка"]["Количество"] > 0:
        iron_count = random.randint(20, 30)
        coal_count = random.randint(20, 30)
        coin_count = random.randint(1, 3)

        items["Железо"] += iron_count
        items["Уголь"] += coal_count
        tools["Кирка"]["Прочность"] -= 15

        player["Усталость"] += random.randint(10, 20)
        player["Голод"] += random.randint(10, 15)
        player["Жажда"] += random.randint(10, 15)

        items["Монеты"] += coin_count
        _profile.autosave_game()
        _clear_screen.clear()
        print(Fore.GREEN + f'Вы добили {coal_count} ед. железа и {iron_count} ед. железа, прочность кирки: {tools["Кирка"]["Прочность"]}%')
        _profile.profile()

def well():
    global items, progress, player, tools
    if level >= 5 and tools["Ведро"]["Количество"] >= 1:

        progress_count = random.uniform(0.1, 5.0)
        progress += progress_count

        water_count = random.randint(10, 30)
        tools["Ведро"]["Прочность"] -= 5
        items["Вода"] += water_count
        player["Голод"] += random.randint(10, 20)
        player["Жажда"] += random.randint(10, 20)
        player["Усталость"] += random.randint(5, 15)

        print(Fore.GREEN + f"+ {water_count} ед. воды")
    elif level < 5:
        _clear_screen.clear()
        print(Fore.RED + "Чтобы пойти к колодцу нужен 5 уровень")
    elif tools["Ведро"]["Количество"] == 0:
        _clear_screen.clear()
        print(Fore.RED + "Чтобы пойти к колодцу нужен ведро")
    _profile.profile()

def lake():
    global items, progress, player, tools
    if level >= 10 and tools["Лодка"]["Количество"] >= 1 and tools["Удочка"]["Количество"] >= 1:
        
        progress_count = random.uniform(0.1, 10.0)
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
        _clear_screen.clear()
        print(Fore.RED + "Чтобы пойти в озеро нужен 10 уровень")
    elif tools["Лодка"]["Количество"] == 0:
        _clear_screen.clear()
        print(Fore.RED + "Чтобы пойти в озеро нужна лодка")
    elif tools["Удочка"]["Количество"] == 0:
        print(Fore.RED + "Чтобы пойти в озеро нужна удочка")
    _profile.profile()