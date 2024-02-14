import os
from typing import Dict, List, Callable, Type, Any
import importlib.util

from rich.console import Console

class Game:
    def __init__(self) -> None:
        self.events: Dict[str, List[Callable[[], None]]] = {}
        self.modules: List[Type[Any]] = []
        self.console = Console()
    

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
        self.trigger("start")

    def register_trigger(self, event_name: str, func: Callable[[], None]) -> None:
        if event_name not in self.events:
            self.events[event_name] = []
        self.events[event_name].append(func)
    
