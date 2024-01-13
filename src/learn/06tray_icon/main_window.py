import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QSystemTrayIcon, QMenu, QMainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setFixedSize(640, 480)

        self.tray = QSystemTrayIcon()
        if self.tray.isSystemTrayAvailable():
            icon = QIcon("icon.png")
            self.tray.setIcon(icon)
            self.tray.activated.connect(self.tray_activated)

            menu = QMenu()
            exit_action = menu.addAction("quit")
            exit_action.triggered.connect(sys.exit)

            self.tray.setContextMenu(menu)
            self.tray.show()
            self.tray.setToolTip("icon hover event")
            self.tray.showMessage("DAQSystem", "System Started")
        else:
            self.tray = None
        self.show()

    def tray_activated(self, reason):
        if reason == QSystemTrayIcon.Trigger or reason == QSystemTrayIcon.DoubleClick:
            self.activateWindow() if self.isVisible() else self.show()
