# Журнал изменений

## Версия 2.0.0

### Добавлено
- Мобы в лесу и шахте: `Гоблин`, `Волк`, `Паук`, `Зомби`, `Скелет`
- Новые предметы: `Камень`, `Золото`, `Кристалл`, `Кожа`, `Алмаз`, `Череп`, `Кость`, `Нить`, `Листья`, они на данный момент бесполезные
- В главном меню при выборе `Обновления` будет показываться установлена актуальная версия или старая, если версия старая, то будет ссылка на скачивание новой версии
- Красивое оформление с помощью модуля [Rich](https://github.com/Textualize/rich)

### Изменено
- Вместо ввода цифр для выполнения операций нужно использовать <kbd>↑</kbd> (стрелка вверх) и <kbd>↓</kbd> (стрелка вниз) с помощью модуля [Inquirer](https://github.com/magmax/python-inquirer)
- Данные сохраняются в формате `pickle` вместо `json`
- Маленькие изменения в логике игры
- Оптимизация кода

### Удалено
- Удален пункт `Помощь` из главной страницы (временно)

## Версия 1.0.0

### Добавлено
- Файл guide.md, где написано, где и как можно найти предметы, количество опыта за определенные действия и т.п.
- В стартовом меню теперь есть возможность покинуть игру