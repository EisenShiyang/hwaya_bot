import re
from Class.Command import Command
from Utils import Checker, Actions, Messages
class ValidationHelper:
    def __init__(self, id, message, messageHelper):
        self.id = id
        self.message = message
        self.messageHelper = messageHelper

    def Execute(self):
        # Check if the user is just typing around
        if '/' not in self.message:
            self.messageHelper.Add(Messages.COMMAND_NOT_FOUND)
            return None

        # Check if the user just wants some help
        if self.AssistanceCheck(self.message) : return Command(self.id, self.message)

        # Check what kind of action that the user want to take
        performAction = re.split('：', self.message)[0]       

        # Check if it is a valid action
        if not self.ActionCheck(performAction):
            self.messageHelper.Add(Messages.ACTION_ERROR)
            return None

        # If the user just wants to sign in
        if performAction == Actions.REGISTER : return self.RegisterValidation()

        # Check if the user hasn't registered yet
        if not self.RegisterCheck(self.id):
            self.messageHelper.Add(Messages.NOT_REGISTERED)
            return None

        # If the action is Add/Delete
        if performAction == Actions.FOOD[0] or performAction == Actions.FOOD[1] : return self.AddDeleteValidation()
        
    def AddDeleteValidation(self):
        # Check if the order of the symbol is correct
        symbolList = [s for s in re.split('\w', self.message) if s != '']
        if not self.AddDeleteSymbolCheck(symbolList):
            self.messageHelper.Add(Messages.SYMBOL_ORDER_ERROR)
            return None
        
        # Extract all labels from the incoming message
        labelList = re.split('：|～|@', self.message)
        # Check if it is a valid location
        if not self.LocationCheck(labelList[3]):
            self.messageHelper.Add(Messages.LOCATION_ERROR)
            return None

        # If all good, set all labels to each attribute of the Command object
        return Command(self.id, labelList[0], labelList[1],labelList[2],labelList[3])

    def RegisterValidation(self):
        # Check if the order of the symbol is correct
        symbolList = [s for s in re.split('\w', self.message) if s != '']
        if not self.RegisterSymbolCheck(symbolList):
            self.messageHelper.Add(Messages.SYMBOL_ORDER_ERROR)
            return None
        
        # Check if the name is entered, if yes, return the object
        name = re.split('：', self.message)[1]
        if not self.NameCheck(name):
            self.messageHelper.Add(Messages.NAME_MISSING)
            return None
        
        return Command(self.id, Actions.REGISTER, name)

    def AssistanceCheck(self, command):
        return Checker.AssistanceCheck(command)

    def RegisterCheck(self, id):
        return Checker.RegisterCheck(id)
    
    def AddDeleteSymbolCheck(self, symbols):
        return Checker.AddDeleteSymbolCheck(symbols)

    def RegisterSymbolCheck(self, symbols):
        return Checker.RegisterSymbolCheck(symbols)
    
    def NameCheck(self, name):
        return Checker.NameCheck(name)

    def ActionCheck(self, action):
        return Checker.ActionCheck(action)
    
    def LocationCheck(self, location):
        return Checker.LocationCheck(location)
    