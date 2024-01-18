from typing import Dict

from app import App
from util.config_loader import ConfigLoader
from background.machine.machine_config import MachineConfig
from background.daq.device.device_config import DeviceConfig


def add_temp_conf(conf: Dict) -> Dict:
    conf['DAQ']['DEVICE_CONFIGS'] = [
        {
            'NAME': 'temp_device1',
            'RATE': 30,
            'SENSORS': [
                {
                    'NAME': 'temp1',
                    'CHANNEL': 'ai0',
                    'OPTIONS': {}
                },
                {
                    'NAME': 'temp2',
                    'CHANNEL': 'ai1',
                    'OPTIONS': {}
                },
            ],
        },
        {
            'NAME': 'vib_device1',
            'RATE': 20,
            'SENSORS': [
                {
                    'NAME': 'vib1',
                    'CHANNEL': 'ai0',
                    'OPTIONS': {}
                },
                {
                    'NAME': 'vib2',
                    'CHANNEL': 'ai1',
                    'OPTIONS': {}
                },
            ],
        },
    ]

    conf['MACHINES'].append({
        'MACHINE_CONFIG': {
            'NAME': 'machine1',
            'SENSORS': ['temp1', 'vib1'],
            'FAULT_DETECT_MODE': {
                'ACTIVATE': True,
                'THRESHOLD': 500,
            },
        },
        'DATA_SEND': {
            'ACTIVATE': True,
            'HOST': '127.0.0.1',
            'PORT': 8082,
            'TIMEOUT': 60,
        }
    })
    return conf


if __name__ == '__main__':
    # conf = ConfigLoader.load_conf()
    # # conf = add_temp_conf(conf)
    # machine_configs = [MachineConfig(**m_conf['MACHINE_CONFIG']) for m_conf in conf['MACHINES']]
    # device_configs = [DeviceConfig(**d_conf) for d_conf in conf['DAQ']['DEVICE_CONFIGS']]
    #
    # ConfigLoader.save_conf(conf)
    # print(conf)
    app = App()
    app.run()
