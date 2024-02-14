from typing import Dict, List, Callable

__all__ = ["Game"]


class Game:
    def __init__(self):
        self.events: Dict[str, List[Callable]] = {}

    def trigger(self, event_name: str):
        if event_name in self.events:
            for event_func in self.events[event_name]:
                event_func()

    def on(self, event_name: str):
        def decorator(func: Callable):
            if event_name not in self.events:
                self.events[event_name] = []
            self.events[event_name].append(func)

        return decorator
