import asyncio
import random
from typing import List

from observable import Subject


class DAQ(Subject):
    def __init__(self, sensors: List[str]):
        super().__init__()
        self._sensors = sensors

    def start_generation(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.generation())

    async def generation(self):
        while True:
            # 센서 별 초당 20개 데이터 생성
            data = {sensor: [random.random()*10-5 for _ in range(20)] for sensor in self._sensors}
            self.notify_observers(data)
            await asyncio.sleep(1)
