import random
import inquirer
from utils import clear, alert, save_game, check_all
from variables import health_max, player, items

@check_all
def recovery():
    global items, player

    clear()

    health_gain = random.randint(5, 10)
    fatigue_reduction = random.randint(5, 15)
    player["Здоровье"] += health_gain
    player["Усталость"] -= fatigue_reduction

    alert(f"Вы отдыхаете и восстанавливаете {health_gain} здоровья и уменьшаете усталость на {fatigue_reduction}", 'success')

    if player["Усталость"] < 0:
        player["Усталость"] = 0
    if player["Здоровье"] > health_max:
        player["Здоровье"] = health_max

    save_game()

    from .profile import profile
    profile()

@check_all
def food():
    global player

    clear()

    options = [
        inquirer.List('choice',
                      message="Выберите опцию:",
                      choices=[
                          ('Назад', '0'),
                          ('Яблоко', '1'),
                          ('Рыба', '2'),
                          ('Вода', '3'),
                      ],
                      ),
    ]

    try:
        answers = inquirer.prompt(options)
        choice = answers['choice']
    except TypeError:
        save_game()
        exit()

    from .profile import profile
    if choice == '0':
        profile()
    elif choice == '1':
        if player['Голод'] >= 1:
            if items['Яблоко']['Количество'] >= 1:
                player['Голод'] -= items['Яблоко']['Бонусы']['Питание']
                alert(f"-{items['Яблоко']['Бонусы']['Питание']} голода", 'success')
            else:
                alert('Недостаточно', 'error')
        else:
            alert('Ты не голоден', 'warning')
    elif choice == '2':
        if items['Рыба']['Количество'] >= 1:
            if player['Голод'] >= 1:
                player['Голод'] -= items['Рыба']['Бонусы']['Питание']
                alert(f"-{items['Рыба']['Бонусы']['Питание']} голода", 'success')
            else:
                alert('Недостаточно', 'error')
        else:
            alert('Ты не голоден', 'warning')
    elif choice == '3':
        if items['Вода']['Количество'] >= 1:
            if player['Жажда'] >= 1:
                player['Жажда'] -= items['Вода']['Бонусы']['Насыщенность водой']
                alert(f"-{items['Вода']['Бонусы']['Насыщенность водой']} жажды", 'success')
            else:
                alert('Недостаточно', 'error')
        else:
            alert('Тебе не нужно пить', 'warning')
    food()
