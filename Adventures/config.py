import inquirer.themes

from core import Game, DictSerializable, Const

__all__ = ["game", "config"]


default_theme = {
    "Checkbox": {
        "selection_color": "gray46",
        "selection_icon": "❯",
        "selected_icon": "◉",
        "selected_color": "green",
        "unselected_icon": "◯",
    },
    "List": {"selection_color": "gray46", "selection_cursor": "❯"},
}


class Config(DictSerializable):
    def __init__(self) -> None:
        self.version = Const("3.0")
        self.theme = default_theme

    def load_theme(self):
        self.theme = inquirer.themes.load_theme_from_dict(self.theme)
        return self.theme

config = Config()

game = Game(config)

