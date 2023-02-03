class User:
    def __init__(self, name, id):
        self.name = name
        self.id = id

    def GetName(self):
        return self.name

    def GetId(self):
        return self.id