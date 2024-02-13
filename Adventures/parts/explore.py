import random
from rich import print
import inquirer
from utils import clear, alert, save_game, check_all
from variables import player, items, theme

from .profile import profile
from .mobs import generate_forest_mob, generate_mineshaft_mob


@check_all
def explore():
    clear()

    # Список опций для исследования
    options = [
        inquirer.List(
            "choice",
            message="Куда пойдём?",
            choices=[
                ("Назад", "0"),
                ("Лес", "1"),
                ("Шахта", "2"),
                ("Колодец", "3"),
                ("Озеро", "4"),
            ],
        ),
    ]

    try:
        answers = inquirer.prompt(options, theme=theme)
        choice = answers["choice"]  # pyright: ignore
    except TypeError:
        save_game()
        exit()

    if choice == "0":
        from .profile import profile

        profile()
    elif choice == "1":
        forest()
    elif choice == "2":
        mineshaft()
    elif choice == "3":
        well()
    elif choice == "4":
        lake()


def generate_random_loot(loot_table: dict, multiplier=1.0):
    global items, player
    num_items_to_get = random.randint(
        1, len(loot_table)
    )  # Генерируем случайное количество предметов
    items_to_get = random.sample(list(loot_table.keys()), num_items_to_get)

    for item in items_to_get:
        quantity_range = loot_table[item]
        quantity = int(
            random.uniform(quantity_range[0], quantity_range[1]) * multiplier
        )
        if quantity > 0:
            items[item]["Количество"] += quantity
            alert(f"+ {quantity} {item}", "success", enter=False)
    alert("", enter=True)


@check_all
def forest():
    global items, player
    clear()

    # Генерируем случайное число от 0 до 1
    encounter_chance = random.random()

    if encounter_chance <= 0.2:
        # Моб встретился!
        mob = generate_forest_mob()
        print(f"Вы встретили моба: {mob.name}")
        print(f"Здоровье моба: {mob.health}")
        print(f"Урон моба: {mob.damage}")

        mob.mob()
        clear()

    player["Опыт"] += random.uniform(0.1, 5.0)

    if items["Топор"]["Количество"] == 0:
        player["Усталость"] += random.randint(5, 15)
        player["Голод"] += random.randint(5, 10)
        player["Жажда"] += random.randint(10, 15)

        loot_table = {
            "Монеты": (1, 3),
            "Дерево": (1, 5),
            "Вода": (1, 5),
            "Яблоко": (1, 2),
            "Листья": (1, 2),
        }

        generate_random_loot(loot_table, multiplier=1.2)
        save_game()

    elif items["Топор"]["Количество"] > 0:
        player["Усталость"] += random.randint(5, 15)
        player["Голод"] += random.randint(5, 10)
        player["Жажда"] += random.randint(5, 15)
        items["Топор"]["Прочность"] -= random.randint(5, 10)

        loot_table = {
            "Монеты": (1, 5),
            "Дерево": (1, 10),
            "Вода": (1, 5),
            "Яблоко": (1, 5),
            "Листья": (1, 5),
        }

        generate_random_loot(loot_table)
        save_game()

    profile()


@check_all
def mineshaft():
    global items, player

    clear()

    if player["Уровень"] >= 2:

        encounter_chance = random.random()

        if encounter_chance <= 0.3:
            mob = generate_mineshaft_mob()
            print(f"Вы встретили моба: {mob.name}")
            print(f"Здоровье моба: {mob.health}")
            print(f"Урон моба: {mob.damage}")

            mob.mob()

        progress_count = random.uniform(2.0, 5.0)
        player["Опыт"] += progress_count

        if items["Кирка"]["Количество"] == 0:
            player["Усталость"] += random.randint(10, 20)
            player["Голод"] += random.randint(10, 15)
            player["Жажда"] += random.randint(10, 15)

            loot_table = {
                "Камень": (1, 5),
                "Монеты": (1, 4),
            }

            generate_random_loot(loot_table, multiplier=1.2)
            save_game()

        elif items["Кирка"]["Количество"] > 0:
            player["Усталость"] += random.randint(10, 20)
            player["Голод"] += random.randint(10, 15)
            player["Жажда"] += random.randint(10, 15)
            items["Кирка"]["Прочность"] -= random.randint(5, 10)

            loot_table = {
                "Монеты": (1, 8),
                "Железо": (1, 5),
                "Уголь": (1, 10),
                "Камень": (1, 3),
                "Золото": (1, 2),
                "Кристалл": (1, 3),
                "Алмаз": (1, 2),
            }

            generate_random_loot(loot_table)
            save_game()

    else:
        alert("Чтобы пойти в шахту, нужен 2 уровень", "error")

    profile()


@check_all
def well():
    global items, player

    clear()

    if player["Уровень"] >= 5 and items["Ведро"]["Количество"] >= 1:
        progress_count = random.uniform(10.0, 15.0)
        player["Опыт"] += progress_count
        items["Ведро"]["Прочность"] -= random.randint(10, 15)
        player["Голод"] += random.randint(10, 20)
        player["Жажда"] += random.randint(10, 20)
        player["Усталость"] += random.randint(5, 15)

        loot_table = {
            "Вода": (1, 15),
        }

        generate_random_loot(loot_table)
        save_game()

    elif player["Уровень"] < 5:
        alert("Чтобы пойти к колодцу, нужен 5 уровень", "error")
    elif items["Ведро"]["Количество"] == 0:
        alert("Чтобы пойти к колодцу, нужно ведро", "error")

    profile()


@check_all
def lake():
    global items, player

    clear()

    if (
        player["Уровень"] >= 10
        and items["Лодка"]["Количество"] >= 1
        and items["Удочка"]["Количество"] >= 1
    ):
        progress_count = random.uniform(10.0, 20.0)
        player["Опыт"] += progress_count
        items["Лодка"]["Прочность"] -= 5
        items["Удочка"]["Прочность"] -= 10
        player["Голод"] += random.randint(10, 20)
        player["Жажда"] += random.randint(10, 20)
        player["Усталость"] += random.randint(5, 15)

        loot_table = {
            "Рыба": (1, 15),
        }

        generate_random_loot(loot_table)
        save_game()

    elif player["Уровень"] < 10:
        alert("Чтобы пойти в озеро, нужен 10 уровень", "error")
    elif items["Лодка"]["Количество"] == 0:
        alert("Чтобы пойти в озеро, нужна лодка", "error")
    elif items["Удочка"]["Количество"] == 0:
        alert("Чтобы пойти в озеро, нужна удочка", "error")

    profile()
