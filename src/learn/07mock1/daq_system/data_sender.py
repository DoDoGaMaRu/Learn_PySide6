from datetime import datetime

from observable import Observer


class DataSender(Observer):
    def update(self, data):
        print(datetime.today(), data)
