from core import Module
from utils import alert
from config import game

class TestMod(Module):
    def __init__(self) -> None:
        super().__init__("events", "1")
        game.register_trigger("start", self.start)

    def start(self):
        alert("start")