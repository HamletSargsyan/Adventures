import os
import pickle
import random
from typing import Union, NoReturn, Any

import inquirer

from rich import print
from Adventures.core import Item

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

    game.player.health = health_max - random.randint(30, 50)
    game.player.hunger = 0
    game.player.fatigue = 0
    game.player.thirst = 0
    
    items["Монеты"]["Количество"] -= 100

    save_game()
    clear()

    if message:
        alert(message, "error")
    else:
        alert("Ты погиб...", "error")
    clear()
    alert("Ты вернулся к жизни\n\nПостарайся не умереть в следующий раз!", "warning")

    game.trigger("profile")


def check_all(func):
    def wrapper():
        try:
            from parts.checks import check

            check()
            func()
            save_game()
        except RecursionError:
            pass
        except KeyboardInterrupt as e:
            clear()
            save_game()
            alert("Выход из игры", "warning", enter=False)
            exit()
        except Exception as e:
            ...  # TODO

    return wrapper


@check_all
def level_up():
    global health_max, damage_max, protection_max, hunger_max, thirst_max, fatigue_max
    from parts.profile import profile

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

    try:
        answers = inquirer.prompt(questions, theme=theme)
        choice = answers["choice"]  # pyright: ignore
    except TypeError:
        save_game()
        exit()

    if choice == "1":
        health_max = health_max + 10
        save_game()
        alert("+10 к Здоровью")
    elif choice == "2":
        hunger_max = hunger_max + 10
        save_game()
        alert("+10 к Голоду")
    elif choice == "3":
        thirst_max = thirst_max + 10
        save_game()
        alert("+10 к Жажде")
    elif choice == "4":
        fatigue_max = fatigue_max + 10
        save_game()
        alert("+10 к Усталости")
    elif choice == "5":
        damage_max = damage_max + 1
        save_game()
        alert("+1 к Урону")
    elif choice == "6":
        protection_max = protection_max + 1
        save_game()
        alert("+1 к Защите")

    save_game()
    game.trigger("profile")


@check_all
def get_item(name: str) -> Union[Item, None]:
    for item in items.value:
        if name == item.name:
            return item


@check_all
def prompt(questions, choice: str = "choice") -> Union[Any, NoReturn]:
    try:
        answers = inquirer.prompt(questions)
        return answers[choice] # pyright: ignore
    except TypeError:
        game.trigger("exit_game")
