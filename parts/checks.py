import random

from utils import clear, alert, die, level_up, save_game
from variables import health_max, hunger_max, thirst_max, fatigue_max, player, items

def check():
    global items, player, health_max, hunger_max, thirst_max, fatigue_max
    

    if player["Здоровье"] >= health_max:
        player["Здоровье"] = health_max
    if player["Голод"] >= hunger_max:
        player["Голод"] = hunger_max
    if player["Жажда"] >= thirst_max:
        player["Жажда"] = thirst_max
    if player["Усталость"] >= fatigue_max:
        player["Усталость"] = fatigue_max
    if player["Уровень"] < 0:
        player["Уровень"] = 0

    if player["Здоровье"] < 0:
        player["Здоровье"] = 0
    if player["Голод"] < 0:
        player["Голод"] = 0
    if player["Жажда"] < 0:
        player["Жажда"] = 0
    if player["Усталость"] < 0:
        player["Усталость"] = 0
    if player["Уровень"] < 0:
        player["Уровень"] = 0

    if player["Усталость"] >= fatigue_max:
        player["Здоровье"] -= random.randint(1, 5)
    if player["Голод"] >= hunger_max:
        player["Здоровье"] -= random.randint(1, 5)
    if player["Жажда"] >= thirst_max:
        player["Здоровье"] -= random.randint(1, 5)
    if player["Здоровье"] <= 0:
        die()

    if player['Опыт'] >= 100:
        player['Уровень'] += 1
        player['Опыт'] = 0.0
        lootbox_quantity = random.randint(1, 3)
        items["Лутбокс"]['Количество'] += lootbox_quantity
        clear()
        alert(f"[bright_green]Поздравляем! Ваш уровень повышен до {player['Уровень']}[/bright_green]", 'success')
        alert(f"Вы получили {lootbox_quantity} лутбокс", 'success')
        
        #  https://github.com/HamletSargsyan/Adventures/issues/9
        # level_up()

    if items["Топор"]["Прочность"] <= 0:
        items["Топор"]["Количество"] -= 1
        items["Топор"]["Прочность"] = 20
    if items["Кирка"]["Прочность"] <= 0:
        items["Кирка"]["Количество"] -= 1
        items["Кирка"]["Прочность"] = 20
    if items["Меч"]["Прочность"] <= 0:
        items["Меч"]["Количество"] -= 1
        items["Меч"]["Прочность"] = 25
    if items["Ведро"]["Прочность"] <= 0:
        items["Ведро"]["Количество"] -= 1
        items["Ведро"]["Прочность"] = 10
    if items["Лодка"]["Прочность"] <= 0:
        items["Лодка"]["Количество"] -= 1
        items["Лодка"]["Прочность"] = 40
    if items["Удочка"]["Прочность"] <= 0:
        items["Удочка"]["Количество"] -= 1
        items["Удочка"]["Прочность"] = 10

        
    if items["Топор"]["Количество"] <= 0:
        items["Топор"]["Количество"] = 0
    if items["Кирка"]["Количество"] <= 0:
        items["Кирка"]["Количество"] = 0
    if items["Меч"]["Количество"] <= 0:
        items["Меч"]["Количество"] = 0
    if items["Ведро"]["Количество"] <= 0:
        items["Ведро"]["Количество"] = 0
    if items["Лодка"]["Количество"] <= 0:
        items["Лодка"]["Количество"] = 0
    if items["Удочка"]["Количество"] <= 0:
        items["Удочка"]["Количество"] = 0
    
    save_game()
