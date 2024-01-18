from dataclasses import dataclass
from typing import List, Dict


@dataclass
class SensorConfig:
    NAME            : str
    CHANNEL         : str
    OPTIONS         : Dict[str, any]


@dataclass
class DeviceConfig:
    NAME            : str
    RATE            : int
    SENSORS         : List[SensorConfig]

    def __post_init__(self):
        if isinstance(self.SENSORS, Dict):
            self.SENSORS = [SensorConfig(**sensor_conf) for sensor_conf in self.SENSORS]
