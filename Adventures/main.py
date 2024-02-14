from rich import print
from rich.text import Text
from rich.panel import Panel
import inquirer


from utils import clear, load_game, save_game, check_all
from variables import version, theme

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
            subtitle=f"{version}",
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

    try:
        answers = inquirer.prompt(questions, theme=theme)
        choice = answers["choice"]  # pyright: ignore
    except TypeError:
        save_game()
        exit()

    if choice == "1":
        game.trigger("profile")
    elif choice == "2":
        game.trigger("check_update")
    elif choice == "3":
        load_game()
        game.trigger("profile")
    elif choice == "4":
        game.trigger("help")


if __name__ == "__main__":
    game.run()