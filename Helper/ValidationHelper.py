import re
from Helper.Class.Food import Food
import Utils.Actions

class ValidationHelper:
    def __init__(self, message):
        self.message = message
        self.Food = None

    def Execute(self):
        symbolList = re.split('\w', self.message)
        if not self.SymbolCheck(symbolList) : return self.Food
        labelList = re.split(':|~|@', self.message)
        if not self.ActionCheck(labelList[0]) : return self.Food
        self.Food = Food(labelList[0], labelList[1],labelList[2],labelList[3])
        return self.Food

    def SymbolCheck(self, symbols):
        desiredList = ['/', '', ':', '', '~', '', '/', '', '@', '']
        return symbols == desiredList

    def ActionCheck(self, action):
        return action in Utils.Actions.FOOD