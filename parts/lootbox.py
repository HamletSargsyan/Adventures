import random
from rich import print
import inquirer
from utils import clear, alert, check_all, save_game
from variables import player, items
from rich.console import Console


@check_all
def lootbox_open():
    global items, player

    items["Лутбокс"]["Количество"] -= 1

    loot_table = list(items.keys())  # Получить список всех доступных предметов
    rarity_weights = {
        "Обычный": 6,   # Увеличенный вес для обычных предметов
        "Редкий": 3,    # Вес для редких предметов
        "Необычный": 2, # Вес для необычных предметов
        "Эпический": 1  # Вес для эпических предметов
    }
    
    num_items_to_get = random.randint(1, 10)  # Генерируем случайное количество предметов
    
    items_to_get = random.choices(loot_table, k=num_items_to_get, weights=[rarity_weights[items[item]["Редкость"]] for item in loot_table])
    
    console = Console()  # Создаем объект консоли rich
    
    for item in items_to_get:
        quantity = 0  # Изначально количество устанавливаем в 0
        
        # Устанавливаем максимальное количество для каждой редкости предмета
        if items[item]["Редкость"] == "Обычный":
            quantity = random.randint(1, 5)  # Максимальное количество для обычных предметов
        elif items[item]["Редкость"] == "Редкий":
            quantity = random.randint(1, 3)  # Максимальное количество для редких предметов
        elif items[item]["Редкость"] == "Необычный":
            quantity = random.randint(1, 2)  # Максимальное количество для необычных предметов
        elif items[item]["Редкость"] == "Эпический":
            quantity = 1  # Максимальное количество для эпических предметов
        
        if quantity > 0:
            items[item]["Количество"] += quantity
            
            #TODO Добавить в версии v2.0.2
            # rarity_color = {
            #     "Обычный": "green",
            #     "Редкий": "blue",
            #     "Необычный": "yellow",
            #     "Эпический": "magenta"
            # }

            rarity_color = {
                "Обычный": "green",
                "Редкий": "green",
                "Необычный": "green",
                "Эпический": "green"
            }
            
            # Форматируем сообщение с учетом цвета редкости
            message = f"+ [{rarity_color[items[item]['Редкость']]}]{quantity} {item}[/{rarity_color[items[item]['Редкость']]}]"
            
            # Выводим сообщение с цветом
            console.print(message)
    
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
