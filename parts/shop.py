import random
from variables import *
from colorama import init, Fore, Style, Back

import main_functions._clear_screen as _clear_screen
import main_functions._profile as _profile

init(autoreset=True)

def shop():
    print(Fore.GREEN + "Добро пожаловать в магазин\n")
    print("Что будем делать?\n"
          "1. Купить\n"
          "2. Продать\n"
          "3. Назад\n")
    choice = input().lower()

    if choice == "1":
        _clear_screen.clear()
        buy()
    elif choice == "2":
        _clear_screen.clear()
        sell()
    elif choice == "3":
        _clear_screen.clear()
        _profile.profile()
    else:
        print("Неправильный ввод. Попробуйте ещё\n")


def buy():
    global items, progress, player, tools
    
    food_price, water_price, coal_price, wood_price, iron_price, lootbox_price = 10, 10, 15, 20, 25, 300
    axe_price, pickaxe_price, sword_price, bucket_price = 50, 50, 50, 100

    progress_count = random.uniform(0.1, 5.0)
    progress += progress_count
    print(Fore.GREEN + f'Твои монеты: {items["Монеты"]}\n\n')
    print("Что хочешь купить?\n\n"
        f"0. назад\n"
        f"1. еда - {food_price} монет\n"
        f"2. вода - {water_price} монет\n"
        f"3. уголь - {coal_price} монет\n"
        f"4. дерево - {wood_price} монет\n"
        f"5. железо - {iron_price} монет\n"
        f"6. топор - {axe_price} монет\n"
        f"7. кирка - {pickaxe_price} монет\n"
        f"8. меч - {sword_price} монет\n"
        f"9. лутбокс - {lootbox_price} монет")
    choice = input().lower()
    
    if choice == "0":
        _clear_screen.clear()
        shop()
    elif choice == "1":
        if items["Монеты"] >= food_price:
            _clear_screen.clear()
            items["Монеты"] -= food_price 
            items["Еда"]["Яблоко"] += 5 
            print(Fore.GREEN + f"Ты купил 5 еды за {food_price} монет\n")
            buy()
        else:
            print(Fore.RED + "Недостаточно монет\n")
            buy()
    elif choice == "2":
        if items["Монеты"] >= water_price:
            _clear_screen.clear()
            items["Монеты"] -= water_price
            items["Вода"] += 5
            print(Fore.GREEN + f"Ты купил 5 воды за {food_price} монет\n")
            _profile.autosave_game()
            buy()
        else:
            print(Fore.RED + "Недостаточно монет\n")
            buy()
    elif choice == "3":
        if items["Монеты"] >= coal_price:
            _clear_screen.clear()
            items["Монеты"] -= coal_price
            items["Уголь"] += 5
            print(Fore.GREEN + f"Ты купил 5 уголья за {coal_price} монет\n")
            _profile.autosave_game()
            buy()
        else:
            print(Fore.RED + "Недостаточно монет\n")
            buy()
    elif choice == "4":
        if items["Монеты"] >= wood_price:
            _clear_screen.clear()
            items["Монеты"] -= wood_price
            items["Дерево"] += 5
            print(Fore.GREEN + f"Ты купил 5 дерева за {wood_price} монет\n")
            _profile.autosave_game()
            buy()
        else:
            print(Fore.RED + "Недостаточно монет\n")
            buy()
    elif choice == "5":
        if items["Монеты"] >= iron_price:
            _clear_screen.clear()
            items["Монеты"] -= iron_price
            items["Железо"] += 5
            print(Fore.GREEN + f"Ты купил 5 железа за {iron_price} монет\n")
            _profile.autosave_game()
            buy()
        else:
            print(Fore.RED + "Недостаточно монет\n")
            buy()
    elif choice == "6":
        if items["Монеты"] >= axe_price:
            _clear_screen.clear()
            items["Монеты"] -= axe_price
            tools["Топор"]["Количество"] += 1
            print(Fore.GREEN + f"Ты купил 1 топор за {axe_price} монет\n")
            _profile.autosave_game()
            buy()
        else:
            print(Fore.RED + "Недостаточно монет\n")
            buy()
    elif choice == "7":
        if items["Монеты"] >= pickaxe_price:
            _clear_screen.clear()
            items["Монеты"] -= pickaxe_price
            tools["Кирка"]["Количество"] += 1
            print(Fore.GREEN + f"Ты купил 1 кирку за {pickaxe_price} монет\n")
            _profile.autosave_game()
            buy()
        else:
            print(Fore.RED + "Недостаточно монет\n")
            buy()
    elif choice == "8":
        if items["Монеты"] >= sword_price:
            _clear_screen.clear()
            items["Монеты"] -= sword_price
            tools["Мечь"]["Количество"] += 1
            print(Fore.GREEN + f"Ты купил 1 кирку за {sword_price} монет\n")
            _profile.autosave_game()
            buy()
        else:
            print(Fore.RED + "Недостаточно монет\n")
            buy()
    elif choice == "9":
        if items["Монеты"] >= lootbox_price:
            _clear_screen.clear()
            items["Монеты"] -= lootbox_price
            items["Лутбокс"] += 1
            print(Fore.GREEN + f"Ты купил 1 лутбокс за {lootbox_price} монет\n")
            _profile.autosave_game()
            buy()
    else:
        _clear_screen.clear()
        print(Fore.RED + "Неправильный ввод. Попробуйте ещё\n")
        buy()

def sell():
    global items, progress, player, tools
    
    food_sell_price, water_sell_price, coal_sell_price, wood_sell_price, iron_sell_price = 3, 3, 5, 10, 15
    axe_sell_price, pickaxe_sell_price, sword_sell_price = 20, 20, 20

    progress_count = random.uniform(0.1, 5.0)
    progress += progress_count
    print(f"""
У тебя есть:

0. назад
1. еда - {items["Еда"]["Яблоко"]} | {food_sell_price} монет
2. вода - {items["Вода"]} | {water_sell_price} монет
3. уголь - {items["Уголь"]} | {coal_sell_price} монет
4. дерево - {items["Дерево"]} | {wood_sell_price} монет
5. железо - {items["Железо"]} | {iron_sell_price} монет
6. топор - {tools["Топор"]["Количество"]} | {axe_sell_price} монет
7. кирка - {tools["Кирка"]["Количество"]} | {pickaxe_sell_price} монет
8. меч - {tools["Мечь"]["Количество"]} | {sword_sell_price} монет
          """)
    choice = input("Что хочешь продать?").lower()

    if choice == "0":
        _clear_screen.clear()
        shop()
    elif choice == "1":
        if items["Еда"]["Яблоко"] > 0:
            _clear_screen.clear()
            items["Монеты"] += food_sell_price
            items["Еда"]["Яблоко"] -= 1
            print(Fore.GREEN + f"Ты продал 1 еду за {food_sell_price} монет")
            _profile.autosave_game()
            sell()
        else:
            print(Fore.RED + "У тебя нет еды для продажи")
            sell()
    elif choice == "2":
        if items["Вода"] > 0:
            _clear_screen.clear()
            items["Монеты"] += water_sell_price
            items["Вода"] -= 1
            print(Fore.GREEN + f"Ты продал 1 воду за {water_sell_price} монет")
            _profile.autosave_game()
            sell()
        else:
            print(Fore.RED + "У тебя нет воды для продажи")
            sell()
    elif choice == "3":
        if items["Уголь"] > 0:
            _clear_screen.clear()
            items["Монеты"] += coal_sell_price
            items["Уголь"] -= 1
            print(Fore.GREEN + f"Ты продал 1 уголь за {coal_sell_price} монет")
            _profile.autosave_game()
            sell()
        else:
            print(Fore.RED + "У тебя нет угля для продажи")
            sell()
    elif choice == "4":
        if items["Дерево"] > 0:
            _clear_screen.clear()
            items["Монеты"] += wood_sell_price
            items["Дерево"] -= 1
            print(Fore.GREEN + f"Ты продал 1 дерево за {wood_sell_price} монет")
            _profile.autosave_game()
            sell()
        else:
            print(Fore.RED + "У тебя нет дерева для продажи")
            sell()
    elif choice == "5":
        if items["Железо"] > 0:
            _clear_screen.clear()
            items["Монеты"] += iron_sell_price
            items["Железо"] -= 1
            print(Fore.GREEN + f"Ты продал 1 железо за {iron_sell_price} монет")
            _profile.autosave_game()
            sell()
        else:
            print(Fore.RED + "У тебя нет железа для продажи")
            sell()
    elif choice == "6":
        if tools["Топор"]["Количество"] > 0:
            _clear_screen.clear()
            items["Монеты"] += axe_sell_price
            tools["Топор"]["Количество"] -= 1
            if tools["Топор"]["Количество"] == 0:
                tools["Топор"]["Прочность"] = 100
            print(Fore.GREEN + f"Ты продал 1 топор за {axe_sell_price} монет")
            _profile.autosave_game()
            sell()
        else:
            print(Fore.RED + "У тебя нет топора для продажи")
            sell()
    elif choice == "7":
        if tools["Кирка"]["Количество"] > 0:
            _clear_screen.clear()
            items["Монеты"] += pickaxe_sell_price
            tools["Кирка"]["Количество"] -= 1
            if tools["Кирка"]["Количество"] == 0:
                tools["Кирка"]["Прочность"] = 100
            print(Fore.GREEN + f"Ты продал 1 кирку за {pickaxe_sell_price} монет")
            _profile.autosave_game()
            sell()
        else:
            print(Fore.RED + "У тебя нет кирки для продажи")
            sell()
    elif choice == "8":
        if tools["Мечь"]["Количество"] > 0:
            _clear_screen.clear()
            items["Монеты"] += tools["Мечь"]["Количество"]
            tools["Мечь"]["Количество"] -= 1
            if tools["Мечь"]["Количество"] == 0:
                tools["Мечь"]["Прочность"] = 100
            print(Fore.GREEN + f"Ты продал 1 кирку за {sword_sell_price} монет")
            _profile.autosave_game()
            sell()
    else:
        _clear_screen.clear()
        print(Fore.RED + "Неправылный ввод. Попробуйте ещё")
        sell()