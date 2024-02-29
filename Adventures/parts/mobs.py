import random
import datetime
import inquirer

from utils import clear, alert, prompt
from .checks import check
from config import game


class Mob:
    def __init__(self, name, health, damage, loot=[]):
        self.name = name
        self.health = health
        self.damage = damage
        self.loot = loot

    def mob(self):
        questions = [
            inquirer.List(
                "choice", message="Выбери опцию", choices=["Сражаться", "Уйти"]
            ),
        ]
        choice = prompt(questions)

        if choice == "Сражаться":
            self.attack()
        elif choice == "Уйти":
            self.leave()

    def leave(self):

        damage = (
            random.randint(1, 10) - game.player.protection
            if game.player.protection != 0
            else random.randint(1, 10)
        )
        game.player.health -= damage
        game.save()
        alert(f"{self.name} догнал и ударил\n\n-{damage} здоровья", "error")
        check()
        clear()

    def attack(self):
        while self.health and game.player.health > 0:
            mob_damage = random.randint(1, self.damage - game.player.protection)
            damage = random.randint(1, game.player.damage)

            if game.player.get_or_add_item("меч").quantity > 0:
                damage += 10

            self.health -= damage
            game.player.health -= mob_damage

            clear()
            alert(
                f"Ты нанес удар и нанес {damage} урона\n"
                f"{self.name} наносит удар и наносит {mob_damage} урона",
                "warning",
            )

            if game.player.health <= 0:
                alert(f"{self.name} победил тебя...", "error")
                game.trigger("die")

            if self.health <= 0:
                alert(f"Ты одолел {self.name}!", "success")
                for loot_item in self.loot:
                    quantity = random.randint(1, 5)
                    game.player.get_or_add_item(loot_item).quantity += quantity

                    alert(f"+ {quantity} {loot_item}", "success", enter=False)
                alert("", enter=True)
                game.player.xp += random.randint(10, 15)
                return game.trigger("profile")

            check()
            clear()
            game.save()


class Goblin(Mob):
    def __init__(self):
        loot = ["Монеты", "Вода"]
        super().__init__(
            name="Гоблин",
            health=random.randint(50, 70),
            damage=random.randint(10, 15),
            loot=loot,
        )


class Wolf(Mob):
    def __init__(self):
        loot = ["Монеты", "Кожа"]
        super().__init__(
            name="Волк",
            health=random.randint(30, 40),
            damage=random.randint(5, 8),
            loot=loot,
        )


class Spider(Mob):
    def __init__(self):
        loot = ["Нить"]
        super().__init__(
            name="Паук",
            health=random.randint(40, 55),
            damage=random.randint(7, 12),
            loot=loot,
        )


class Zombie(Mob):
    def __init__(self):
        loot = ["Монеты", "Кожа"]
        super().__init__(
            name="Зомби",
            health=random.randint(70, 90),
            damage=random.randint(8, 12),
            loot=loot,
        )


class Skeleton(Mob):
    def __init__(self):
        loot = ["Монеты", str(random.choice(["Череп", "Кость"]))]
        super().__init__(
            name="Скелет",
            health=random.randint(60, 75),
            damage=random.randint(12, 18),
            loot=loot,
        )


def generate_forest_mob():
    mob_types = []

    now = datetime.datetime.now()
    current_hour = now.hour

    if 21 <= current_hour or current_hour <= 6:  # Ночь (с 21:00 до 6:00)
        mob_types = [Wolf, Goblin, Spider, Zombie]
    else:  # День (с 6:00 до 21:59)
        mob_types = [Spider, Zombie]

    random_mob_type = random.choice(mob_types)
    new_mob = random_mob_type()
    return new_mob


def generate_mineshaft_mob():
    mob_types = []

    now = datetime.datetime.now()
    current_hour = now.hour

    if 21 <= current_hour or current_hour <= 6:  # Ночь (с 21:00 до 6:00)
        mob_types = [Goblin, Skeleton, Spider]
    else:  # День (с 6:00 до 21:59)
        mob_types = [Spider, Zombie, Skeleton]

    random_mob_type = random.choice(mob_types)
    new_mob = random_mob_type()
    return new_mob
