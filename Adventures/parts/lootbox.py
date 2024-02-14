import random
from rich import print
import inquirer
from utils import clear, alert, check_all, save_game
from variables import player, items, theme
from rich.console import Console
from config import game


@game.on("open_lootbox")
@check_all
def open_lootbox():
    global items, player

    items["Лутбокс"]["Количество"] -= 1

    loot_table = list(items.keys())
    rarity_weights = {"Обычный": 6, "Редкий": 3, "Необычный": 2, "Эпический": 1}

    num_items_to_get = random.randint(1, 10)

    items_to_get = random.choices(
        loot_table,
        k=num_items_to_get,
        weights=[rarity_weights[items[item]["Редкость"]] for item in loot_table],
    )

    console = Console()

    for item in items_to_get:
        quantity = 0

        if items[item]["Редкость"] == "Обычный":
            quantity = random.randint(1, 5)
        elif items[item]["Редкость"] == "Редкий":
            quantity = random.randint(1, 3)
        elif items[item]["Редкость"] == "Необычный":
            quantity = random.randint(1, 2)
        elif items[item]["Редкость"] == "Эпический":
            quantity = 1

        if quantity > 0:
            items[item]["Количество"] += quantity

            # TODO Добавить в версии v2.1.0 или раньше если возможно
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
                "Эпический": "green",
            }

            # Форматируем сообщение с учетом цвета редкости
            message = f"+ [{rarity_color[items[item]['Редкость']]}]{quantity} {item}[/{rarity_color[items[item]['Редкость']]}]"

            # Выводим сообщение с цветом
            console.print(message)

    alert("", enter=True)

    save_game()
    game.trigger("profile")


@game.on("lootbox_menu")
@check_all
def lootbox_menu():
    clear()
    print("Хочешь открыть лутбокс?")
    options = [
        inquirer.List(
            "choice", message="Выберите опцию:", choices=[("Да", "1"), ("Нет", "2")]
        ),
    ]

    try:
        answers = inquirer.prompt(options, theme=theme)
        choice = answers["choice"]  # pyright: ignore
    except TypeError:
        save_game()
        exit()

    if choice == "1":
        if items["Лутбокс"]["Количество"] >= 1:
            clear()
            game.trigger("open_lootbox")
        else:
            clear()
            alert("У тебя нет лутбокса", "error")
    elif choice == "2":
        clear()

    game.trigger("profile")
