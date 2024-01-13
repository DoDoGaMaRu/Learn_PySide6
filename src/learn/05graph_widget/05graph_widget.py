import sys
import random

from PySide6.QtCore import QThread, SIGNAL
import time

from PySide6.QtGui import QAction, QKeySequence
from PySide6.QtWidgets import QWidget, QMainWindow, QApplication
from realtime_chart import RealtimeChartWidget


class Worker(QThread):
    def __init__(self, proc):
        super().__init__()
        self.proc = proc

    def run(self):
        while True:
            for _ in range(20):
                self.emit(SIGNAL(self.proc(random.random()*10)))
            time.sleep(1)


class MainWindow(QMainWindow):
    def __init__(self, name: str, widget: QWidget):
        QMainWindow.__init__(self)
        self.setWindowTitle(name)
        self.setCentralWidget(widget)

        # Menu
        self.menu = self.menuBar()
        self.exit_menu = self.menu.addMenu("Menu")

        # Exit QAction
        exit_action = QAction("Exit", self)
        exit_action.setShortcut(QKeySequence.Quit)
        exit_action.triggered.connect(self.close)
        self.exit_menu.addAction(exit_action)

        # Status Bar
        self.status = self.statusBar()
        self.status.showMessage("Running")

        # Set Size
        # geometry = self.screen().availableGeometry()
        self.setFixedSize(720, 480)


if __name__ == "__main__":
    app = QApplication([])

    chart_widget = RealtimeChartWidget("temp", 160)
    window = MainWindow("Chart View", chart_widget)
    window.show()

    worker = Worker(chart_widget.append_data)
    worker.start()

    sys.exit(app.exec())
