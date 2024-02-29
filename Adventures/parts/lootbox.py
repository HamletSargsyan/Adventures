import random
from rich import print
import inquirer
from utils import prompt
from Adventures.core import ItemRarity
from items import items
from utils import clear, alert, check_all
from rich.console import Console
from config import game


@game.on("open_lootbox")
@check_all
def open_lootbox():
    item = game.player.get_or_add_item("лутбокс")
    item.quantity -= 1

    rarity_weights = {"Обычный": 6, "Редкий": 4, "легендарный": 3, "Необычный": 2, "Эпический": 1}

    num_items_to_get = random.randint(1, 10)

    items_to_get = random.choices(
        items.value,
        k=num_items_to_get,
        weights=[rarity_weights[item.rarity.value] for item in items.value],
    )

    console = Console()

    for item in items_to_get:
        quantity = 0

        if item.rarity == ItemRarity.COMMON:
            quantity = random.randint(1, 5)
        elif item.rarity == ItemRarity.UNCOMMON:
            quantity = random.randint(1, 3)
        elif item.rarity == ItemRarity.RARE:
            quantity = random.randint(1, 2)
        elif item.rarity == ItemRarity.LEGENDARY:
            quantity = 1

        if quantity > 0:
            item.quantity += quantity

            # TODO Добавить в пользовтельскый модуль
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

            message = f"+ [{rarity_color[item.rarity.value]}]{quantity} {item.name}[/{rarity_color[item.rarity.value]}]"

            # Выводим сообщение с цветом
            console.print(message)

    alert("", enter=True)

    game.save()
    game.trigger("profile")


@game.on("lootbox_menu")
@check_all
def lootbox_menu():
    clear()
    print("Хочешь открыть лутбокс?")
    questions = [
        inquirer.List(
            "choice", message="Выберите опцию:", choices=[("Да", "1"), ("Нет", "2")]
        ),
    ]

    choice = prompt(questions)

    clear()
    if choice == "1":
        if game.player.get_or_add_item('лутбокс').quantity >= 1:
            game.trigger("open_lootbox")
        else:
            alert("У тебя нет лутбокса", "error")
    elif choice == "2":
        clear()

    game.trigger("profile")
