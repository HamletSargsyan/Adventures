version = "2.0.1"

health_max = 100
hunger_max = 100
thirst_max = 100
fatigue_max = 100
damage_max = 5
protection_max = 0  # Защита

player = {
    "Здоровье": 100,
    "Голод": 0,
    "Жажда": 0,
    "Усталость": 0,
    "Уровень": 0,
    "Опыт": 0
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
        "История": "Монеты используются как игровая валюта."
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
        "История": "Дерево может быть использовано для строительства или изготовления предметов."
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
        "История": "Вода необходима для выживания персонажа."
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
        "История": "Железо может быть использовано для ковки оружия и брони."
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
        "История": "Уголь используется в печах и кузницах."
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
        "История": "Лутбоксы содержат разнообразные сокровища."
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
        "История": "Рыбу можно приготовить и съесть для восстановления здоровья."
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
        "История": "Яблоко можно съесть для восстановления здоровья."
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
        "История": "Камень можно использовать для строительства и изготовления инструментов."
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
        "История": "Золото используется для изготовления драгоценных украшений и предметов."
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
        "История": "Кристаллы обладают магической энергией и могут использоваться для создания заклинаний."
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
        "История": "Кожу можно использовать для создания брони и предметов одежды."
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
        "История": "Алмазы являются одними из самых ценных драгоценных камней."
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
        "История": "Черепы могут использоваться в ритуалах и алхимии."
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
        "История": "Кости могут использоваться для создания инструментов и украшений."
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
        "История": "Нить может использоваться для шитья и создания одежды."
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
        "История": "Листья можно использовать для создания зелий и алхимических смесей."
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
        "Изготовление": {},
        "Эффекты": {},
        "История": "Топор может быть использован для рубки деревьев и сражений."
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
        "Изготовление": {},
        "Эффекты": {},
        "История": "Кирка может быть использована для добычи ресурсов и сражений."
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
        "Изготовление": {},
        "Эффекты": {},
        "История": "Меч является мощным оружием для сражений."
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
        "Изготовление": {},
        "Эффекты": {},
        "История": "Ведро может быть использовано для переноски жидкостей."
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
        "Изготовление": {},
        "Эффекты": {},
        "История": "Лодка позволяет перемещаться по воде."
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
        "Изготовление": {},
        "Эффекты": {},
        "История": "Удочка используется для ловли рыбы."
    }
}