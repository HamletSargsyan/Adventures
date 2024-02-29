from utils import clear, prompt

from rich import print
from rich.panel import Panel
from rich.text import Text
import inquirer

from config import game


def items_help(): ...


def mobs_help(): ...


def locations_help(): ...


def craft_help(): ...


@game.on("help")
def help():
    clear()
    print(Panel(Text("Приветствую! Это справка для игры"), title="Справка"))

    questions = [
        inquirer.List(
            "choice",
            message="Выберите опцию:",
            choices=[
                ("Назад", "1"),
                ("Придметы", "2"),
                ("Мобы", "3"),
                ("Локации", "4"),
                ("Крафты", "5"),
            ],
        ),
    ]

    choice = prompt(questions)

    if choice == "1":
        game.trigger("start")
    elif choice == "2":
        items_help()
    elif choice == "3":
        mobs_help()
    elif choice == "4":
        locations_help()
    elif choice == "5":
        craft_help()
