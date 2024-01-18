import yaml

from typing import Dict
from os import path, makedirs


class ConfigLoader:
    CONF_PATH = 'resources/config.yml'
    DEFAULT_CONF = {
        'DAQ': {
            'DEVICE_CONFIGS': []
        },
        'MACHINES': []
    }

    @staticmethod
    def load_conf() -> Dict:
        if not path.isfile(ConfigLoader.CONF_PATH):
            dir_path = path.dirname(ConfigLoader.CONF_PATH)
            makedirs(dir_path, exist_ok=True)
            open(ConfigLoader.CONF_PATH, 'w')

        with open(ConfigLoader.CONF_PATH, 'r', encoding='UTF-8') as yml:
            conf = yaml.safe_load(yml)
            if not is_valid_conf(conf):
                conf = ConfigLoader.DEFAULT_CONF

        return conf

    @staticmethod
    def save_conf(conf: Dict) -> None:
        if not path.isfile(ConfigLoader.CONF_PATH):
            dir_path = path.dirname(ConfigLoader.CONF_PATH)
            makedirs(dir_path, exist_ok=True)
            open(ConfigLoader.CONF_PATH, 'w')

        with open(ConfigLoader.CONF_PATH, 'w', encoding='UTF-8') as yml:
            yaml.safe_dump(conf, yml, default_flow_style=False)


def is_valid_conf(conf: Dict) -> bool:
    if conf is None:
        return False
    if 'DAQ' not in conf.keys():
        return False
    if 'MACHINES' not in conf.keys():
        return False
    return True
