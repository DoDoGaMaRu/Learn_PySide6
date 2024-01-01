import asyncio
import random

from observable import Subject


class DAQ(Subject):
    def __init__(self, _min: int, _max: int):
        super().__init__()
        self._min = _min
        self._max = _max

    def start_generation(self):
        loop = asyncio.get_event_loop()
        loop.create_task(self.generation())

    async def generation(self):
        while True:
            random_num = random.randrange(self._min, self._max)
            self.notify_observers(random_num)
            await asyncio.sleep(1)
