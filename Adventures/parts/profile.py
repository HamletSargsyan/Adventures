from rich import print
from rich.panel import Panel

import inquirer

from utils import clear, check_all, save_game
from variables import (
    player,
    items,
    health_max,
    hunger_max,
    thirst_max,
    fatigue_max,
    theme,
)
from .inventory import inventory
from config import game


@game.on("profile")
@check_all
def profile():
    global items, player, health_max, hunger_max, thirst_max, fatigue_max

    clear()

    player_status = (
        f'{"[bright_red]Здоровье:[/bright_red]" if player["Здоровье"] <= 10 else "Здоровье:"} {player["Здоровье"]}/{health_max}\n'
        f'Голод: {player["Голод"]}/{hunger_max}\n'
        f'Жажда: {player["Жажда"]}/{thirst_max}\n'
        f'Усталость: {player["Усталость"]}/{fatigue_max}\n'
        f'Уровень: {player["Уровень"]}\n'
        f'Опыт: {player["Опыт"]:.1f}%/100%\n'
    )

    print(
        Panel.fit(
            player_status, title="[bold bright_green]Статус игрока[/bold bright_green]"
        )
    )

    options = [
        inquirer.List(
            "choice",
            message="Выберите опцию:",
            choices=[
                ("Инвентарь", "1"),
                ("Исследование", "2"),
                ("Верстак", "3"),
                ("Магазин", "4"),
                ("Отдых", "5"),
                ("Еда", "6"),
                "Назад",
            ],
        ),
    ]

    try:
        answers = inquirer.prompt(options, theme=theme)
        choice = answers["choice"]  # pyright: ignore
    except TypeError:
        save_game()
        exit()

    if choice == "1":
        game.trigger("inventory")
    elif choice == "2":
        game.trigger("explore")
    elif choice == "3":
        game.trigger("craft")
    elif choice == "4":
        game.trigger("shop")
    elif choice == "5":
        game.trigger("recovery")
    elif choice == "6":
        game.trigger("foot")
    elif choice == "Назад":
        game.trigger("start")
