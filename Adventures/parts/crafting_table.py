import random
import inquirer

from utils import clear, alert, save_game, check_all
from variables import player, items, theme

from config import game


class Craft:
    def __init__(self):
        self.items = items
        self.player = player

    def craft_tool(
        self, item_name: str, progress_range: tuple, required_materials: dict
    ):
        clear()
        if all(
            items[material]["Количество"] >= amount
            for material, amount in required_materials.items()
        ):
            alert(f"Вы создали {item_name.lower()}", "success")
            items[item_name]["Количество"] += 1

            for material, amount in required_materials.items():
                items[material]["Количество"] -= amount

            progress_count = random.uniform(*progress_range)
            player["Опыт"] += progress_count  # Заменил "Опит" на "Опыт"
            save_game()
        else:
            alert(f"Недостаточно материалов для создания {item_name.lower()}", "error")

    def craft_item(
        self, item_name: str, progress_range: tuple, required_materials: dict
    ):
        clear()
        if all(
            items[material]["Количество"] >= amount
            for material, amount in required_materials.items()
        ):
            alert(f"Вы создали {item_name.lower()}", "success")
            items[item_name]["Количество"] += 1

            for material, amount in required_materials.items():
                items[material]["Количество"] -= amount

            progress_count = random.uniform(*progress_range)
            player["Опыт"] += progress_count  # Заменил "Опит" на "Опыт"
            save_game()
        else:
            alert(f"Недостаточно материалов для создания {item_name.lower()}", "error")


@game.on("craft")
@check_all
def craft():
    clear()
    questions = [
        inquirer.List(
            "choice",
            message="Что вы хотите скрафтить?",
            choices=[
                ("Назад", "0"),
                ("Топор", "1"),
                ("Кирка", "2"),
                ("Меч", "3"),
                ("Ведро", "4"),
                ("Лодка", "5"),
                ("Удочка", "6"),
            ],
        ),
    ]
    try:
        answers = inquirer.prompt(questions, theme=theme)
        choice = answers["choice"]  # pyright: ignore
    except TypeError:
        save_game()
        exit()

    crafting = Craft()
    if choice == "0":
        clear()
        game.trigger("profile")
    elif choice == "1":
        crafting.craft_tool(
            item_name="Топор",
            progress_range=(3.0, 5.0),
            required_materials=items["Топор"]["Изготовление"],
        )
    elif choice == "2":
        crafting.craft_tool(
            item_name="Кирка",
            progress_range=(5.0, 8.0),
            required_materials=items["Кирка"]["Изготовление"],
        )
    elif choice == "3":
        crafting.craft_tool(
            item_name="Меч",
            progress_range=(5.0, 9.0),
            required_materials=items["Меч"]["Изготовление"],
        )
    elif choice == "4":
        crafting.craft_tool(
            item_name="Ведро",
            progress_range=(5.0, 9.0),
            required_materials=items["Ведро"]["Изготовление"],
        )
    elif choice == "5":
        crafting.craft_tool(
            item_name="Лодка",
            progress_range=(5.0, 9.0),
            required_materials=items["Лодка"]["Изготовление"],
        )
    elif choice == "6":
        crafting.craft_tool(
            item_name="Удочка",
            progress_range=(5.0, 9.0),
            required_materials=items["Удочка"]["Изготовление"],
        )

    game.trigger("craft")
