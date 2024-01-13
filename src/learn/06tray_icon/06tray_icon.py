import sys
from PySide6.QtWidgets import QApplication

from main_window import MainWindow


class App:
    def __init__(self):
        self._app = QApplication([])
        self._app.setQuitOnLastWindowClosed(False) # 마지막 창이 꺼져도 프로그램이 종료되지 않음

        self._main_window = MainWindow()

    def run(self):
        sys.exit(self._app.exec())


if __name__ == '__main__':
    app = App()
    app.run()
