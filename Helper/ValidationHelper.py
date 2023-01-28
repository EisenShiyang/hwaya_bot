import re
from Helper.Class.Command import Command
import Utils.Actions
class ValidationHelper:
    def __init__(self, message):
        self.message = message

    def Execute(self):
        # Check if the user just wants some help
        if self.AssistanceCheck(self.message) : return Command(self.message)
        # Check if the order of the symbol is correct
        symbolList = re.split('\w', self.message)
        if not self.SymbolCheck(symbolList) : return None
        # Extract all labels from the incoming message
        labelList = re.split(':|~|@', self.message)
        # Check if it is a valid action
        if not self.ActionCheck(labelList[0]) : return None
        # If all good, set all labels to each attribute of the Command object
        return Command(labelList[0], labelList[1],labelList[2],labelList[3])

    def AssistanceCheck(self, command):
        return command in Utils.Actions.HELP or command in Utils.Actions.CODE

    def SymbolCheck(self, symbols):
        desiredList = ['/', '', ':', '', '~', '', '/', '', '@', '']
        return symbols == desiredList

    def ActionCheck(self, action):
        return action in Utils.Actions.FOOD