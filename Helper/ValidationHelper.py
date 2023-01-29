import re
from Class.Command import Command
import Utils.Checker
import Utils.Actions
import Utils.Locations
import Utils.Symbols
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
        else:
            # Check if the user just wants some help
            if self.AssistanceCheck(self.message) : return Command(self.message)

            # Check what kind of action that the user want to take
            performAction = re.split(':', self.message)[0]
            # Check if it is a valid action
            if not self.ActionCheck(performAction):
                self.messageHelper.Add("Action Error\n")
                return None
            # If the action is Add
            if performAction == Utils.Actions.FOOD[0]:
                return self.AddValidation()
            # If the action is Delete
            if performAction == Utils.Actions.FOOD[1]:
                return self.DeleteValidation()
            
    def AddValidation(self):
        # Check if the order of the symbol is correct
        symbolList = re.split('\w', self.message)
        if not self.AddSymbolCheck(symbolList):
            self.messageHelper.Add("Symbol missing or command error\n")
            return None
        
        # Extract all labels from the incoming message
        labelList = re.split(':|~|@', self.message)
        # Check if it is a valid location
        if not self.LocationCheck(labelList[3]):
            self.messageHelper.Add("Location Error")

        # If there is an error, return none
        # If all good, set all labels to each attribute of the Command object
        return None if len(self.messageHelper.GetMessage()) > 0 else Command(labelList[0], labelList[1],labelList[2],labelList[3])
            

    def DeleteValidation(self):
        print("HIT DELETE")
        return Command("/刪除", "", "","")

    def AssistanceCheck(self, command):
        return Utils.Checker.AssistanceCheck(command)

    def AddSymbolCheck(self, symbols):
        return Utils.Checker.AddSymbolCheck(symbols)

    def ActionCheck(self, action):
        return Utils.Checker.ActionCheck(action)
    
    def LocationCheck(self, location):
        return Utils.Checker.LocationCheck(location)