from enum import Enum
import os
import pickle
from typing import TYPE_CHECKING, Any, Dict, Generic, Iterable, List, Callable, Literal, TypeVar, TypedDict, Union
import inquirer.themes
from rich.console import Console

from utils import get_item

if TYPE_CHECKING:
    from config import Config

class DictSerializable:
    def to_dict(self) -> dict:
        return self.__dict__

    @classmethod
    def from_dict(cls, dict_data: dict):
        instance = cls()
        instance.__dict__.update(dict_data)
        return instance



T = TypeVar('T')

class Const(Generic[T], DictSerializable):
    def __init__(self, value: T):
        self._value = value
        self._index = 0
    
    @property
    def value(self) -> T:
        return self._value
    
    def from_dict(self):
        raise AttributeError("Const object is immutable")
    
    def __str__(self) -> str:
        return str(self._value)

    def __repr__(self) -> str:
        return repr(self._value)
    
    def __iter__(self):
        self._index = 0
        return self
    
    
    def __next__(self):
        if self._index < len(self.value): #pyright: ignore
            value: T = self.value[self._index]
            self._index += 1
            return value
        else:
            # Raise StopIteration to signal the end of iteration
            raise StopIteration


class Game:
    def __init__(self, config) -> None:
        self.events: Dict[str, List[Callable[[], None]]] = {}
        self.console = Console()
        self.player = Player()
        self.save_dir: str = "./saves"

        self.config = config
        self.theme = inquirer.themes.load_theme_from_dict(self.theme)



    def trigger(self, event_name: str) -> None:
        if event_name in self.events:
            for event_func in self.events[event_name]:
                event_func()

    def on(self, event_name: str) -> Callable[[Callable[[], None]], Callable[[], None]]:
        def decorator(func: Callable[[], None]) -> Callable[[], None]:
            if event_name not in self.events:
                self.events[event_name] = []
            self.events[event_name].append(func)
            return func

        return decorator

    def run(self):
        self.config.load_theme()
        self.trigger("start")

    def register_trigger(self, event_name: str, func: Callable[[], None]) -> None:
        if event_name not in self.events:
            self.events[event_name] = []
        self.events[event_name].append(func)
    
    def _create_save_dir(self):
        if os.path.exists(self.save_dir):
            return
        os.mkdir(self.save_dir)

    def save(self):
        self._create_save_dir()
        
        game_data = {
            "player": self.player.to_dict(),
        }

        with open(self.save_dir, "wb") as f:
            pickle.dump(game_data, f)
    
    def load(self):
        self._create_save_dir()

        if os.path.exists(self.save_dir):
            from utils import alert
            alert("Файл сохранения не найден.", "error")
            return

        with open(self.save_dir, "rb") as f:
            game_data = pickle.load(f)
            self.player.from_dict(game_data["player"])
            

class Effect(DictSerializable):
    def __init__(
            self,
            type: Union[Literal["buff"], Literal["debuff"]],
            value: Union[int, float]
            ) -> None:
        self.type = type
        self.value = value


class ItemRarity(Enum):
    COMMON = "обычный"
    UNCOMMON = "необычный"
    RARE = "редкий"
    EPIC = "эпический"
    LEGENDARY = "легендарный"


class CraftDict(TypedDict):
    name: str
    quantity: int


class Item(DictSerializable):
    def __init__(
            self,
            name: str,
            strength: float,
            rarity: ItemRarity,
            desc: str,
            can_equip: bool = False,
            price: Union[int, None] = None,
            effects: Union[List[Effect], None] = None,
            craft: Union[List[CraftDict], None] = None,
            quantity: int = 0
            ) -> None:
        self.name = name
        self.strength = strength
        self.rarity = rarity
        self.desc = desc
        self.can_equip = can_equip
        self.price = price
        self.effects = effects
        self.craft = craft
        self.quantity = quantity

    def __repr__(self) -> str:
        return f"<Item {self.name}>"
    
    def __str__(self) -> str:
        return self.__repr__()
    
   

class Player(DictSerializable):
    def __init__(
            self,
            name: str = "игрок"
            ) -> None:
        self.name = name
        self.health = 100
        self.hunger = 0
        self.thirst = 0
        self.fatigue = 0
        self.level = 1
        self.xp = 0.0
        self.damage = 5
        self.protection = 1

        self.health_max = 100
        self.hunger_max = 100
        self.thirst_max = 100
        self.fatigue_max = 100

        self.inventory: List[Item] = []
        self.equiped_items: List[Item] = []

    def _get_item(self, name: str, where: Union[Literal["inventory"], Literal["equiped_items"]]):
        _items = self.inventory if where == "inventory" else self.equiped_items
        
        for item in _items:
            if item.name == name:
                return item

    def get_or_add_item(self, name: str):
        if not get_item(name):
            raise
        if not self._get_item(name, "inventory"):
            self.inventory.append(get_item(name)) # pyright: ignore
        return self._get_item(name, "inventory")
