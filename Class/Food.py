class Food:
    def __init__(self, item, date, location):
        self.item = item
        self.date = date
        self.location = location

    def GetItem(self):
        return self.item

    def GetLocation(self):
        return self.location

    def GetDate(self):
        return self.date.strftime("%m/%d")