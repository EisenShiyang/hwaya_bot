import Utils.Actions
import Utils.Locations
import Utils.Symbols

def AssistanceCheck(command):
    return command in Utils.Actions.HELP or command in Utils.Actions.CODE

def SymbolCheck(symbols):
    return symbols == Utils.Symbols.SYMBOL_LIST

def ActionCheck(action):
    return action in Utils.Actions.FOOD

def LocationCheck(location):
    return location in Utils.Locations.FRIDGE_HWAYA or location in Utils.Locations.FRIDGE_MICRON