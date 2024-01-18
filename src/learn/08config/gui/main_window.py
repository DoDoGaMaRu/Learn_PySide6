from PySide6.QtWidgets import QMainWindow


class MainWindow(QMainWindow):
    def __init__(self, widget):
        super().__init__()
        # Environ Setting

        # Menu
        self._menu = self.menuBar()
        self._init_menu()

        # Window Setting
        self.setFixedSize(1280, 720)
        self.status = self.statusBar()
        self.show()

        self.setCentralWidget(widget)

    def _init_menu(self):
        pass
