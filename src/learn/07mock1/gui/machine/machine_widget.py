from typing import List, Dict

from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QHBoxLayout, QLabel

from daq_system import Machine
from .realtime_chart import RealtimeChartWidget
from observable import Observer


class CommonMeta(type(QWidget), type(Observer)):
    pass


class MachineWidget(QWidget, Observer, metaclass=CommonMeta):
    def __init__(self, machine: Machine):
        super().__init__()
        self._machine = machine
        self._machine.register_observer(self)

        self.charts: Dict[str, RealtimeChartWidget] = {}
        self.layout = QHBoxLayout(self)

        for sensor in self._machine.get_sensors():
            new_chart = RealtimeChartWidget(sensor, 320)
            self.layout.addWidget(new_chart)
            self.charts[sensor] = new_chart

    @QtCore.Slot()
    def update(self, named_data: Dict[str, List[float]]):
        for name, datas in named_data.items():
            if name not in self.charts.keys():
                new_chart = RealtimeChartWidget(name, 320)
                self.layout.addWidget(new_chart)
                self.charts[name] = new_chart
            self.charts[name].append_data(datas)

    def remove_subject(self):
        self._machine.remove_observer(self)
        self._machine = None
