from PySide6 import QtCore, QtWidgets

from daq_system.daq import DAQ
from daq_system.daq_system import DAQSystem
from daq_system.machine import Machine
from daq_system.data_sender import DataSender
from observable import Observer


class CommonMeta(type(QtWidgets.QWidget), type(Observer)):
    pass


class MonitoringWidget(QtWidgets.QWidget, Observer, metaclass=CommonMeta):
    def __init__(self):
        super().__init__()
        self.text = QtWidgets.QLabel(alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)

    @QtCore.Slot()
    def update(self, random_num):
        self.text.setText(str(random_num))


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        m1 = Machine()

        mw = MonitoringWidget()
        m1.register_observer(mw)

        ds = DataSender()
        m1.register_observer(ds)

        daq = DAQ(0, 20)
        self.daq_system = DAQSystem(machines=[m1], daq=daq)
        self.daq_system.start()
        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(mw)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    window = MyWidget()
    window.resize(400, 300)
    window.show()

    app.exec()
