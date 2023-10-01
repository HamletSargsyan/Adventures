import random
from rich import print
import inquirer
from utils import clear, alert, check_all, save_game
from variables import player, items

@check_all
def lootbox_open():
    global items, player
    loot_table = list(items.keys())  # Получить список всех доступных предметов
    rarity_weights = {
        "Обычный": 4,   # Вес для обычных предметов
        "Редкий": 3,    # Вес для редких предметов
        "Необычный": 2, # Вес для необычных предметов
        "Эпический": 1  # Вес для эпических предметов
    }
    
    num_items_to_get = random.randint(1, 10)  # Генерируем случайное количество предметов
    
    items_to_get = random.choices(loot_table, k=num_items_to_get, weights=[rarity_weights[items[item]["Редкость"]] for item in loot_table])
    
    for item in items_to_get:
        quantity = int(random.uniform(1, 10))
        if quantity > 0:
            items[item]["Количество"] += quantity
            alert(f"+ {quantity} {item}", 'success', enter=False)
    alert("", enter=True)

    save_game()
    from .profile import profile
    profile()

@check_all
def lootbox_menu():
    clear()
    print("Хочешь открыть лутбокс?")
    options = [
        inquirer.List('choice',
                      message="Выберите опцию:",
                      choices=[
                          ("Да", "1"),
                          ("Нет", "2")
                      ]),
    ]
    
    try:
        answers = inquirer.prompt(options)
        choice = answers['choice']
    except TypeError:
        save_game()
        exit()

    if choice == "1":
        if items["Лутбокс"]['Количество'] >= 1:
            clear()
            lootbox_open()
        else:
            clear()
            alert("У тебя нет лутбокса", 'error')
    elif choice == "2":
        clear()
    
    from .profile import profile
    profile()
