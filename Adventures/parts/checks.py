import random

from items import items
from utils import clear, alert
from config import game


def check():
    if game.player.health >= game.player.health_max:
        game.player.health = game.player.health_max
    if game.player.hunger >= game.player.hunger_max:
        game.player.hunger = game.player.hunger_max
    if game.player.thirst >= game.player.thirst_max:
        game.player.thirst = game.player.thirst_max
    if game.player.fatigue >= game.player.fatigue_max:
        game.player.fatigue = game.player.fatigue_max
    if game.player.level < 0:
        game.player.level = 0

    if game.player.health < 0:
        game.player.health = 0
    if game.player.hunger < 0:
        game.player.hunger = 0
    if game.player.thirst < 0:
        game.player.thirst = 0
    if game.player.fatigue < 0:
        game.player.fatigue = 0
    if game.player.level < 0:
        game.player.level = 0

    if game.player.fatigue >= game.player.fatigue_max:
        game.player.health -= random.randint(1, 5)
    if game.player.hunger >= game.player.hunger_max:
        game.player.health -= random.randint(1, 5)
    if game.player.thirst >= game.player.thirst_max:
        game.player.health -= random.randint(1, 5)
    if game.player.health <= 0:
        game.trigger("die")

    if game.player.xp >= 100:
        game.player.level += 1
        game.player.xp = 0.0
        lootbox_quantity = random.randint(1, 3)
        game.player.get_or_add_item("лутбокс").quantity += lootbox_quantity
        clear()
        alert(
            f"[bright_green]Поздравляем! Ваш уровень повышен до {game.player.health}[/bright_green]",
            "success",
        )
        alert(f"Вы получили {lootbox_quantity} лутбокс", "success")

        # https://github.com/HamletSargsyan/Adventures/issues/9
        # level_up()
        # game.trigger("level_up")

    for item in items.value:
        if item.strength and item.strength <= 0:
            item.strength = 0
            item.quantity -= 1
        if item.quantity < 0:
            item.quantity = 0

    game.save()
