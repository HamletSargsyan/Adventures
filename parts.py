import random
import os
import json
import sys
from variables import *
from colorama import init, Fore, Style, Back

init(autoreset=True)

def clear():
    _checks.check()
    os.system('cls' if os.name=='nt' else 'clear')

def autosave_game():
    _checks.check()
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
            health_max = game_data['health_max']
            level = game_data['level']
            progress = game_data['progress']
            player = game_data['player']
            items = game_data['items']
            tools = game_data['tools']
            

        print(Fore.GREEN + "Игра загружена.")
        _checks.check()
    except FileNotFoundError:
        print(Fore.RED + "Файл сохранения не найден.")
    _profile.profile()

def die():
    _checks.check()
    autosave_game()
    input("Нажмите Enter, чтобы выйти из игры.")
    sys.exit()

class _checks:
    def check():
        global items, progress, level, player, tools

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
        if tools["Меч"]["Прочность"] <= 0:
            tools["Меч"]["Количество"] -= 1
            tools["Меч"]["Прочность"] = 100
        if tools["Ведро"]["Прочность"] <= 0:
            tools["Ведро"]["Количество"] -= 1
            tools["Ведро"]["Прочность"] = 100
        if tools["Лодка"]["Прочность"] <= 0:
            tools["Лодка"]["Количество"] -= 1
            tools["Лодка"]["Прочность"] = 100
        if tools["Удочка"]["Прочность"] <= 0:
            tools["Удочка"]["Количество"] -= 1
            tools["Удочка"]["Прочность"] = 100
        if progress >= 100:
            level += 1
            progress = 0.0
            items["Лутбокс"] += 1
            clear()
            print(Fore.LIGHTGREEN_EX + f"Поздравляем! Твой уровень повышен до {level}")
            print("Ты получил 1 лутбокс")
            print()
            input("Нажми ENTER, чтобы продолжить...")
            clear()
            _profile.profile()
        if tools["Топор"]["Количество"] <= 0:
            tools["Топор"]["Количество"] = 0
        if tools["Кирка"]["Количество"] <= 0:
            tools["Кирка"]["Количество"] = 0
        if tools["Меч"]["Количество"] <= 0:
            tools["Меч"]["Количество"] = 0
        if tools["Ведро"]["Количество"] <= 0:
            tools["Ведро"]["Количество"] = 0
        if tools["Лодка"]["Количество"] <= 0:
            tools["Лодка"]["Количество"] = 0
        if tools["Удочка"]["Количество"] <= 0:
            tools["Удочка"]["Количество"] = 0
        
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

class _profile:
    def profile():
        global items, progress, level, player, tools
        _checks.check()
        
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
            _explore.explore()
        elif choice == "2":
            clear()
            _fight.fight()
        elif choice == "3":
            clear()
            _rest.rest()
        elif choice == "4":
            clear()
            _eat.eat()
        elif choice == "5":
            clear()
            _drink.drink()
        elif choice == "6":
            clear()
            _craft.craft()
        elif choice == "7":
            _lootbox.lootbox_menu()
        elif choice == "8":
            clear()
            load_game()
        elif choice == "9":
            clear()
            _shop.shop()    
        else:
            clear()
            print(Fore.RED + "Неправылный ввод. Попробуйте ещё")
            _profile.profile()

class _craft:
    def craft():
        global items, progress, player, tools
        print(Fore.WHITE + "Что вы хотите скрафтить?")
        print("""
        0. Назад
        1. Топор
        2. Кирка
        3. Меч
        4. Ведро
        5. Лодка
        6. Удочка
        """)
        choice = input()
        if choice == "0":
            clear()
            _profile.profile()
        elif choice == "1":
            if items["Дерево"] >= 5 and items["Железо"] >= 3:
                print(Fore.GREEN + "Вы создали топор")
                tools["Топор"]["Количество"] += 1
                items["Дерево"] -= 5
                items["Железо"] -= 3
                progress_count = random.uniform(3.0, 5.0)
                progress += progress_count
                autosave_game()
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
                autosave_game()
            else:
                print(Fore.RED + "Недостаточно материалов для создания кирки")
    
        elif choice == "3":
            if items["Железо"] >= 2 and items["Дерево"] >= 1:
                print(Fore.GREEN + "Вы создали меч")
                tools["Меч"]["Количество"] += 1
                items["Железо"] -= 2
                items["Дерево"] -= 1
                progress_count = random.uniform(5.0, 9.0)
                progress += progress_count
                autosave_game()
            else:
                print(Fore.RED + "Недостаточно материалов для создания меча")
        elif choice == "4":
            if items["Железо"] >= 3:
                print(Fore.GREEN + "Вы создали ведро")
                tools["Ведро"]["Количество"] += 1
                items["Железо"] -= 3
                progress_count = random.uniform(5.0, 9.0)
                progress += progress_count
                autosave_game()
            else:
                print(Fore.RED + "Недостаточно материалов для создания ведра")
        elif choice == "5":
            if items["Железо"] >= 2 and items["Дерево"] >= 5:
                print(Fore.GREEN + "Вы создали лодку")
                tools["Лодка"]["Количество"] += 1
                items["Дерево"] -= 5
                items["Железо"] -= 2
                progress_count = random.uniform(5.0, 9.0)
                progress += progress_count
                autosave_game()
            else:
                print(Fore.RED + "Недостаточно материалов для создания лодки")
        elif choice == "6":
            if items["Железо"] >= 5:
                print(Fore.GREEN + "Вы создали удочку")
                tools["Удочка"]["Количество"] += 1
                items["Железо"] -= 5
                progress_count = random.uniform(5.0, 9.0)
                progress += progress_count
                autosave_game()
            else:
                print(Fore.RED + "Недостаточно материалов для создания удочки")
        else:
            print(Fore.RED + "Неверный ввод. Попробуйте еще раз.")
            _craft.craft()
        autosave_game()
        _profile.profile()

class _drink:
    def drink():
        global items, progress, player, tools
        clear()
        if items["Вода"] < 1:
            print(Fore.RED + "Недостатично воды")
        elif items["Вода"] >= 1:
            if player["Жажда"] == 0:
                print(Fore.YELLOW + "Тебе ненужно пить")
            else:
                player["Жажда"] -= 10
                items["Вода"] -= 1
                print(Fore.LIGHTGREEN_EX + "Вы пьете воду и уменьшаете жажду")
        if player["Жажда"] < 0:
            player["Жажда"] = 0
        autosave_game()
        _profile.profile()

class _eat:
    def eat():
        global items, progress, player, tools
        clear()
        if items["Еда"]["Яблоко"] < 10:
            print(Fore.RED + "Недостатично еды")
        elif items["Еда"]["Яблоко"] >= 10:
            if player["Голод"] == 0:
                print(Fore.YELLOW + "Ты уже сыт")
            else:
                player["Голод"] -= 10
                items["Еда"]["Яблоко"] -= 1
                print(Fore.LIGHTGREEN_EX + "Вы съедаете еду и уменьшаете голод")
        if player["Голод"] < 0:
            player["Голод"] = 0
        autosave_game()
        _profile.profile()

class _explore:
    def explore():
        clear()
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
            clear()
            _profile.profile()
        elif choice == "1":
            clear()
            _explore.forest()
        elif choice == "2":
            clear()
            _explore.mineshaft()
        elif choice == "3":
            clear()
            _explore.well()
        elif choice == "4":
            clear()
            _explore.lake()

        else:
            clear()
            print(Fore.RED + "Неверный ввод. Попробуйте еще раз.")
            _explore.explore()

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
            clear()
            print(Fore.GREEN + f"Вы добили {wood_count} ед. дерево, {water_count} ед. воды и {food_count} ед. еды")
            autosave_game()
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
            tools["Топор"]["Прочность"] -= random.randint(5, 10)
            items["Вода"] += water_count
            items["Дерево"] += wood_count
            clear()
            autosave_game()
            print(Fore.GREEN + f"Вы добили {wood_count} ед. дерево, {water_count} ед. воды и {food_count} ед. еды, прочность топора: {tools['Топор']['Прочность']}%")
            _profile.profile()

    def mineshaft():
        global items, progress, player, tools
        if level >= 2:
            progress_count = random.uniform(2.0, 5.0)
            progress += progress_count
            if tools["Кирка"]["Количество"] == 0:
                iron_count = random.randint(1, 5)
                coal_count = random.randint(1, 5)
                coin_count = random.randint(5, 10)
                items["Железо"] += iron_count
                items["Уголь"] += coal_count

                player["Усталость"] += random.randint(10, 20)
                player["Голод"] += random.randint(10, 15)
                player["Жажда"] += random.randint(10, 15)

                items["Монеты"] += coin_count
                autosave_game()
                clear()
                print(Fore.GREEN + f"Вы добили {iron_count} ед. железа и {coal_count} ед. угля")
                _profile.profile()
            elif tools["Кирка"]["Количество"] > 0:
                iron_count = random.randint(20, 30)
                coal_count = random.randint(20, 30)
                coin_count = random.randint(5, 15)

                items["Железо"] += iron_count
                items["Уголь"] += coal_count
                tools["Кирка"]["Прочность"] -= random.randint(5, 1)

                player["Усталость"] += random.randint(10, 20)
                player["Голод"] += random.randint(10, 15)
                player["Жажда"] += random.randint(10, 15)

                items["Монеты"] += coin_count
                autosave_game()
                clear()
                print(Fore.GREEN + f'Вы добили {coal_count} ед. железа и {iron_count} ед. железа, прочность кирки: {tools["Кирка"]["Прочность"]}%')
                _profile.profile()
        elif level < 2:
            clear()
            print(Fore.RED + "Чтобы пойти в шахту нужен 2 уровень")
        _profile.profile()

    def well():
        global items, progress, player, tools
        if level >= 5 and tools["Ведро"]["Количество"] >= 1:

            progress_count = random.uniform(5.0, 10.0)
            progress += progress_count

            water_count = random.randint(10, 30)
            tools["Ведро"]["Прочность"] -= random.randint(10, 15)
            items["Вода"] += water_count
            player["Голод"] += random.randint(10, 20)
            player["Жажда"] += random.randint(10, 20)
            player["Усталость"] += random.randint(5, 15)

            print(Fore.GREEN + f"+ {water_count} ед. воды")
        elif level < 5:
            clear()
            print(Fore.RED + "Чтобы пойти к колодцу нужен 5 уровень")
        elif tools["Ведро"]["Количество"] == 0:
            clear()
            print(Fore.RED + "Чтобы пойти к колодцу нужен ведро")
        _profile.profile()

    def lake():
        global items, progress, player, tools
        if level >= 10 and tools["Лодка"]["Количество"] >= 1 and tools["Удочка"]["Количество"] >= 1:
            
            progress_count = random.uniform(10.0, 20.0)
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
            clear()
            print(Fore.RED + "Чтобы пойти в озеро нужен 10 уровень")
        elif tools["Лодка"]["Количество"] == 0:
            clear()
            print(Fore.RED + "Чтобы пойти в озеро нужна лодка")
        elif tools["Удочка"]["Количество"] == 0:
            print(Fore.RED + "Чтобы пойти в озеро нужна удочка")
        _profile.profile()

class _fight:
    def fight():
        global items, progress, player, tools
        progress_count = random.uniform(5.0, 7.0)
        progress += progress_count
        clear()
        print(Fore.LIGHTYELLOW_EX + "Вы вступаете в бой с монстром!")
        if tools["Меч"]["Количество"] == 0:
            damage_taken = random.randint(10, 20)
            coin_count  = random.randint(10, 20)
            food_count  = random.randint(10, 20)

            player["Здоровие"] -= damage_taken
            items["Монеты"] += coin_count
            items["Еда"]["Яблоко"] += food_count

            autosave_game()
            print(Fore.YELLOW + f"Вы теряете {damage_taken} здоровья")
            print(Fore.LIGHTGREEN_EX + f"Вы получили {coin_count} ед. монет и {food_count} ед. еды")
            print()
            _profile.profile()
        elif tools["Меч"]["Количество"] >= 0:
            damage_taken = random.randint(5, 10)
            coin_count  = random.randint(20, 30)
            food_count  = random.randint(20, 30)

            player["Здоровие"] -= damage_taken
            items["Монеты"] += coin_count
            items["Еда"]["Яблоко"] += food_count

            tools["Меч"]["Прочность"] -= random.randint(10, 25)
            autosave_game()
            print(Fore.YELLOW + f"Вы теряете {damage_taken} здоровья.")
            print(Fore.LIGHTGREEN_EX + f"Вы получили {coin_count} ед. монет и {food_count} ед. еды")
            print()
            _profile.profile()

class _lootbox:
    def lootbox_open():
        global items, progress, player, tools
        loots = ["монеты", "дерево", "вода", "яблоко", "железо", "уголь", "топор", "кирка", "меч"]

        items["Лутбокс"] -= 1
        print(Fore.LIGHTGREEN_EX + "Ты открыл лутбокс и получил:")
        print()
        for i in range(random.randint(1, 5)):
            loot = random.choice(loots)
            quantity = random.randint(1, 10)
            print(f"{loot}: {quantity}".capitalize())
            if loot == "монеты":
                items["Монеты"] += quantity
            elif loot == "дерево":
                items["Дерево"] += quantity
            elif loot == "вода":
                items["Вода"] += quantity
            elif loot == "яблоко":
                items["Еда"]["Яблоко"] += quantity
            elif loot == "железо":
                items["Железо"] += quantity
            elif loot == "уголь":
                items["Уголь"] += quantity
            elif loot == "топор":
                tools["Топор"]["Количество"] += 1
            elif loot == "кирка":
                tools["Кирка"]["Количество"] += 1
            elif loot == "меч":
                tools["Меч"]["Количество"] += 1
            autosave_game()
        print()
        input("Нажми ENTER, чтобы продолжить...")
        clear()
        _profile.profile()

    def lootbox_menu():
        clear()
        print("Хочешь открить лутбокс?")
        print("""
        1. да
        2. нет
        """)
        choice = input().lower()

        if choice == "1":
            if items["Лутбокс"] >= 1:
                clear()
                _lootbox.lootbox_open()
            else:
                clear()
                print(Fore.RED + "У тебя нет лутбокса")
                _profile.profile()
        elif choice == "2":
            clear()
            _profile.profile()
        else:
            clear()
            print(Fore.RED + "Неправылный ввод. Попробуйте ещё")
            _lootbox.lootbox_menu()

class _rest:
    def rest():
        global items, progress, player, tools
        clear()
        health_gain = random.randint(5, 10)
        fatigue_reduction = random.randint(5, 15)

        player["Здоровие"] += health_gain
        player["Усталость"] -= fatigue_reduction

        print(Fore.LIGHTGREEN_EX + f"Вы отдыхаете и восстанавливаете {health_gain} здоровья и уменьшаете усталость на {fatigue_reduction}")
        print()
        if player["Усталость"] < 0:
            player["Усталость"] = 0
        if player["Здоровие"] > health_max:
            player["Здоровие"] = health_max
        autosave_game()
        _profile.profile()

class _shop:
    def shop():
        print(Fore.GREEN + "Добро пожаловать в магазин\n")
        print("Что будем делать?\n"
            "1. Купить\n"
            "2. Продать\n"
            "3. Назад\n")
        choice = input().lower()

        if choice == "1":
            clear()
            _shop.buy()
        elif choice == "2":
            clear()
            _shop.sell()
        elif choice == "3":
            clear()
            _profile.profile()
        else:
            print("Неправильный ввод. Попробуйте ещё\n")
            _shop.shop()


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
            global choice, quantity
            choice = int(input("\nЧто хочешь купить? (номер тавара) "))

            if choice == 0:
                clear()
                _shop.shop()

            quantity = int(input("Сколько? "))

            if quantity == 0:
                clear()
                _shop.shop()

            elif choice == 1:
                if items["Монеты"] >= food_price * int(quantity):
                    clear()
                    items["Монеты"] -= food_price * int(quantity) 
                    items["Еда"]["Яблоко"] += int(quantity) 
                    print(Fore.GREEN + f"Ты купил {quantity} еды за {food_price * int(quantity)} монет\n")
                    _shop.buy()
                else:
                    print(Fore.RED + "Недостаточно монет\n")
                    _shop.buy()
            elif choice == 2:
                if items["Монеты"] >= water_price * int(quantity):
                    clear()
                    items["Монеты"] -= water_price * int(quantity)
                    items["Вода"] += int(quantity)
                    print(Fore.GREEN + f"Ты купил {quantity} воды за {water_price * int(quantity)} монет\n")
                    autosave_game()
                    _shop.buy()
                else:
                    print(Fore.RED + "Недостаточно монет\n")
                    _shop.buy()
            elif choice == 3:
                if items["Монеты"] >= coal_price * int(quantity):
                    clear()
                    items["Монеты"] -= coal_price * int(quantity)
                    items["Уголь"] += int(quantity)
                    print(Fore.GREEN + f"Ты купил {quantity} уголья за {coal_price * int(quantity)} монет\n")
                    autosave_game()
                    _shop.buy()
                else:
                    print(Fore.RED + "Недостаточно монет\n")
                    _shop.buy()
            elif choice == 4:
                if items["Монеты"] >= wood_price * int(quantity):
                    clear()
                    items["Монеты"] -= wood_price * int(quantity)
                    items["Дерево"] += int(quantity)
                    print(Fore.GREEN + f"Ты купил {quantity} дерева за {wood_price * int(quantity)} монет\n")
                    autosave_game()
                    _shop.buy()
                else:
                    print(Fore.RED + "Недостаточно монет\n")
                    _shop.buy()
            elif choice == 5:
                if items["Монеты"] >= iron_price * int(quantity):
                    clear()
                    items["Монеты"] -= iron_price * int(quantity)
                    items["Железо"] += int(quantity)
                    print(Fore.GREEN + f"Ты купил {quantity} железа за {iron_price * int(quantity)} монет\n")
                    autosave_game()
                    _shop.buy()
                else:
                    print(Fore.RED + "Недостаточно монет\n")
                    _shop.buy()
            elif choice == 6:
                if items["Монеты"] >= axe_price * int(quantity):
                    clear()
                    items["Монеты"] -= axe_price * int(quantity)
                    tools["Топор"]["Количество"] += int(quantity)
                    print(Fore.GREEN + f"Ты купил {quantity} топор(ов) за {axe_price * int(quantity)} монет\n")
                    autosave_game()
                    _shop.buy()
                else:
                    print(Fore.RED + "Недостаточно монет\n")
                    _shop.buy()
            elif choice == 7:
                if items["Монеты"] >= pickaxe_price * int(quantity):
                    clear()
                    items["Монеты"] -= pickaxe_price * int(quantity)
                    tools["Кирка"]["Количество"] += int(quantity)
                    print(Fore.GREEN + f"Ты купил {quantity} кирку(и) за {pickaxe_price * int(quantity)} монет\n")
                    autosave_game()
                    _shop.buy()
                else:
                    print(Fore.RED + "Недостаточно монет\n")
                    _shop.buy()
            elif choice == 8:
                if items["Монеты"] >= sword_price * int(quantity):
                    clear()
                    items["Монеты"] -= sword_price * int(quantity)
                    tools["Меч"]["Количество"] += int(quantity)
                    print(Fore.GREEN + f"Ты купил {quantity} меч(а) за {sword_price * int(quantity)} монет\n")
                    autosave_game()
                    _shop.buy()
                else:
                    print(Fore.RED + "Недостаточно монет\n")
                    _shop.buy()
            elif choice == 9:
                if items["Монеты"] >= lootbox_price * int(quantity):
                    clear()
                    items["Монеты"] -= lootbox_price * int(quantity)
                    items["Лутбокс"] += int(quantity)
                    print(Fore.GREEN + f"Ты купил {quantity} лутбокс(ов) за {lootbox_price * int(quantity)} монет\n")
                    autosave_game()
                    _shop.buy()
                else:
                    print(Fore.RED + "Недостаточно монет\n")
                    _shop.buy()
            else:
                clear()
                print(Fore.RED + "Неправильный ввод. Попробуйте ещё\n")
                _shop.buy()
        except ValueError:
            clear()
            print(Fore.RED + "Неправильный ввод. Попробуйте ещё\n")
            _shop.buy()

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
                _shop.shop()

            quantity = int(input("Сколько? "))

            if quantity == 0:
                clear()
                _shop.shop()
            
            if choice == 1:
                quantity = int(quantity)
                if quantity > items["Еда"]["Яблоко"]:
                    print(Fore.RED + "У тебя нет столько яблок для продажи")
                    _shop.sell()
                else:
                    clear()
                    items["Монеты"] += food_sell_price * quantity
                    items["Еда"]["Яблоко"] -= quantity
                    print(Fore.GREEN + f"Ты продал {quantity} еды за {food_sell_price * quantity} монет")
                    autosave_game()
                    _shop.sell()
            elif choice == 2:
                quantity = int(quantity)
                if quantity > items["Вода"]:
                    print(Fore.RED + "У тебя нет столько воды для продажи")
                    _shop.sell()
                else:
                    clear()
                    items["Монеты"] += water_sell_price * quantity
                    items["Вода"] -= quantity
                    print(Fore.GREEN + f"Ты продал {quantity} воды за {water_sell_price * quantity} монет")
                    autosave_game()
                    _shop.sell()
            elif choice == 3:
                quantity = int(quantity)
                if quantity > items["Уголь"]:
                    print(Fore.RED + "У тебя нет столько угля для продажи")
                    _shop.sell()
                else:
                    clear()
                    items["Монеты"] += coal_sell_price * quantity
                    items["Уголь"] -= quantity
                    print(Fore.GREEN + f"Ты продал {quantity} угля за {coal_sell_price * quantity} монет")
                    autosave_game()
                    _shop.sell()
            elif choice == 4:
                quantity = int(quantity)
                if quantity > items["Дерево"]:
                    print(Fore.RED + "У тебя нет столько дерева для продажи")
                    _shop.sell()
                else:
                    clear()
                    items["Монеты"] += wood_sell_price * quantity
                    items["Дерево"] -= quantity
                    print(Fore.GREEN + f"Ты продал {quantity} дерева за {wood_sell_price * quantity} монет")
                    autosave_game()
                    _shop.sell()
            elif choice == 5:
                quantity = int(quantity)
                if quantity > items["Железо"]:
                    print(Fore.RED + "У тебя нет столько железа для продажи")
                    _shop.sell()
                else:
                    clear()
                    items["Монеты"] += iron_sell_price * quantity
                    items["Железо"] -= quantity
                    print(Fore.GREEN + f"Ты продал {quantity} железа за {iron_sell_price * quantity} монет")
                    autosave_game()
                    _shop.sell()
            elif choice == 6:
                quantity = int(quantity)
                if quantity > tools["Топор"]["Количество"]:
                    print(Fore.RED + "У тебя нет столько топоров для продажи")
                    _shop.sell()
                else:
                    clear()
                    items["Монеты"] += axe_sell_price * quantity
                    tools["Топор"]["Количество"] -= quantity
                    if tools["Топор"]["Количество"] == 0:
                        tools["Топор"]["Прочность"] = 100
                    print(Fore.GREEN + f"Ты продал {quantity} топоров за {axe_sell_price * quantity} монет")
                    autosave_game()
                    _shop.sell()
            elif choice == 7:
                quantity = int(quantity)
                if quantity > tools["Кирка"]["Количество"]:
                    print(Fore.RED + "У тебя нет столько кирок для продажи")
                    _shop.sell()
                else:
                    clear()
                    items["Монеты"] += pickaxe_sell_price * quantity
                    tools["Кирка"]["Количество"] -= quantity
                    if tools["Кирка"]["Количество"] == 0:
                        tools["Кирка"]["Прочность"] = 100
                    print(Fore.GREEN + f"Ты продал {quantity} кирок за {pickaxe_sell_price * quantity} монет")
                    autosave_game()
                    _shop.sell()
            elif choice == 8:
                quantity = int(quantity)
                if quantity > tools["Меч"]["Количество"]:
                    print(Fore.RED + "У тебя нет столько мечей для продажи")
                    _shop.sell()
                else:
                    clear()
                    items["Монеты"] += quantity * sword_sell_price
                    tools["Меч"]["Количество"] -= quantity
                    if tools["Меч"]["Количество"] == 0:
                        tools["Меч"]["Прочность"] = 100
                    print(Fore.GREEN + f"Ты продал {quantity} мечей за {sword_sell_price * quantity} монет")
                    autosave_game()
                    _shop.sell()
            else:
                clear()
                print(Fore.RED + "Неправильный ввод. Попробуйте ещё")
                _shop.sell()
        except ValueError:
            clear()
            print(Fore.RED + "Неправильный ввод. Попробуйте ещё\n")
            _shop.sell()

if __name__ == "__main__":
    _start_menu.start_menu()