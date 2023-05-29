import random
from variables import *
from colorama import init, Fore, Style, Back

import main_functions._clear_screen as _clear_screen
import main_functions._profile as _profile

init(autoreset=True)


def fight():
    global items, progress, player, tools
    progress_count = random.uniform(5.0, 7.0)
    progress += progress_count
    _clear_screen.clear()
    print(Fore.LIGHTYELLOW_EX + "Вы вступаете в бой с монстром!")
    if tools["Мечь"]["Количество"] == 0:
        damage_taken = random.randint(10, 20)
        coin_count  = random.randint(10, 20)
        food_count  = random.randint(10, 20)

        player["Здоровие"] -= damage_taken
        items["Монеты"] += coin_count
        items["Еда"]["Яблоко"] += food_count

        _profile.autosave_game()
        print(Fore.YELLOW + f"Вы теряете {damage_taken} здоровья")
        print(Fore.LIGHTGREEN_EX + f"Вы получили {coin_count} ед. монет и {food_count} ед. еды")
        print()
        _profile.profile()
    elif tools["Мечь"]["Количество"] >= 0:
        damage_taken = random.randint(5, 10)
        coin_count  = random.randint(20, 30)
        food_count  = random.randint(20, 30)

        player["Здоровие"] -= damage_taken
        items["Монеты"] += coin_count
        items["Еда"]["Яблоко"] += food_count

        tools["Мечь"]["Прочность"] -= random.randint(10, 25)
        _profile.autosave_game()
        print(Fore.YELLOW + f"Вы теряете {damage_taken} здоровья.")
        print(Fore.LIGHTGREEN_EX + f"Вы получили {coin_count} ед. монет и {food_count} ед. еды")
        print()
        _profile.profile()