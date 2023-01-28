import re
from Helper.Class.Command import Command
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
            # Check if the order of the symbol is correct
            symbolList = re.split('\w', self.message)
            if not self.SymbolCheck(symbolList):
                self.messageHelper.Add("Symbol missing or command error\n")
                return None
            else:
                # Extract all labels from the incoming message
                labelList = re.split(':|~|@', self.message)
                print(labelList)
                # Check if it is a valid action
                if not self.ActionCheck(labelList[0]):
                    self.messageHelper.Add("Action Error\n")
                # Check if it is a valid location
                if not self.LocationCheck(labelList[3]):
                    self.messageHelper.Add("Location Error")
                # If there is an error, return none
                if len(self.messageHelper.GetMessage()) > 0:
                    return None
                # If all good, set all labels to each attribute of the Command object
                return Command(labelList[0], labelList[1],labelList[2],labelList[3])

    def AssistanceCheck(self, command):
        return command in Utils.Actions.HELP or command in Utils.Actions.CODE

    def SymbolCheck(self, symbols):
        return symbols == Utils.Symbols.SYMBOL_LIST

    def ActionCheck(self, action):
        return action in Utils.Actions.FOOD
    
    def LocationCheck(self, location):
        return location in Utils.Locations.FRIDGE_HWAYA or location in Utils.Locations.FRIDGE_MICRON