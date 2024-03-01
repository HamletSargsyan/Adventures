import os
import random
from typing import Union, NoReturn, Any

import inquirer

from rich import print
from core import Item

from items import items

from config import game


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def alert(text: str, level: str = "log", enter=True):
    if level == "log":
        print(f"[bright_white]{text}[/bright_white]")

    elif level == "warning":
        print(f"[bright_yellow]{text}[/bright_yellow]")

    elif level == "error":
        print(f"[bright_red]{text}[/bright_red]")

    elif level == "success":
        print(f"[bright_green]{text}[/bright_green]")

    else:
        level = "log"
        print(f"[bright_white]{text}[/bright_white]")

    if enter:
        input("Нажми ENTER, чтобы продолжить...")


@game.on("die")
def die(message: Union[str, None] = None):
    global items, player, items

    game.player.health = game.player.health_max - random.randint(30, 50)
    game.player.hunger = 0
    game.player.fatigue = 0
    game.player.thirst = 0

    game.player.get_or_add_item("монета").quantity -= 100  # pyright: ignore

    clear()

    if message:
        alert(message, "error")
    else:
        alert("Ты погиб...", "error")
    clear()
    alert("Ты вернулся к жизни\n\nПостарайся не умереть в следующий раз!", "warning")

    game.trigger("profile")


def check_all(func):
    def wrapper(*args, **kwargs):
        try:
            from parts.checks import check

            check()
            func()
            game.save()
        except RecursionError:
            pass
        except KeyboardInterrupt:
            clear()
            game.save()
            alert("Выход из игры", "warning", enter=False)
            exit()
        except Exception as e:
            raise e  # TODO

    return wrapper


@check_all
def level_up():
    clear()
    questions = [
        inquirer.List(
            "choice",
            message="Выбери, что будем улучшать:",
            choices=[
                ("Здоровье", "1"),
                ("Голод", "2"),
                ("Жажда", "3"),
                ("Усталость", "4"),
                ("Урон", "5"),
                ("Защита", "6"),
            ],
        ),
    ]

    choice = prompt(questions)

    if choice == "1":
        game.player.health_max += 10
        alert("+10 к Здоровью")
    elif choice == "2":
        game.player.hunger_max += 10
        alert("+10 к Голоду")
    elif choice == "3":
        game.player.thirst_max += 10
        alert("+10 к Жажде")
    elif choice == "4":
        game.player.fatigue_max += 10
        alert("+10 к Усталости")
    elif choice == "5":
        game.player.damage += 1
        alert("+1 к Урону")
    elif choice == "6":
        game.player.protection += 1
        alert("+1 к Защите")

    game.save()
    game.trigger("profile")


@check_all
def get_item(name: str) -> Union[Item, NoReturn]:
    for item in items.value:
        if name == item.name:
            return item
    raise ValueError


# @check_all
def prompt(questions, choice: str = "choice") -> Union[Any, NoReturn]:
    try:
        answers = inquirer.prompt(questions, theme=game.config.load_theme())
        return answers[choice]  # pyright: ignore
    except TypeError:
        game.trigger("exit_game")
