from typing import List

from observable import Observer, Subject


class Machine(Observer, Subject):
    def __init__(self, name: str, sensors: List[str]):
        super().__init__()
        self._name = name
        self._sensors = sensors

    def get_name(self):
        return self._name

    def get_sensors(self):
        return self._sensors

    def update(self, data):
        filtered_data = {}
        for sensor in self._sensors:
            filtered_data[sensor] = data[sensor]
        self.notify_observers(filtered_data)
