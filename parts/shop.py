from rich import print
from rich.panel import Panel
import inquirer

from utils import clear, alert, save_game, check_all
from variables import items

class Shop:
    def __init__(self):
        self.items = items

    def buy(self, item_name, quantity):
        if item_name in self.items:
            item = self.items[item_name]
            if item["Цена"] * quantity <= items["Монеты"]["Количество"]:
                # Проверяем, хватает ли денег у игрока
                items["Монеты"]["Количество"] -= item["Цена"] * quantity  # Уменьшаем Монеты игрока
                item["Количество"] += quantity  # Увеличиваем количество купленных предметов
                alert(f"Вы купили {quantity} {item_name}.", 'success')
            else:
                alert("У вас недостаточно монет.", 'error')
        else:
            alert("Такого предмета нет в магазине.", 'error')

    def sell(self, item_name, quantity):
        if item_name in self.items:
            item = self.items[item_name]
            if item["Количество"] >= quantity:
                # Рассчитываем цену продажи немного ниже цены покупки
                sell_price = item["Цена"] * quantity * 0.9  # Продаем по 90% от цены покупки
                items["Монеты"]["Количество"] += sell_price  # Увеличиваем Монеты игрока
                item["Количество"] -= quantity  # Уменьшаем количество проданных предметов
                alert(f"Вы продали {quantity} {item_name} за {sell_price} монет.", 'success')
            else:
                alert("У вас недостаточно предметов для продажи.", 'error')
        else:
            alert("Такого предмета нет в магазине.", 'error')

    def get_available_items(self):
        # Возвращаем список доступных предметов, исключая "Монеты", если они есть в списке
        available_items = list(self.items.keys())
        available_items.remove("Монеты")
        return available_items

@check_all
def shop():
    clear()
    print(Panel.fit("0. Назад\n"
                    "1. Купить\n"
                    "2. Продать", title="Добро пожаловать в магазин"))

    _shop = Shop()
    available_items = _shop.get_available_items()

    options = [
        inquirer.List('choice',
                      message="Выберите опцию:",
                      choices=[
                          'Назад',
                          'Купить',
                          'Продать'
                      ])
    ]

    try:
        answers = inquirer.prompt(options)
        choice = answers['choice']
    except TypeError:
        save_game()
        exit()

    if choice == 'Назад':
        from .profile import profile
        profile()

    elif choice == 'Купить':
        clear()
        item_choice = inquirer.prompt([
            inquirer.List('item',
                          message="Выберите предмет для покупки:",
                          choices=available_items)
        ])
        item_name = item_choice['item']
        clear()
        quantity = int(input("Введите количество: "))  # Можно также использовать inquirer для ввода количества
        _shop.buy(item_name, quantity)

    elif choice == 'Продать':
        clear()
        item_choice = inquirer.prompt([
            inquirer.List('item',
                          message="Выберите предмет для продажи:",
                          choices=available_items)
        ])
        item_name = item_choice['item']
        clear()
        quantity = int(input("Введите количество: "))  # Можно также использовать inquirer для ввода количества
        _shop.sell(item_name, quantity)
    shop()
