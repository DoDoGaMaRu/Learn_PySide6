import sys
from typing import List
from PySide6.QtGui import QIcon, QAction
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QMainWindow

from daq_system.machine import Machine
from .machine.machine_widget import MachineWidget


class FunctionExecutor:
    def __init__(self, proc, *args, **kwargs):
        self.proc = proc
        self.args = args
        self.kwargs = kwargs

    def __call__(self):
        self.proc(*self.args, **self.kwargs)


class MainWindow(QMainWindow):
    def __init__(self, machines: List[Machine]):
        super().__init__()
        # Environ Setting
        self._machines: List[Machine] = machines

        # Menu
        self._menu = self.menuBar()
        self._init_machine_menu()

        # Window Setting
        self.setFixedSize(1280, 720)
        self.status = self.statusBar()
        self.show()

    def _init_machine_menu(self):
        self._machine_menu = self._menu.addMenu("Machine")
        for machine in self._machines:
            select_action = QAction(machine.get_name(), self)
            select_action.triggered.connect(FunctionExecutor(self.set_machine_widget, machine))
            self._machine_menu.addAction(select_action)

    def set_machine_widget(self, machine):
        central_widget = self.centralWidget()
        if isinstance(central_widget, MachineWidget):
            central_widget.remove_subject()

        machine_widget = MachineWidget(machine)
        self.setCentralWidget(machine_widget)
        self.status.showMessage(machine.get_name())
