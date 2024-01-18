from dataclasses import dataclass
from typing import List
from abc import ABC, abstractmethod


@dataclass
class ActivableModeConfig(ABC):
    ACTIVATE        : bool

    def __post_init__(self):
        if self.ACTIVATE:
            self.valid_check()

    @abstractmethod
    def valid_check(self):
        pass


@dataclass
class FaultDetectModeConfig(ActivableModeConfig):
    THRESHOLD       : int

    def valid_check(self):
        pass


@dataclass
class MachineConfig:
    NAME            : str
    SENSORS         : List[str]

    FAULT_DETECT_MODE    : FaultDetectModeConfig
