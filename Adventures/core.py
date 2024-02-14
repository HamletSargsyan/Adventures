import os
from typing import Dict, List, Callable, Type, Any
import importlib.util

class Game:
    def __init__(self) -> None:
        self.events: Dict[str, List[Callable[[], None]]] = {}
        self.modules: List[Type["Any"]] = []

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
        self.import_modules("modules")
        print("Импортированные модули:")
        for mod in self.modules:
            m = mod()
            print(m.name, m.version)
        self.trigger("start")

    def register_trigger(self, event_name: str, func: Callable[[], None]) -> None:
        if event_name not in self.events:
            self.events[event_name] = []
        self.events[event_name].append(func)
    
    def import_modules(self, folder_path: str):
        self.modules = []
        for filename in os.listdir(folder_path):
            if filename.endswith(".py"):
                module_name = filename[:-3]
                module = importlib.import_module(f"{folder_path}.{module_name}")
                for name in dir(module):
                    obj = getattr(module, name)
                    if isinstance(obj, type) and issubclass(obj, Module) and name.endswith("Mod"):
                        self.modules.append(obj)

class Module:
    def __init__(self, name: str, version: str) -> None:
        self.name = name
        self.version = version