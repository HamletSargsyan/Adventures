import random
import os
import json
import sys
from colorama import init, Fore, Style, Back

from settings.variables import *
from settings.utils import clear, autosave_game, load_game, die

#PARTS
from _checks import *
from _profile import *

init(autoreset=True)


def shop():
    print(Fore.GREEN + "Добро пожаловать в магазин\n")
    print("Что будем делать?\n"
        "1. Купить\n"
        "2. Продать\n"
        "3. Назад\n")
    choice = input().lower()
    if choice == "1":
        clear()
        buy()
    elif choice == "2":
        clear()
        sell()
    elif choice == "3":
        clear()
        profile()
    else:
        print("Неправильный ввод. Попробуйте ещё\n")
        shop()
def buy():
    global items, progress, player, tools
    
    food_price, water_price, coal_price, wood_price, iron_price, lootbox_price = 10, 10, 15, 20, 25, 300
    axe_price, pickaxe_price, sword_price, bucket_price = 50, 50, 50, 100
    print(Fore.GREEN + f'Твои монеты: {items["Монеты"]}\n\n')
    print("Что хочешь купить?\n\n"
        f"0. назад\n"
        f"1. яблоко - {food_price} монет\n"
        f"2. вода - {water_price} монет\n"
        f"3. уголь - {coal_price} монет\n"
        f"4. дерево - {wood_price} монет\n"
        f"5. железо - {iron_price} монет\n"
        f"6. топор - {axe_price} монет\n"
        f"7. кирка - {pickaxe_price} монет\n"
        f"8. меч - {sword_price} монет\n"
        f"9. лутбокс - {lootbox_price} монет")
    
    try:
        choice = int(input("\nЧто хочешь купить? (номер тавара) "))
        if choice == 0:
            clear()
            shop()
        quantity = int(input("Сколько? "))
        if quantity == 0:
            clear()
            shop()
        elif choice == 1:
            if items["Монеты"] >= food_price * int(quantity):
                clear()
                items["Монеты"] -= food_price * int(quantity) 
                items["Еда"]["Яблоко"] += int(quantity) 
                print(Fore.GREEN + f"Ты купил {quantity} еды за {food_price * int(quantity)} монет\n")
                buy()
            else:
                print(Fore.RED + "Недостаточно монет\n")
                buy()
        elif choice == 2:
            if items["Монеты"] >= water_price * int(quantity):
                clear()
                items["Монеты"] -= water_price * int(quantity)
                items["Вода"] += int(quantity)
                print(Fore.GREEN + f"Ты купил {quantity} воды за {water_price * int(quantity)} монет\n")
                autosave_game()
                buy()
            else:
                print(Fore.RED + "Недостаточно монет\n")
                buy()
        elif choice == 3:
            if items["Монеты"] >= coal_price * int(quantity):
                clear()
                items["Монеты"] -= coal_price * int(quantity)
                items["Уголь"] += int(quantity)
                print(Fore.GREEN + f"Ты купил {quantity} уголья за {coal_price * int(quantity)} монет\n")
                autosave_game()
                buy()
            else:
                print(Fore.RED + "Недостаточно монет\n")
                buy()
        elif choice == 4:
            if items["Монеты"] >= wood_price * int(quantity):
                clear()
                items["Монеты"] -= wood_price * int(quantity)
                items["Дерево"] += int(quantity)
                print(Fore.GREEN + f"Ты купил {quantity} дерева за {wood_price * int(quantity)} монет\n")
                autosave_game()
                buy()
            else:
                print(Fore.RED + "Недостаточно монет\n")
                buy()
        elif choice == 5:
            if items["Монеты"] >= iron_price * int(quantity):
                clear()
                items["Монеты"] -= iron_price * int(quantity)
                items["Железо"] += int(quantity)
                print(Fore.GREEN + f"Ты купил {quantity} железа за {iron_price * int(quantity)} монет\n")
                autosave_game()
                buy()
            else:
                print(Fore.RED + "Недостаточно монет\n")
                buy()
        elif choice == 6:
            if items["Монеты"] >= axe_price * int(quantity):
                clear()
                items["Монеты"] -= axe_price * int(quantity)
                tools["Топор"]["Количество"] += int(quantity)
                print(Fore.GREEN + f"Ты купил {quantity} топор(ов) за {axe_price * int(quantity)} монет\n")
                autosave_game()
                buy()
            else:
                print(Fore.RED + "Недостаточно монет\n")
                buy()
        elif choice == 7:
            if items["Монеты"] >= pickaxe_price * int(quantity):
                clear()
                items["Монеты"] -= pickaxe_price * int(quantity)
                tools["Кирка"]["Количество"] += int(quantity)
                print(Fore.GREEN + f"Ты купил {quantity} кирку(и) за {pickaxe_price * int(quantity)} монет\n")
                autosave_game()
                buy()
            else:
                print(Fore.RED + "Недостаточно монет\n")
                buy()
        elif choice == 8:
            if items["Монеты"] >= sword_price * int(quantity):
                clear()
                items["Монеты"] -= sword_price * int(quantity)
                tools["Меч"]["Количество"] += int(quantity)
                print(Fore.GREEN + f"Ты купил {quantity} меч(а) за {sword_price * int(quantity)} монет\n")
                autosave_game()
                buy()
            else:
                print(Fore.RED + "Недостаточно монет\n")
                buy()
        elif choice == 9:
            if items["Монеты"] >= lootbox_price * int(quantity):
                clear()
                items["Монеты"] -= lootbox_price * int(quantity)
                items["Лутбокс"] += int(quantity)
                print(Fore.GREEN + f"Ты купил {quantity} лутбокс(ов) за {lootbox_price * int(quantity)} монет\n")
                autosave_game()
                buy()
            else:
                print(Fore.RED + "Недостаточно монет\n")
                buy()
        else:
            clear()
            print(Fore.RED + "Неправильный ввод. Попробуйте ещё\n")
            buy()
    except ValueError:
        clear()
        print(Fore.RED + "Неправильный ввод. Попробуйте ещё\n")
        buy()
def sell():
    global items, progress, player, tools
    
    food_sell_price, water_sell_price, coal_sell_price, wood_sell_price, iron_sell_price = 5, 5, 10, 10, 15
    axe_sell_price, pickaxe_sell_price, sword_sell_price = 20, 20, 20
    
    print(f"""
У тебя есть:
0. назад / отмена
1. яблоко - {items["Еда"]["Яблоко"]} | {food_sell_price} монет
2. вода - {items["Вода"]} | {water_sell_price} монет
3. уголь - {items["Уголь"]} | {coal_sell_price} монет
4. дерево - {items["Дерево"]} | {wood_sell_price} монет
5. железо - {items["Железо"]} | {iron_sell_price} монет
6. топор - {tools["Топор"]["Количество"]} | {axe_sell_price} монет
7. кирка - {tools["Кирка"]["Количество"]} | {pickaxe_sell_price} монет
8. меч - {tools["Меч"]["Количество"]} | {sword_sell_price} монет
    """)
    
    try:
        choice = int(input("Что хочешь продать? (номер тавара) "))
        if choice == 0:
            clear()
            shop()
        quantity = int(input("Сколько? "))
        if quantity == 0:
            clear()
            shop()
        
        if choice == 1:
            quantity = int(quantity)
            if quantity > items["Еда"]["Яблоко"]:
                print(Fore.RED + "У тебя нет столько яблок для продажи")
                sell()
            else:
                clear()
                items["Монеты"] += food_sell_price * quantity
                items["Еда"]["Яблоко"] -= quantity
                print(Fore.GREEN + f"Ты продал {quantity} еды за {food_sell_price * quantity} монет")
                autosave_game()
                sell()
        elif choice == 2:
            quantity = int(quantity)
            if quantity > items["Вода"]:
                print(Fore.RED + "У тебя нет столько воды для продажи")
                sell()
            else:
                clear()
                items["Монеты"] += water_sell_price * quantity
                items["Вода"] -= quantity
                print(Fore.GREEN + f"Ты продал {quantity} воды за {water_sell_price * quantity} монет")
                autosave_game()
                sell()
        elif choice == 3:
            quantity = int(quantity)
            if quantity > items["Уголь"]:
                print(Fore.RED + "У тебя нет столько угля для продажи")
                sell()
            else:
                clear()
                items["Монеты"] += coal_sell_price * quantity
                items["Уголь"] -= quantity
                print(Fore.GREEN + f"Ты продал {quantity} угля за {coal_sell_price * quantity} монет")
                autosave_game()
                sell()
        elif choice == 4:
            quantity = int(quantity)
            if quantity > items["Дерево"]:
                print(Fore.RED + "У тебя нет столько дерева для продажи")
                sell()
            else:
                clear()
                items["Монеты"] += wood_sell_price * quantity
                items["Дерево"] -= quantity
                print(Fore.GREEN + f"Ты продал {quantity} дерева за {wood_sell_price * quantity} монет")
                autosave_game()
                sell()
        elif choice == 5:
            quantity = int(quantity)
            if quantity > items["Железо"]:
                print(Fore.RED + "У тебя нет столько железа для продажи")
                sell()
            else:
                clear()
                items["Монеты"] += iron_sell_price * quantity
                items["Железо"] -= quantity
                print(Fore.GREEN + f"Ты продал {quantity} железа за {iron_sell_price * quantity} монет")
                autosave_game()
                sell()
        elif choice == 6:
            quantity = int(quantity)
            if quantity > tools["Топор"]["Количество"]:
                print(Fore.RED + "У тебя нет столько топоров для продажи")
                sell()
            else:
                clear()
                items["Монеты"] += axe_sell_price * quantity
                tools["Топор"]["Количество"] -= quantity
                if tools["Топор"]["Количество"] == 0:
                    tools["Топор"]["Прочность"] = 100
                print(Fore.GREEN + f"Ты продал {quantity} топоров за {axe_sell_price * quantity} монет")
                autosave_game()
                sell()
        elif choice == 7:
            quantity = int(quantity)
            if quantity > tools["Кирка"]["Количество"]:
                print(Fore.RED + "У тебя нет столько кирок для продажи")
                sell()
            else:
                clear()
                items["Монеты"] += pickaxe_sell_price * quantity
                tools["Кирка"]["Количество"] -= quantity
                if tools["Кирка"]["Количество"] == 0:
                    tools["Кирка"]["Прочность"] = 100
                print(Fore.GREEN + f"Ты продал {quantity} кирок за {pickaxe_sell_price * quantity} монет")
                autosave_game()
                sell()
        elif choice == 8:
            quantity = int(quantity)
            if quantity > tools["Меч"]["Количество"]:
                print(Fore.RED + "У тебя нет столько мечей для продажи")
                sell()
            else:
                clear()
                items["Монеты"] += quantity * sword_sell_price
                tools["Меч"]["Количество"] -= quantity
                if tools["Меч"]["Количество"] == 0:
                    tools["Меч"]["Прочность"] = 100
                print(Fore.GREEN + f"Ты продал {quantity} мечей за {sword_sell_price * quantity} монет")
                autosave_game()
                sell()
        else:
            clear()
            print(Fore.RED + "Неправильный ввод. Попробуйте ещё")
            sell()
    except ValueError:
        clear()
        print(Fore.RED + "Неправильный ввод. Попробуйте ещё\n")
        sell()