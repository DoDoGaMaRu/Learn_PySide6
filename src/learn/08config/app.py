import sys

from PySide6.QtWidgets import QApplication

from util.config_loader import ConfigLoader
from gui.main_window import MainWindow
from gui.setting_widget.setting import QSetting
from gui.setting_widget.setting_step.device_setting_step import QDeviceSettingStep


class App:
    def __init__(self):
        self._conf = ConfigLoader.load_conf()
        self._app = QApplication([])
        self._app.setQuitOnLastWindowClosed(True)

        self._setting_step = QSetting()
        self._init_setting_step()
        self._main_window = MainWindow(self._setting_step)

    def run(self):
        sys.exit(self._app.exec())

    def _init_setting_step(self):
        self._setting_step.add_step(QDeviceSettingStep())
        self._setting_step.go_step(1)


