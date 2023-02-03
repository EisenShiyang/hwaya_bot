import Utils.Actions
from Helper.DatabaseHelper import *
class ActionHelper:
    def __init__(self, command, messageHelper):
        self.command = command
        self._messageHelper = messageHelper
    
    def Execute(self):
        if self.command.GetAction() == Utils.Actions.FOOD[0]:
            self.AddFood()
        elif self.command.GetAction() == Utils.Actions.FOOD[1]:
            self.DeleteFood()
        elif self.command.GetAction() == Utils.Actions.REGISTER:
            self.Register()
    
    def AddFood(self):
        result = AddFood(self.command)
        self._messageHelper.Add(self.command.GetAction()+"\n")

    def DeleteFood(self):
        self._messageHelper.Add(self.command.GetAction()+"\n")

    def Register(self):
        # Call register function in DatabaseHelper
        result = Register(self.command.GetId(), self.command.GetItem())
        if result is None:
            self._messageHelper.Add("User Already Exists")
        else:
            self._messageHelper.Add(self.command.GetAction()+" Success!\n")

