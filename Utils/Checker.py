from Utils import Actions, Locations, Symbols
from Helper.DatabaseHelper import *

def AssistanceCheck(command):
    return command == Actions.HELP or command == Actions.CODE or command == Actions.ID or command == Actions.HOWTO or command == Actions.LOCATION or command == Actions.LIST

def RegisterCheck(id):
    return CheckRegistered(id)

def AddDeleteSymbolCheck(symbols):
    return symbols == Symbols.ADD_DELETE_SYMBOL_LIST_HALF or symbols == Symbols.ADD_DELETE_SYMBOL_LIST_FULL

def RegisterSymbolCheck(symbols):
    return symbols == Symbols.REGISTER_SYMBOL_LIST_FULL

def NameCheck(name):
    return name != ''

def ActionCheck(action):
    return action in Actions.FOOD or action in Actions.REGISTER

def LocationCheck(location):
    return location in Locations.FRIDGE_HWAYA or location in Locations.FRIDGE_MICRON