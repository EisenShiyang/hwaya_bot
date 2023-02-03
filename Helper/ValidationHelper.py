import re
from Class.Command import Command
from Class.User import User
import Utils.Checker
import Utils.Actions
import Utils.Messages
class ValidationHelper:
    def __init__(self, message, messageHelper):
        self.message = message
        self.messageHelper = messageHelper

    def Execute(self):
        # Check if the user is just typing around
        if '/' not in self.message:
            self.messageHelper.Add(Utils.Messages.COMMAND_NOT_FOUND)
            return None

        # Check if the user just wants some help
        if self.AssistanceCheck(self.message) : return Command(self.message)

        # Check what kind of action that the user want to take
        performAction = re.split(':', self.message)[0]
        # TODO : Check the user has registered or not        

        # Check if it is a valid action
        if not self.ActionCheck(performAction):
            self.messageHelper.Add("Action Error\n")
            return None

        # If the action is Add/Delete
        if performAction == Utils.Actions.FOOD[0] or performAction == Utils.Actions.FOOD[1] : return self.AddDeleteValidation()
        
        # If the user just wants to sign in
        print(re.split('\w', self.message))
        name = re.split(':', self.message)[1]
        if performAction == Utils.Actions.REGISTER : return self.RegisterValidation(name)

    def AddDeleteValidation(self):
        # Check if the order of the symbol is correct
        symbolList = re.split('\w', self.message)
        if not self.AddDeleteSymbolCheck(symbolList):
            self.messageHelper.Add("Symbol missing or command error\n")
            return None
        
        # Extract all labels from the incoming message
        labelList = re.split(':|~|@', self.message)
        # Check if it is a valid location
        if not self.LocationCheck(labelList[3]):
            self.messageHelper.Add("Location Error")
            return None

        # If all good, set all labels to each attribute of the Command object
        return Command(labelList[0], labelList[1],labelList[2],labelList[3])

    def RegisterValidation(self,name):
        return Command(Utils.Actions.REGISTER, name)

    def AssistanceCheck(self, command):
        return Utils.Checker.AssistanceCheck(command)

    def AddDeleteSymbolCheck(self, symbols):
        return Utils.Checker.AddDeleteSymbolCheck(symbols)

    def ActionCheck(self, action):
        return Utils.Checker.ActionCheck(action)
    
    def LocationCheck(self, location):
        return Utils.Checker.LocationCheck(location)