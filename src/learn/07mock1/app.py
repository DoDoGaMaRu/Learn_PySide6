import sys

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from daq_system import DAQSystem, Machine, DAQ
from daq_system.data_sender import DataSender
from gui.main_window import MainWindow
from gui.tray_icon import TrayIcon


class App:
    def __init__(self):
        self._load_config()
        self._app = QApplication([])
        self._app.setQuitOnLastWindowClosed(False)

        self._daq = DAQ(self.conf['sensors'])
        self._machines = [Machine(**machine_conf) for machine_conf in self.conf['machines']]
        self._daq_system = DAQSystem(self._machines, self._daq)
        self._daq_system.start()

        ds = DataSender()
        for m in self._machines:
            m.register_observer(ds)

        icon = QIcon("icon.png")
        self._main_window = MainWindow(machines=self._machines)
        self._tray = TrayIcon(main_window=self._main_window, icon=icon)
        self._tray.set_exit_event(self.exit_event)

    def run(self):
        sys.exit(self._app.exec())

    def _load_config(self):
        self.conf = {
            'sensors': ['temp1', 'temp2', 'temp3', 'vib1', 'vib2', 'vib3'],
            'machines': [
                {
                    'name': 'machine1',
                    'sensors': ['temp1', 'vib1']
                },
                {
                    'name': 'machine2',
                    'sensors': ['temp2', 'vib2']
                },
                {
                    'name': 'machine3',
                    'sensors': ['temp3', 'vib3']
                },
            ]
        }

    def exit_event(self): # TODO 에러 핸들링하기
        self._daq_system.exit()
        sys.exit()
