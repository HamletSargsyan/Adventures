from rich import print
from rich.panel import Panel

import inquirer

from utils import clear, check_all, save_game
from variables import player, items

@check_all
def inventory():
    clear()
    global items, player  # Убрал дублирующееся объявление переменной 'items'
    # Сортируем предметы по количеству в убывающем порядке
    sorted_items = sorted(items.items(), key=lambda x: x[1]["Количество"], reverse=True)

    player_items = ""
    # Цикл для вывода предметов игрока, если их количество больше 0
    for index, (item_name, item_data) in enumerate(sorted_items):
        if item_data["Количество"] > 0:
            player_items += f"{item_name}: {item_data['Количество']:.0f}{f' | Прочность: ' + str(item_data['Прочность']) if item_data['Прочность'] > 0 else ''}"
            if index < len(sorted_items) - 1:
                player_items += '\n'

    print(Panel.fit(player_items, title="[bold bright_green]Предметы[/bold bright_green]"))

    options = [
        inquirer.List('choice',
                      message="Выберите опцию:",
                      choices=[
                          ("Назад в профиль", "1"),
                          ("Открыть лутбокс", "2")
                      ],
                      ),
    ]

    try:
        answers = inquirer.prompt(options)
        choice = answers['choice']
    except TypeError:
        save_game()
        exit()

    if choice == '1':
        from .profile import profile
        profile()
    elif choice == '2':
        from .lootbox import lootbox_menu
        lootbox_menu()