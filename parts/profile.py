from rich import print
from rich.panel import Panel

import inquirer

from utils import clear, check_all, save_game
from variables import player
from .inventory import inventory

@check_all
def profile():
    clear()

    player_status = (f'{"[bright_red]Здоровье:[/bright_red]" if player["Здоровье"] <= 10 else "Здоровье:"} {player["Здоровье"]}\n'
                     f'Голод: {player["Голод"]}\n'
                     f'Жажда: {player["Жажда"]}\n'
                     f'Усталость: {player["Усталость"]}\n'
                     f'Уровень: {player["Уровень"]}\n'
                     f'Опыт: {player["Опыт"]:.1f}%/100%\n'  # Исправлено: Опит -> Опыт
                     )

    print(Panel.fit(player_status, title="[bold bright_green]Статус игрока[/bold bright_green]"))


    # Создайте список опций для inquirer
    options = [
        inquirer.List('choice',
                      message="Выберите опцию:",
                      choices=[
                          ("Инвентарь", "1"),
                          ("Исследование", "2"),  # Исправлено: Иследование -> Исследование
                          ("Верстак", "3"),
                          ("Магазин", "4"),
                          ("Отдых", "5"),
                          ("Еда", "6"),
                          ("Открыть лутбокс", "7")
                      ]),
    ]
    
    try:
        answers = inquirer.prompt(options)
        choice = answers['choice']
    except TypeError:
        save_game()
        exit()

    if choice == '1':
        inventory()
    elif choice == '2':
        from .explore import explore
        explore()
    elif choice == '3':
        from .crafting_table import craft
        craft()
    elif choice == '4':
        from .shop import shop
        shop()
    elif choice == '5':
        from .recovery import recovery
        recovery()
    elif choice == '6':
        from .recovery import food
        food()
    elif choice == '7':
        from .lootbox import lootbox_menu
        lootbox_menu()
