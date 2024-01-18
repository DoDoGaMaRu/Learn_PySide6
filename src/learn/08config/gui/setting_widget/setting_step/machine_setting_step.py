from .setting_step import QSettingStep


class QMachineSettingStep(QSettingStep):
    def is_valid(self) -> bool:
        return True
