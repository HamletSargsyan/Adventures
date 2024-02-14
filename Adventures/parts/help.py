from variables import theme
from utils import alert, clear

from rich import print
from rich.panel import Panel
from rich.text import Text
from rich.table import Table
from rich.console import Console
import inquirer


def items_help(): ...


def mobs_help(): ...


def locations_help(): ...


def craft_help(): ...


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

    try:
        answers = inquirer.prompt(questions, theme=theme)
        choice = answers["choice"]  # pyright: ignore
    except TypeError:
        exit()

    if choice == "1":
        from main import start_menu

        start_menu()
    elif choice == "2":
        items_help()
    elif choice == "3":
        mobs_help()
    elif choice == "4":
        locations_help()
    elif choice == "5":
        craft_help()
