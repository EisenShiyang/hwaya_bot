class Command:
    def __init__(self, id, action, item="", date="", location=""):
        self.id = id
        self.action = action
        self.item = item
        self.date = date
        self.location = location

    def GetId(self):
        return self.id

    def GetAction(self):
        return self.action

    def GetItem(self):
        return self.item
    
    def GetDate(self):
        return self.date
    
    def GetLocation(self):
        return self.location