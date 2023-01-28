class Command:
    def __init__(self, action, item="", date="", location=""):
        self.action = action
        self.item = item
        self.date = date
        self.location = location

    def GetAction(self):
        return self.action

    def GetItem(self):
        return self.item
    
    def GetDate(self):
        return self.date
    
    def GetLocation(self):
        return self.location