from PySide6.QtWidgets import QVBoxLayout, QLabel, QLineEdit, QHBoxLayout

from .setting_step import QSettingStep


class QDeviceSettingStep(QSettingStep):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.addWidget(QDeviceSetting())

    def is_valid(self) -> bool:
        return True


class QDeviceSetting(QSettingStep):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.set_name = QHBoxLayout()
        self.set_rate = QHBoxLayout()

        self.name_label = QLabel('name : ')
        self.rate_label = QLabel('rate : ')
        self.name_input = QLineEdit(self)
        self.rate_input = QLineEdit(self)

        self.set_name.addWidget(self.name_label, stretch=2)
        self.set_name.addWidget(self.name_input, stretch=5)

        self.set_rate.addWidget(self.rate_label, stretch=2)
        self.set_rate.addWidget(self.rate_input, stretch=5)

        self.layout.addLayout(self.set_name)
        self.layout.addLayout(self.set_rate)

    def is_valid(self) -> bool:
        return True


class QSensorSetting(QSettingStep):
    def is_valid(self) -> bool:
        return True
