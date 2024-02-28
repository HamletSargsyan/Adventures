import os
import pickle
import random
from typing import Union

import inquirer

from rich import print
from Adventures.core import Item
from variables import (
    version,
    health_max,
    damage_max,
    protection_max,
    hunger_max,
    thirst_max,
    fatigue_max,
    player,
    # items,
    theme,
)
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


def save_game():
    global version, health_max, hunger_max, thirst_max, fatigue_max, damage_max, protection_max, player, items
    game_data = {
        "health_max": health_max,
        "hunger_max": hunger_max,
        "thirst_max": thirst_max,
        "fatigue_max": fatigue_max,
        "damage_max": damage_max,
        "protection_max": protection_max,
        "player": player,
        "items": items,
    }

    with open("saves/game_data.pickle", "wb") as f:
        pickle.dump(game_data, f)


def load_game():
    global version, health_max, protection_max, thirst_max, fatigue_max, damage_max, protection_max, player, items, items
    clear()
    try:
        with open("saves/game_data.pickle", "rb") as f:
            game_data = pickle.load(f)
            health_max = game_data["health_max"]
            protection_max = game_data["protection_max"]
            thirst_max = game_data["thirst_max"]
            fatigue_max = game_data["fatigue_max"]
            protection_max = game_data["protection_max"]
            player.update(game_data["player"])
            items.update(game_data["items"])

            alert("Игра загружена.", "success")

    except FileNotFoundError:
        alert("Файл сохранения не найден.", "error")


@game.on("die")
def die(message: Union[str, None] = None):
    global items, player, items

    player["Здоровье"] = health_max - random.randint(30, 50)
    player["Голод"] = 0
    player["Жажда"] = 0
    player["Усталость"] = 0
    player["Уровень"] = 0 if player["Уровень"] == 0 else player["Уровень"] - 1
    player["Опит"] = 0

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


def get_item(name: str) -> Item:
    for item in items:
        if name == item.name:
            return item