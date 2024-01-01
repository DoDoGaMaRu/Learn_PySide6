from observable import Observer, Subject


class Machine(Observer, Subject):
    def update(self, data):
        self.notify_observers(data)
