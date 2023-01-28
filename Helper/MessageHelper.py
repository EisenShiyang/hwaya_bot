class MessageHelper:

    def __init__(self):
        self.message = ""
        
    def Add(self, text):
        self.message += text

    def GetMessage(self):
        return self.message
    