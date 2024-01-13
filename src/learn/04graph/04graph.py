import sys

from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from main_widget import Widget


if __name__ == "__main__":
    data = (
        [0,1,2,3,4,5],
        [0,1,2,3,4,5]
    )

    # Qt Application
    app = QApplication([])

    widget = Widget(data)
    window = MainWindow(widget)
    window.show()

    sys.exit(app.exec())