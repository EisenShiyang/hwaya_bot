import Utils.Actions
import Utils.Locations
import Utils.Symbols

def AssistanceCheck(command):
    return command == Utils.Actions.HELP or command == Utils.Actions.CODE or command == Utils.Actions.ID or command == Utils.Actions.HOWTO

def RegisterCheck(command):
    return True

def AddDeleteSymbolCheck(symbols):
    return symbols == Utils.Symbols.ADD_DELETE_SYMBOL_LIST_HALF or symbols == Utils.Symbols.ADD_DELETE_SYMBOL_LIST_FULL

def RegisterSymbolCheck(symbols):
    return symbols == Utils.Symbols.REGISTER_SYMBOL_LIST_HALF or symbols == Utils.Symbols.REGISTER_SYMBOL_LIST_FULL

def NameCheck(name):
    return name != ''

def ActionCheck(action):
    return action in Utils.Actions.FOOD or action in Utils.Actions.REGISTER

def LocationCheck(location):
    return location in Utils.Locations.FRIDGE_HWAYA or location in Utils.Locations.FRIDGE_MICRON