import random
import inquirer
from core import CraftDict

from utils import clear, alert, check_all, get_item, prompt

from config import game


class Craft:
    def __init__(self):
        pass

    def craft(self, item_name: str, progress_range: tuple):
        clear()

        item = get_item(item_name)
        if not item.craft:
            raise ValueError

        if all(get_item(i["name"]).quantity >= i["quantity"] for i in item.craft):
            alert(f"Вы создали {item_name.lower()}", "success")
            item.quantity += 1

            for i in item.craft:
                item_ = get_item(i["name"])
                item_.quantity -= i["quantity"]

            progress_count = random.uniform(*progress_range)
            game.player.xp += progress_count
            game.save()
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

    choice = prompt(questions)

    crafting = Craft()
    if choice == "0":
        clear()
        game.trigger("profile")
    elif choice == "1":
        crafting.craft(
            item_name="Топор",
            progress_range=(3.0, 5.0),
        )
    elif choice == "2":
        crafting.craft(
            item_name="Кирка",
            progress_range=(5.0, 8.0),
        )
    elif choice == "3":
        crafting.craft(
            item_name="Меч",
            progress_range=(5.0, 9.0),
        )
    elif choice == "4":
        crafting.craft(
            item_name="Ведро",
            progress_range=(5.0, 9.0),
        )
    elif choice == "5":
        crafting.craft(
            item_name="Лодка",
            progress_range=(5.0, 9.0),
        )
    elif choice == "6":
        crafting.craft(
            item_name="Удочка",
            progress_range=(5.0, 9.0),
        )

    game.trigger("craft")
