from rich import print
from rich.panel import Panel
import inquirer
from core import Item
from items import items

from utils import clear, alert, check_all, get_item, prompt

from config import game


class Shop:
    def __init__(self):
        self.items = [item for item in items.value if item.price]

    def buy(self, item_name, quantity):
        if get_item(item_name) in self.items:
            item: Item = self.items[item_name]
            coin = game.player.get_item("монета")
            if item.price * quantity <= coin.quantity:
                # Проверяем, хватает ли денег у игрока
                coin.quantity -= item.price * quantity  # Уменьшаем Монеты игрока
                item.quantity += quantity  # Увеличиваем количество купленных предметов
                alert(f"Вы купили {quantity} {item_name}.", "success")
            else:
                alert("У вас недостаточно монет.", "error")
        else:
            alert("Такого предмета нет в магазине.", "error")

    def sell(self, item_name, quantity):
        if get_item(item_name) in self.items:
            item: Item = self.items[item_name]
            if item.quantity >= quantity:
                # Рассчитываем цену продажи немного ниже цены покупки
                sell_price = item.price * quantity / 2
                coin = game.player.get_item("монета")
                coin.quantity += sell_price
                item.quantity -= quantity
                alert(
                    f"Вы продали {quantity} {item_name} за {sell_price} монет.",
                    "success",
                )
            else:
                alert("У вас недостаточно предметов для продажи.", "error")
        else:
            alert("Такого предмета нет в магазине.", "error")

    def get_available_items(self):
        # Возвращаем список доступных предметов, исключая "Монеты", если они есть в списке
        available_items = [
            f"{item} ({item.quantity} | {item.price}/шт)"
            for item in self.items
            if item != "Монеты"
        ]
        return available_items


@game.on("shop")
@check_all
def shop():
    clear()
    print(
        Panel.fit(
            "0. Назад\n" "1. Купить\n" "2. Продать", title="Добро пожаловать в магазин"
        )
    )

    shop_ = Shop()
    available_items = shop_.get_available_items()

    questions = [
        inquirer.List(
            "choice", message="Выберите опцию:", choices=["Назад", "Купить", "Продать"]
        )
    ]

    choice = prompt(questions)

    if choice == "Назад":
        game.trigger("profile")

    elif choice == "Купить":
        clear()
        item_choice = prompt(
            [
                inquirer.List(
                    "item",
                    message="Выберите предмет для покупки:",
                    choices=available_items,
                )
            ]
        )
        item_name = item_choice["item"].split(" ")[0]  # pyright: ignore
        clear()
        try:
            quantity = int(
                input(
                    f"Введите количество (у вас {game.player.get_item('монета').quantity}): "
                )
            )  # Можно также использовать inquirer для ввода количества
        except ValueError:
            quantity = 1
        shop_.buy(item_name, quantity)

    elif choice == "Продать":
        clear()
        item_choice = prompt(
            [
                inquirer.List(
                    "item",
                    message="Выберите предмет для покупки:",
                    choices=available_items,
                )
            ]
        )
        item_name = item_choice["item"].split(" ")[0]  # pyright: ignore
        clear()
        try:
            quantity = int(
                input(
                    f"Введите количество (у вас {game.player.get_item('монета').quantity}): "
                )
            )  # Можно также использовать inquirer для ввода количества
        except ValueError:
            quantity = 1
        shop_.sell(item_name, quantity)
    game.trigger("profile")
