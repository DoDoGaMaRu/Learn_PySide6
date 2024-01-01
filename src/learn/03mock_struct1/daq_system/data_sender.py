from observable import Observer


class DataSender(Observer):
    def update(self, data):
        print(data)
