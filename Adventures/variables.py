import inquirer.themes

version = "2.0.11.1"

health_max = 100
hunger_max = 100
thirst_max = 100
fatigue_max = 100
damage_max = 5
protection_max = 2  # Защита

custom_theme = {
    "Checkbox": {
        "selection_color": "gray46",
        "selection_icon": "❯",
        "selected_icon": "◉",
        "selected_color": "green",
        "unselected_icon": "◯",
    },
    "List": {"selection_color": "gray46", "selection_cursor": "❯"},
}

theme = inquirer.themes.load_theme_from_dict(custom_theme)

player = {
    "Здоровье": 100,
    "Голод": 0,
    "Жажда": 0,
    "Усталость": 0,
    "Уровень": 0,
    "Опыт": 0.0,
}

items = {
    "Монеты": {
        "Количество": 0,
        "Вес": 1,
        "Цена": 1,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Ресурс",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Монеты используются как игровая валюта.",
    },
    "Дерево": {
        "Количество": 0,
        "Вес": 5,
        "Цена": 10,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Ресурс",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Дерево может быть использовано для строительства или изготовления предметов.",
    },
    "Вода": {
        "Количество": 0,
        "Вес": 2,
        "Цена": 10,
        "Прочность": 0,
        "Бонусы": {"Насыщенность водой": 10},
        "Тип предмета": "Ресурс",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Вода необходима для выживания персонажа.",
    },
    "Железо": {
        "Количество": 0,
        "Вес": 3,
        "Цена": 15,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Ресурс",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Железо может быть использовано для ковки оружия и брони.",
    },
    "Уголь": {
        "Количество": 0,
        "Вес": 2,
        "Цена": 15,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Ресурс",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Уголь используется в печах и кузницах.",
    },
    "Лутбокс": {
        "Количество": 0,
        "Вес": 1,
        "Цена": 100,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Специальный",
        "Редкость": "Необычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Лутбоксы содержат разнообразные сокровища.",
    },
    "Рыба": {
        "Количество": 0,
        "Вес": 1,
        "Цена": 30,
        "Прочность": 0,
        "Бонусы": {"Питание": 10},
        "Тип предмета": "Еда",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Рыбу можно приготовить и съесть для восстановления здоровья.",
    },
    "Яблоко": {
        "Количество": 0,
        "Вес": 1,
        "Цена": 10,
        "Прочность": 0,
        "Бонусы": {"Питание": 5},
        "Тип предмета": "Еда",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Яблоко можно съесть для восстановления здоровья.",
    },
    "Камень": {
        "Количество": 0,
        "Вес": 2,
        "Цена": 12,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Ресурс",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Камень можно использовать для строительства и изготовления инструментов.",
    },
    "Золото": {
        "Количество": 0,
        "Вес": 2,
        "Цена": 42,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Ресурс",
        "Редкость": "Необычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Золото используется для изготовления драгоценных украшений и предметов.",
    },
    "Кристалл": {
        "Количество": 0,
        "Вес": 1,
        "Цена": 67,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Ресурс",
        "Редкость": "Редкий",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Кристаллы обладают магической энергией и могут использоваться для создания заклинаний.",
    },
    "Кожа": {
        "Количество": 0,
        "Вес": 2,
        "Цена": 17,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Ресурс",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Кожу можно использовать для создания брони и предметов одежды.",
    },
    "Алмаз": {
        "Количество": 0,
        "Вес": 1,
        "Цена": 71,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Ресурс",
        "Редкость": "Эпический",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Алмазы являются одними из самых ценных драгоценных камней.",
    },
    "Череп": {
        "Количество": 0,
        "Вес": 1,
        "Цена": 40,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Специальный",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Черепы могут использоваться в ритуалах и алхимии.",
    },
    "Кость": {
        "Количество": 0,
        "Вес": 1,
        "Цена": 30,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Специальный",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Кости могут использоваться для создания инструментов и украшений.",
    },
    "Нить": {
        "Количество": 0,
        "Вес": 1,
        "Цена": 20,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Ресурс",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Нить может использоваться для шитья и создания одежды.",
    },
    "Листья": {
        "Количество": 0,
        "Вес": 1,
        "Цена": 4,
        "Прочность": 0,
        "Бонусы": {},
        "Тип предмета": "Ресурс",
        "Редкость": "Обычный",
        "Свойства": {},
        "Изготовление": {},
        "Эффекты": {},
        "Описание": "Листья можно использовать для создания зелий и алхимических смесей.",
    },
    "Топор": {
        "Количество": 0,
        "Вес": 5,
        "Цена": 15,
        "Прочность": 20,
        "Бонусы": {"Урон": 15},
        "Тип предмета": "Оружие",
        "Редкость": "Необычный",
        "Свойства": {"Тип оружия": "Топор"},
        "Изготовление": {"Дерево": 5, "Железо": 3},
        "Эффекты": {},
        "Описание": "Топор может быть использован для рубки деревьев и сражений.",
    },
    "Кирка": {
        "Количество": 0,
        "Вес": 5,
        "Цена": 15,
        "Прочность": 20,
        "Бонусы": {"Урон": 15},
        "Тип предмета": "Оружие",
        "Редкость": "Необычный",
        "Свойства": {"Тип оружия": "Кирка"},
        "Изготовление": {"Железо": 5, "Дерево": 3},
        "Эффекты": {},
        "Описание": "Кирка может быть использована для добычи ресурсов и сражений.",
    },
    "Меч": {
        "Количество": 0,
        "Вес": 7,
        "Цена": 25,
        "Прочность": 30,
        "Бонусы": {"Урон": 25},
        "Тип предмета": "Оружие",
        "Редкость": "Необычный",
        "Свойства": {"Тип оружия": "Меч"},
        "Изготовление": {"Железо": 2, "Дерево": 1},
        "Эффекты": {},
        "Описание": "Меч является мощным оружием для сражений.",
    },
    "Ведро": {
        "Количество": 0,
        "Вес": 3,
        "Цена": 5,
        "Прочность": 10,
        "Бонусы": {},
        "Тип предмета": "Инструмент",
        "Редкость": "Необычный",
        "Свойства": {"Тип инструмента": "Ведро"},
        "Изготовление": {"Железо": 3},
        "Эффекты": {},
        "Описание": "Ведро может быть использовано для переноски жидкостей.",
    },
    "Лодка": {
        "Количество": 0,
        "Вес": 15,
        "Цена": 50,
        "Прочность": 40,
        "Бонусы": {},
        "Тип предмета": "Транспорт",
        "Редкость": "Необычный",
        "Свойства": {"Тип транспорта": "Лодка"},
        "Изготовление": {"Железо": 2, "Дерево": 5},
        "Эффекты": {},
        "Описание": "Лодка позволяет перемещаться по воде.",
    },
    "Удочка": {
        "Количество": 0,
        "Вес": 1,
        "Цена": 8,
        "Прочность": 10,
        "Бонусы": {},
        "Тип предмета": "Инструмент",
        "Редкость": "Необычный",
        "Свойства": {"Тип инструмента": "Удочка"},
        "Изготовление": {"Железо": 5, "Нить": 2},
        "Эффекты": {},
        "Описание": "Удочка используется для ловли рыбы.",
    },
}
