from rich import print
from rich.text import Text
from rich.panel import Panel
import inquirer

from utils import clear, load_game, save_game
from variables import version, theme
from parts.profile import profile
from parts.update_check import check_update


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
                #   ("Справка", "4")
            ],
        ),
    ]

    try:
        answers = inquirer.prompt(questions, theme=theme)
        choice = answers["choice"]
    except TypeError:
        save_game()
        exit()

    if choice == "1":
        profile()
    elif choice == "2":
        check_update()
        start_menu()
    elif choice == "3":
        load_game()
        profile()
    elif choice == "4":
        from parts.help import help

        help()


if __name__ == "__main__":
    start_menu()
