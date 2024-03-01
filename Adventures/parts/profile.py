from rich import print
from rich.panel import Panel

import inquirer

from utils import clear, check_all, prompt
from config import game


@game.on("profile")
@check_all
def profile():
    clear()

    player_status = (
        f'{"[bright_red]Здоровье:[/bright_red]" if game.player.health <= 10 else "Здоровье:"} {game.player.health}/{game.player.health_max}\n'
        f"Голод: {game.player.hunger}/{game.player.hunger_max}\n"
        f"Жажда: {game.player.thirst}/{game.player.thirst_max}\n"
        f"Усталость: {game.player.fatigue}/{game.player.fatigue_max}\n"
        f"Уровень: {game.player.level}\n"
        f"Опыт: {game.player.xp:.1f}%/100%"
    )

    print(
        Panel.fit(
            player_status, title="[bold bright_green]Статус игрока[/bold bright_green]"
        )
    )

    questions = [
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

    choice = prompt(questions)

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
