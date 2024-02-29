from core import Const, Item, ItemRarity, CraftDict


items = Const(
    [
        Item(
            name="монета",
            rarity=ItemRarity.COMMON,
            desc="Монеты используются как игровая валюта.",
        ),
        Item(
            name="дерево",
            price=10,
            rarity=ItemRarity.COMMON,
            desc="Дерево может быть использовано для строительства или изготовления предметов.",
        ),
        Item(
            name="вода",
            price=10,
            rarity=ItemRarity.COMMON,
            desc="Вода необходима для выживания персонажа.",
        ),
        Item(
            name="железо",
            price=15,
            rarity=ItemRarity.COMMON,
            desc="Железо может быть использовано для ковки оружия и брони.",
        ),
        Item(
            name="уголь",
            price=15,
            rarity=ItemRarity.COMMON,
            desc="Уголь используется в печах и кузницах.",
        ),
        Item(
            name="лутбокс",
            price=100,
            rarity=ItemRarity.UNCOMMON,
            desc="Лутбоксы содержат разнообразные сокровища.",
        ),
        Item(
            name="рыба",
            price=30,
            rarity=ItemRarity.COMMON,
            desc="Рыбу можно приготовить и съесть для восстановления здоровья.",
        ),
        Item(
            name="чблоко",
            price=10,
            rarity=ItemRarity.COMMON,
            desc="Яблоко можно съесть для восстановления здоровья.",
        ),
        Item(
            name="камень",
            price=12,
            rarity=ItemRarity.COMMON,
            desc="Камень можно использовать для строительства и изготовления инструментов.",
        ),
        Item(
            name="золото",
            price=42,
            rarity=ItemRarity.UNCOMMON,
            desc="Золото используется для изготовления драгоценных украшений и предметов.",
        ),
        Item(
            name="кристалл",
            price=67,
            rarity=ItemRarity.RARE,
            desc="Кристаллы обладают магической энергией и могут использоваться для создания заклинаний.",
        ),
        Item(
            name="кожа",
            price=17,
            rarity=ItemRarity.COMMON,
            desc="Кожу можно использовать для создания брони и предметов одежды.",
        ),
        Item(
            name="алмаз",
            price=71,
            rarity=ItemRarity.EPIC,
            desc="Алмазы являются одними из самых ценных драгоценных камней.",
        ),
        Item(
            name="череп",
            price=40,
            rarity=ItemRarity.COMMON,
            desc="Черепы могут использоваться в ритуалах и алхимии.",
        ),
        Item(
            name="кость",
            price=30,
            rarity=ItemRarity.COMMON,
            desc="Кости могут использоваться для создания инструментов и украшений.",
        ),
        Item(
            name="нить",
            price=20,
            rarity=ItemRarity.COMMON,
            desc="Нить может использоваться для шитья и создания одежды.",
        ),
        Item(
            name="листья",
            price=4,
            rarity=ItemRarity.COMMON,
            desc="Листья можно использовать для создания зелий и алхимических смесей.",
        ),
        Item(
            name="топор",
            price=15,
            rarity=ItemRarity.UNCOMMON,
            craft=[
                CraftDict(name="Дерево", quantity=5),
                CraftDict(name="Железо", quantity=3),
            ],
            desc="Топор может быть использован для рубки деревьев и сражений.",
        ),
        Item(
            name="кирка",
            price=15,
            rarity=ItemRarity.UNCOMMON,
            craft=[
                CraftDict(name="Железо", quantity=5),
                CraftDict(name="Дерево", quantity=3),
            ],
            desc="Кирка может быть использована для добычи ресурсов и сражений.",
        ),
        Item(
            name="меч",
            price=25,
            rarity=ItemRarity.UNCOMMON,
            craft=[
                CraftDict(name="Железо", quantity=2),
                CraftDict(name="Дерево", quantity=1),
            ],
            desc="Меч является мощным оружием для сражений.",
        ),
        Item(
            name="ведро",
            price=5,
            rarity=ItemRarity.UNCOMMON,
            craft=[
                CraftDict(name="Железо", quantity=3),
            ],
            desc="Ведро может быть использовано для переноски жидкостей.",
        ),
        Item(
            name="лодка",
            price=50,
            rarity=ItemRarity.UNCOMMON,
            craft=[
                CraftDict(name="Железо", quantity=2),
                CraftDict(name="Дерево", quantity=3),
            ],
            desc="Лодка позволяет перемещаться по воде.",
        ),
        Item(
            name="удочка",
            price=8,
            rarity=ItemRarity.UNCOMMON,
            craft=[
                CraftDict(name="Железо", quantity=5),
                CraftDict(name="Нить", quantity=2),
            ],
            desc="Удочка используется для ловли рыбы.",
        ),
    ]
)
