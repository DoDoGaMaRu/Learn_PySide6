import asyncio
from typing import List

from PySide6.QtCore import QThread

from .daq import DAQ
from .machine import Machine


class DAQSystem(QThread):
    def __init__(self, machines: List[Machine], daq: DAQ):
        super().__init__()
        self._machines = machines
        self._daq = daq

        self._daq.register_observer(*self._machines)

    def run(self) -> None:
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        self._daq.start_generation()

        loop.run_forever()
