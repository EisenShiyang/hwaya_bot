from Utils import Actions, Messages
from Helper.DatabaseHelper import *
class ActionHelper:
    def __init__(self, command, messageHelper):
        self.command = command
        self.messageHelper = messageHelper
    
    def Execute(self):
        if self.command.GetAction() == Actions.FOOD[0]:
            self.AddFood()
        elif self.command.GetAction() == Actions.FOOD[1]:
            self.DeleteFood()
        elif self.command.GetAction() == Actions.REGISTER:
            self.Register()
        elif self.command.GetAction() == Actions.LIST:
            self.GetFoodList()
    
    def AddFood(self):
        AddFood(self.command)
        self.messageHelper.Add(Messages.ADD_SUCCESS+"位於"+self.command.GetLocation()+"冰箱並將於"+self.command.GetDate()+"過期的"+self.command.GetItem())

    def DeleteFood(self):
        result = DeleteFood(self.command)
        if result.deleted_count == 0:
            self.messageHelper.Add(Messages.DELETE_FOOD_NOT_FOUND)
        else:
            self.messageHelper.Add(Messages.DELETE_SUCCESS+"位於"+self.command.GetLocation()+"冰箱並將於"+self.command.GetDate()+"過期的"+self.command.GetItem())

    def Register(self):
        # Call register function in DatabaseHelper
        result = Register(self.command.GetId(), self.command.GetItem())
        if result is None:
            self.messageHelper.Add(Messages.USER_EXISTED)
        else:
            self.messageHelper.Add(Messages.ROBOT_EMOJI + "Hi " + self.command.GetItem() + Messages.REGISTER_SUCCESS)

    def GetFoodList(self):
        food_list_count, food_list = LoadFood(self.command.GetId())
        if food_list_count > 0:
            self.messageHelper.Add(Messages.FOOD_LIST)
            self.messageHelper.ConstructFoodList(food_list)
        else:
            self.messageHelper.Add(Messages.FOOD_LIST_EMPTY)
        