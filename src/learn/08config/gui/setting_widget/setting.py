from typing import List
from PySide6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QPushButton, QLabel, QStackedWidget
from PySide6.QtCore import Qt

from .setting_step.setting_step import QSettingStep


class QSetting(QWidget):
    def __init__(self):
        super().__init__()
        self.cur_step: int = 0

        # Set Layout
        self.layout = QVBoxLayout(self)

        self.header_layout = QHBoxLayout()
        self.content_layout = QHBoxLayout()
        self.bottom_layout = QHBoxLayout()

        self.layout.addLayout(self.header_layout, 1)
        self.layout.addLayout(self.content_layout, 6)
        self.layout.addLayout(self.bottom_layout, 2)

        self._init_header()
        self._init_content()
        self._init_bottom()

        self.go_step(self.cur_step)

    def _init_header(self):
        self.step_label = QLabel()
        self.header_layout.addWidget(self.step_label)

    def _init_content(self):
        self.central_content = QStackedWidget()
        self.central_content.addWidget(QSettingStep())
        self.content_layout.addWidget(self.central_content)

    def _init_bottom(self):
        self.button_layout = QHBoxLayout()
        self.temp = QHBoxLayout()
        self.temp.addWidget(QPushButton(text='Exit'), alignment=Qt.AlignmentFlag.AlignLeft)
        self.bottom_layout.addLayout(self.temp, 5)
        self.bottom_layout.addLayout(self.button_layout, 1)

        self.prev_button = QPushButton(text='Prev')
        self.next_button = QPushButton(text='Next')
        self.prev_button.clicked.connect(self.prev)
        self.next_button.clicked.connect(self.next)

        self.button_layout.addWidget(self.prev_button)
        self.button_layout.addWidget(self.next_button)

    def add_step(self, setting_step: QSettingStep):
        self.central_content.addWidget(setting_step)

    def go_step(self, step: int):
        if 0 < step < self.central_content.count():
            self.cur_step = step
            self.central_content.setCurrentIndex(step)
            self.step_label.setText(f'step {self.cur_step} of {self.central_content.count()-1}')

    def prev(self):
        self.go_step(self.cur_step - 1)

    def next(self):
        if self.central_content.widget(self.cur_step).is_valid():
            self.go_step(self.cur_step + 1)
