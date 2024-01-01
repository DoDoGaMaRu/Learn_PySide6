import sys
import random
import asyncio
from typing import List

from PySide6 import QtCore, QtWidgets
from abc import ABC, abstractmethod
from threading import Thread


class Observer(ABC):
    @abstractmethod
    def update(self, *args, **kwargs):
        pass


# TODO CommonMeta 관련 찾아보기
class CommonMeta(type(QtWidgets.QWidget), type(Observer)):
    pass


class Subject(ABC):
    observers: List[Observer] = []

    def register_observer(self, observer) -> None:
        self.observers.append(observer)

    def remove_observer(self, observer) -> None:
        self.observers.remove(observer)

    def notify_observers(self, *args, **kwargs):
        for observer in self.observers:
            observer.update(*args, **kwargs)


class RandomNumberGenerator(Subject):
    def __init__(self, min: int, max: int):
        self.min = min
        self.max = max

    def start_generation(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.generation())

    async def generation(self):
        while True:
            random_num = random.randrange(self.min, self.max)
            self.notify_observers(random_num)
            await asyncio.sleep(1)


class MonitoringWidget(QtWidgets.QWidget, Observer, metaclass=CommonMeta):
    def __init__(self, name: str):
        super().__init__()
        self.text = QtWidgets.QLabel(alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

        self.setWindowTitle(name)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)

    @QtCore.Slot()
    def update(self, random_num):
        self.text.setText(str(random_num))


def temp(gen1):
    app = QtWidgets.QApplication([])

    mw1 = MonitoringWidget("mw1")
    mw1.resize(400, 300)
    mw1.show()

    gen1.register_observer(mw1)

    app.exec()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()

    gen1 = RandomNumberGenerator(5, 10)
    t = Thread(target=temp, args=(gen1,))
    t.start()
    gen1.start_generation()

    loop.run_forever()
