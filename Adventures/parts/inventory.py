from rich import print
from rich.panel import Panel

import inquirer

from utils import clear, check_all, prompt
from config import game


@game.on("inventory")
@check_all
def inventory():
    clear()
    # Сортируем предметы по количеству в убывающем порядке
    sorted_items = sorted(game.player.inventory, key=lambda x: x.quantity, reverse=True)

    player_items = ""
    # Цикл для вывода предметов игрока, если их количество больше 0
    for index, item in enumerate(sorted_items):
        if item.quantity > 0:
            player_items += f"{item.name}: {item.quantity:.0f}{f' | Прочность: ' + str(item.strength) if item.strength and item.strength > 0 else ''}"
            if index < len(sorted_items) - 1:
                player_items += "\n"

    print(
        Panel.fit(player_items, title="[bold bright_green]Предметы[/bold bright_green]")
    )

    questions = [
        inquirer.List(
            "choice",
            message="Выберите опцию:",
            choices=[("Назад в профиль", "1"), ("Открыть лутбокс", "2")],
        ),
    ]

    choice = prompt(questions)

    if choice == "1":
        game.trigger("profile")
    elif choice == "2":
        game.trigger("lootbox_menu")
