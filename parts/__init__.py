# Этот код будет выполнен при импорте пакета
# print("Пакет package был импортирован.")

# Перечисляем объекты для экспорта
__all__ = ['_checks', '_craft', '_drink', '_eat', '_explore', '_lootbox', '_monster', '_profile', '_rest', '_shop']

# Импортируем подмодули, чтобы они были доступны из пакета
from . import _craft
from . import _explore
from . import _lootbox
from . import _monster
from . import _rest
from . import _shop
from . import _eat
from . import _drink
from . import _profile