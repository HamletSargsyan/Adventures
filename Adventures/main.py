import sys

if sys.version_info < (3, 8):
    print(f"Игра работает с версии python 3.8 и выше. У вас {sys.version}")
    exit(1)

from rich import print
from rich.text import Text
from rich.panel import Panel
import inquirer


from utils import clear, check_all, prompt

from parts import achievements
from parts import crafting_table
from parts import explore
from parts import help
from parts import inventory
from parts import lootbox
from parts import profile
from parts import recovery
from parts import shop
from parts import update_check
from config import game


@game.on("start")
@check_all
def start_menu():
    clear()
    print(
        Panel(
            Text("\nДобро пожаловать в ADVENTURES\n", justify="center"),
            subtitle=f"{game.config.version}",
        )
    )

    questions = [
        inquirer.List(
            "choice",
            message="Выберите опцию:",
            choices=[
                ("Играть", "1"),
                ("Обновления", "2"),
                ("Выгрузить", "3"),
                # ("Справка", "4")
            ],
        ),
    ]

    choice = prompt(questions)

    if choice == "1":
        game.trigger("profile")
    elif choice == "2":
        game.trigger("check_update")
    elif choice == "3":
        game.load()
        game.trigger("profile")
    elif choice == "4":
        game.trigger("help")


if __name__ == "__main__":
    game.run()
