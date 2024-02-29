import random
import inquirer
from utils import clear, alert, check_all, prompt


from config import game


@game.on("recovery")
@check_all
def recovery():
    clear()

    health_gain = random.randint(5, 10)
    fatigue_reduction = random.randint(5, 15)
    game.player.health += health_gain
    game.player.fatigue -= fatigue_reduction

    alert(
        f"Вы отдыхаете и восстанавливаете {health_gain} здоровья и уменьшаете усталость на {fatigue_reduction}",
        "success",
    )

    if game.player.fatigue < 0:
        game.player.fatigue = 0
    if game.player.health > game.player.health_max:
        game.player.health = game.player.health_max

    game.save()

    game.trigger("profile")


@game.on("food")
@check_all
def food():
    global player

    clear()

    questions = [
        inquirer.List(
            "choice",
            message="Выберите опцию:",
            choices=[
                ("Назад", "0"),
                ("Яблоко", "1"),
                ("Рыба", "2"),
                ("Вода", "3"),
            ],
        ),
    ]

    choice = prompt(questions)

    if choice == "0":
        game.trigger("profile")
    elif choice == "1":
        if game.player.hunger >= 1:
            apple = game.player.get_or_add_item("яблоко")
            if apple.quantity >= 1:
                game.player.hunger -= int(apple.effects[0].value)  # TODO edit
                alert(f"-{int(apple.effects[0].value)} голода", "success")
            else:
                alert("Недостаточно", "error")
        else:
            alert("Ты не голоден", "warning")
    elif choice == "2":
        if game.player.hunger >= 1:
            fish = game.player.get_or_add_item("рыба")
            if fish.quantity >= 1:
                game.player.hunger -= int(fish.effects[0].value)  # TODO edit
                alert(f"-{int(fish.effects[0].value)} голода", "success")
            else:
                alert("Недостаточно", "error")
        else:
            alert("Ты не голоден", "warning")
    elif choice == "3":
        if game.player.thirst >= 1:
            wather = game.player.get_or_add_item("вода")
            if wather.quantity >= 1:
                game.player.thirst -= int(wather.effects[0].value)  # TODO edit
                alert(f"-{int(wather.effects[0].value)} жажды", "success")
            else:
                alert("Недостаточно", "error")
        else:
            alert("Тебе не нужно пить", "warning")
    game.trigger("food")
