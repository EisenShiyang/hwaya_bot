class ActionHelper:

    def __init__(self, command, messageHelper):
        self.command = command
        self._messageHelper = messageHelper
    
    def Execute(self):
        self._messageHelper.Add(self.command.GetAction())
