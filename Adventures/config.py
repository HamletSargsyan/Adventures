import inquirer.themes
from icecream import ic

from core import Game, DictSerializable, Const

__all__ = ["game", "config"]


default_theme = {
    "List": {"selection_color": "gray46", "selection_cursor": "❯"},
}


class Config(DictSerializable):
    def __init__(self) -> None:
        self.version = Const("3.0")
        self.theme = default_theme

    def load_theme(self):
        return inquirer.themes.load_theme_from_dict(self.theme)


config = Config()

game = Game(config)


