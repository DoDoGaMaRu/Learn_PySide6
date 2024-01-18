from abc import ABC, abstractmethod

from PySide6.QtWidgets import QWidget


class QSettingStep(QWidget):

    @abstractmethod
    def is_valid(self) -> bool:
        pass
