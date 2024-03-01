import random
from typing import TYPE_CHECKING
from rich import print
import inquirer
from utils import clear, alert, check_all, get_item, prompt

from .mobs import generate_forest_mob, generate_mineshaft_mob
from config import game

if TYPE_CHECKING:
    from core import Item


@game.on("explore")
@check_all
def explore():
    clear()

    # Список опций для исследования
    questions = [
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

    choice = prompt(questions)

    if choice == "0":
        game.trigger("profile")
    elif choice == "1":
        game.trigger("forest")
    elif choice == "2":
        game.trigger("mineshaft")
    elif choice == "3":
        game.trigger("well")
    elif choice == "4":
        game.trigger("lake")


def generate_random_loot(loot_table: dict, multiplier=1.0):
    num_items_to_get = random.randint(1, len(loot_table))
    items_to_get = random.sample(list(loot_table.keys()), num_items_to_get)

    for item_name in items_to_get:
        quantity_range = loot_table[item_name]
        quantity = int(
            random.uniform(quantity_range[0], quantity_range[1]) * multiplier
        )
        if quantity > 0:
            item = game.player.get_item(item_name)
            item.quantity += quantity
            alert(f"+ {quantity} {item_name}", "success", enter=False)
    alert("", enter=True)


@game.on("chest")
@check_all
def chest():
    alert("Ты нашел сундук", level="success", enter=False)
    questions = [
        inquirer.List(
            "choice",
            message="Открыть?",
            choices=[("Открыть", "1"), ("Не открыть", "2")],
        )
    ]

    choice = prompt(questions)

    if choice == "1":
        loot_table = {
            "Монеты": (5, 15),
            "Дерево": (1, 6),
            "Вода": (3, 6),
            "Железо": (5, 10),
            "Рыба": (5, 10),
        }

        alert("Открыл сундук и получил:", level="success", enter=False)
        generate_random_loot(loot_table)  # TODO
    elif choice == "2":
        alert("Как хочешь")


@game.on("forest")
@check_all
def forest():
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

    chest_chance = random.random()
    if chest_chance <= 0.1:
        game.trigger("chest")
        clear()

    game.player.xp += random.uniform(0.1, 5.0)

    player_item = game.player.get_item("топор")

    if player_item.quantity <= 0:
        game.player.fatigue += random.randint(5, 15)
        game.player.hunger += random.randint(5, 10)
        game.player.thirst += random.randint(10, 15)

        loot_table = {
            "Монеты": (1, 3),
            "Дерево": (1, 5),
            "Вода": (1, 5),
            "Яблоко": (1, 2),
            "Листья": (1, 2),
        }

        generate_random_loot(loot_table, multiplier=1.2)

    else:
        game.player.fatigue += random.randint(5, 15)
        game.player.hunger += random.randint(5, 10)
        game.player.thirst += random.randint(5, 15)
        player_item.strength -= random.uniform(5, 10)  # pyright: ignore

        loot_table = {
            "Монеты": (1, 5),
            "Дерево": (1, 10),
            "Вода": (1, 5),
            "Яблоко": (1, 5),
            "Листья": (1, 5),
        }

        generate_random_loot(loot_table)

    game.save()
    game.trigger("profile")


@game.on("mineshaft")
@check_all
def mineshaft():
    clear()

    if game.player.level >= 2:
        encounter_chance = random.random()

        if encounter_chance <= 0.3:
            mob = generate_mineshaft_mob()
            print(f"Вы встретили моба: {mob.name}")
            print(f"Здоровье моба: {mob.health}")
            print(f"Урон моба: {mob.damage}")

            mob.mob()

        chest_chance = random.random()
        if chest_chance <= 0.1:
            game.on("chest")
            clear()

        progress_count = random.uniform(2.0, 5.0)
        game.player.xp += progress_count

        player_item = game.player.get_item("кирка")

        if player_item.quantity <= 0:
            game.player.fatigue += random.randint(10, 20)
            game.player.hunger += random.randint(10, 15)
            game.player.thirst += random.randint(10, 15)

            loot_table = {
                "Камень": (1, 5),
                "Монеты": (1, 4),
            }

            generate_random_loot(loot_table, multiplier=1.2)
        else:
            game.player.fatigue += random.randint(10, 20)
            game.player.hunger += random.randint(10, 15)
            game.player.thirst += random.randint(10, 15)
            player_item.strength -= random.randint(5, 10)  # pyright: ignore

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
    else:
        alert("Чтобы пойти в шахту, нужен 2 уровень", "error")
    game.save()
    game.trigger("profile")


@game.on("well")
@check_all
def well():
    clear()

    player_item = game.player.get_item("ведро")

    if game.player.level >= 5 and player_item.quantity >= 1:
        progress_count = random.uniform(10.0, 15.0)
        game.player.xp += progress_count
        player_item.strength -= random.randint(10, 15)  # pyright: ignore
        game.player.hunger += random.randint(10, 20)
        game.player.thirst += random.randint(10, 20)
        game.player.fatigue += random.randint(5, 15)

        loot_table = {
            "Вода": (1, 15),
        }
        generate_random_loot(loot_table)
    elif game.player.level < 5:
        alert("Чтобы пойти к колодцу, нужен 5 уровень", "error")
    else:
        alert("Чтобы пойти к колодцу, нужно ведро", "error")
    game.save()
    game.trigger("well")


@game.on("lake")
@check_all
def lake():
    clear()

    boat = game.player.get_item("лодка")
    fishing_rod = game.player.get_item("удочка")
    if game.player.level >= 10 and boat.quantity >= 1 and fishing_rod.quantity >= 1:
        progress_count = random.uniform(10.0, 20.0)
        game.player.xp += progress_count
        boat.strength -= 5  # pyright: ignore
        fishing_rod.strength -= 10  # pyright: ignore
        game.player.hunger += random.randint(10, 20)
        game.player.thirst += random.randint(10, 20)
        game.player.fatigue += random.randint(5, 15)

        loot_table = {
            "Рыба": (1, 15),
        }

        generate_random_loot(loot_table)

    elif game.player.level < 10:
        alert("Чтобы пойти в озеро, нужен 10 уровень", "error")
    elif boat.quantity == 0:
        alert("Чтобы пойти в озеро, нужна лодка", "error")
    elif fishing_rod.quantity == 0:
        alert("Чтобы пойти в озеро, нужна удочка", "error")

    game.trigger("profile")
