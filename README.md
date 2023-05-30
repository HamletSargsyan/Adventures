# Об игре

**Adventurs** - Это текстовая игра, написанная на языке Python. Игра позволяет игроку исследовать окружающий мир, сражаться с противниками и и т.п.

**Версия**: 1.0.0-BETA

## Возможности

- [Профиль игрока](#profile)
- [Исследование](#explore)
- [Сражение с монстром](#fight)
- [Крафтинг](#craft)
- [Магазин](#shop)
- [Лутбокс](#lootbox)
- [Отдых и питание](#rest_and_food)

<a id="profile"></a>

## Профиль игрока

В профиле вы можете видеть ваше `состояние` (здоровые, усталость, голод и жажда), `ресурсы` и `инструменты`.

**Список инструментов и для чего они нужны:**

| Название | Что делает                                |
|:-------: |:-----------------------------------------:|
| Топор    | Приносит больше дерева из леса            |
| Кирка    | Приносит больше лута из шахты             |
| Меч      | Наносит больше урона монстру              |
| Ведро    | Нужен чтобы пойти в колодец и забрать воду|
| Лодка    | Нужен чтобы пойти в озеро                 |
| Удочка   | С ее помощью надо ловить рыбу             |

<a id="explore"></a>

## Исследование

- [Лес](#forest)
- [Шахта](#mineshaft)
- [Колодец](#well)
- [Озеро](#lake)
<a id="forest"></a>

### Лес

В лесу вы в рандомном количестве получайте `опыт`, `предметы` (дерево, вода и яблоко) и `монеты`.

**Лут без топора**

| Название | Рандомное количество |
|:-------: |:--------------------:|
| Опыт     | 0.1 - 5.0            |
| Монеты   | 1 - 3                |
| Дерево   | 1 - 15               |
| Вода     | 1 - 10               |
| Яблоко   | 1 - 10               |
| Усталость| 5 - 15               |
| Голод    | 5 - 10               |
| Жажда    | 10 - 15              |

**Лут с топором**

> Прочность топора уменьшается в рандомном количестве, от 5 до 10.


| Название | Рандомное количество |
|:-------: |:--------------------:|
| Опыт     | 0.1 - 5.0            |
| Монеты   | 1 - 3                |
| Дерево   | 20 - 30              |
| Вода     | 1 - 10               |
| Яблоко   | 1 - 10               |
| Усталость| 5 - 15               |
| Голод    | 5 - 10               |
| Жажда    | 5 - 15               |

<a id="mineshaft"></a>

### Шахта

В шахте вы в рандомном количестве получайте `опыт`, `предметы` (железо и уголь) и `монеты`.

> Шахта доступна с 2 уровня

**Лут без кирки**

| Название | Рандомное количество |
|:--------:|:--------------------:|
| Опыт     | 2.0 - 5.0            |
| Монеты   | 5 - 10               |
| Железо   | 1 - 5                |
| Уголь    | 1 - 5                |
| Усталость| 10 - 20              |
| Голод    | 10 - 15              |
| Жажда    | 10 - 15              |

**Лут с киркой**

> Прочность кирки уменьшается в рандомном количестве, от 5 до 15.

| Название | Рандомное количество |
|:--------:|:--------------------:|
| Опыт     | 2.0 - 5.0            |
| Монеты   | 5 - 15               |
| Железо   | 20 - 30              |
| Уголь    | 20 - 30              |
| Усталость| 10 - 20              |
| Голод    | 10 - 15              |
| Жажда    | 10 - 15              |

<a id="well"></a>

### Колодец

В шахте вы в рандомном количестве получайте `опыт`, `воду` и `монеты`.

> Колодец доступен с 5 уровня
> Чтобы пойти к колодцу обязательно надо иметь ведро

> Прочность ведра уменьшается в рандомном количестве, от 10 до 15.

| Название | Рандомное количество |
|:--------:|:--------------------:|
| Опыт     | 10.0 - 15.0          |
| Вода     | 10 - 30              |
| Усталость| 10 - 20              |
| Голод    | 10 - 15              |
| Жажда    | 10 - 15              |

<a id="lake"></a>

### Озеро

В шахте вы в рандомном количестве получайте `опыт`, `рыбу` и `монеты`.

> Колодец доступен с 10 уровня
> Чтобы пойти к колодцу обязательно надо иметь удочку и лодку

> Прочночть удочки уменшаеться в рандомном количестве, от 10 до 15.

| Название | Рандомное количество |
|:--------:|:--------------------:|
| Опыт     | 10.0 - 20.0          |
| Рыба     | 10 - 30              |
| Усталость| 5 - 15               |
| Голод    | 10 - 20              |
| Жажда    | 10 - 20              |

<a id="fight"></a>

## Сражение с монстром

После сражение с монстром вы в рандомном количестве получайте `опыт`, `яблоко` и `монеты`.

> Будьте внимательным, так как вы получаете урон и это может привести к смерти игрока.

**Лут без меча**

| Название | Рандомное количество |
|:--------:|:--------------------:|
| Опыт     | 5.0 - 7.0            |
| Монеты   | 10 - 20              |
| Яблоко   | 10 - 20              |
| Урон     | 10 - 15              |

**Лут с мечом**

> Прочность меча уменьшается в рандомном количестве, от 10 до 25.

| Название | Рандомное количество |
|:--------:|:--------------------:|
| Опыт     | 5.0 - 7.0            |
| Монеты   | 10 - 20              |
| Яблоко   | 10 - 20              |
| Урон     | 10 - 15              |

<a id="craft"></a>

## Крафтинг

Вы можете крафтить предметы, используя доступные ресурсы. Крафтинг позволяет создавать новые инструменты или улучшать существующие.

**Рецепты крафтов**

| Название | Рецепт               | Опыт      |
|:--------:|:--------------------:|:---------:|
| Топор    | 5 Дерево и 3 Железо  | 3.0 - 5.0 |
| Кирка    | 3 Дерево и 5 Железо  | 5.0 - 8.0 |
| Меч      | 1 Дерево и 2 Железо  | 5.0 - 9.0 |
| Ведро    | 3 Железо             | 5.0 - 9.0 |
| Лодка    | 5 Дерево и 2 Железо  | 5.0 - 9.0 |
| Удочка   | 5 Железо             | 5.0 - 9.0 |

<a id="shop"></a>

## Магазин

В игре есть магазин, где игрок может покупать различные предметы, включая инструменты, ресурсы и лутбоксы.

- [Покупка](#buy)
- [Продажа](#sell)

<a id="buy"></a>

### Покупка

| Название | Цена           |
|:--------:|:--------------:|
| яблоко   | 10             |
| вода     | 10             |
| уголь    | 15             |
| дерево   | 15             |
| железо   | 25             |
| топор    | 50             |
| кирка    | 50             |
| меч      | 50             |
| лутбокс  | 300            |

<a id="sell"></a>

### Продажа

| Название | Цена           |
|:--------:|:--------------:|
| яблоко   | 5              |
| вода     | 5              |
| уголь    | 10             |
| дерево   | 10             |
| железо   | 15             |
| топор    | 20             |
| кирка    | 20             |
| меч      | 20             |

<a id="lootbox"></a>

## Лутбокс

В игре присутствуют лутбоксы, которые игрок может получить после достижения определенного уровня или купить в магазине. Лутбоксы содержат случайные предметы или ресурсы, которые могут помочь игроку в его приключении.

> В лутбоксах попадаються придметы рандомом от 1 до 10

**Таблица лута**

| Название | Рандомное количество |
|:--------:|:--------------------:|
| Монеты   | 1 - 10               |
| Дерево   | 1 - 10               |
| Вода     | 1 - 10               |
| Яблоко   | 1 - 10               |
| Железо   | 1 - 10               |
| Уголь    | 1 - 10               |
| Топор    | 1                    |
| Кирка    | 1                    |
| Меч      | 1                    |

<a id="rest_and_food"></a>

## Отдых и питание

Игрок должен следить за состоянием своего персонажа, включая усталость, голод и жажду. Он может `отдыхать`, `есть` и `пить`, чтобы поддерживать свое здоровье и выживаемость.