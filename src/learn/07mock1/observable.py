from typing import List
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        pass


class Subject(ABC):
    def __init__(self):
        self.observers: List[Observer] = []

    def register_observer(self, observer) -> None:
        if observer not in self.observers:
            self.observers.append(observer)

    def remove_observer(self, observer) -> None:
        if observer in self.observers:
            self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            try:
                observer.update(*args, **kwargs)
            except Exception as e:
                print(e)
