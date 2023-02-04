from Utils import Actions, Messages
from Helper.DatabaseHelper import *
class ActionHelper:
    def __init__(self, command, messageHelper):
        self.command = command
        self._messageHelper = messageHelper
    
    def Execute(self):
        if self.command.GetAction() == Actions.FOOD[0]:
            self.AddFood()
        elif self.command.GetAction() == Actions.FOOD[1]:
            self.DeleteFood()
        elif self.command.GetAction() == Actions.REGISTER:
            self.Register()
    
    def AddFood(self):
        AddFood(self.command)
        self._messageHelper.Add(Messages.ADD_SUCCESS)

    def DeleteFood(self):
        DeleteFood(self.command)
        self._messageHelper.Add(Messages.DELETE_SUCCESS+"位於"+self.command.GetLocation()+"並將於"+self.command.GetDate()+"過期的"+self.command.GetItem())

    def Register(self):
        # Call register function in DatabaseHelper
        result = Register(self.command.GetId(), self.command.GetItem())
        if result is None:
            self._messageHelper.Add(Messages.USER_EXISTED)
        else:
            self._messageHelper.Add(Messages.ROBOT_EMOJI + "Hi " + self.command.GetItem() + Messages.REGISTER_SUCCESS)

