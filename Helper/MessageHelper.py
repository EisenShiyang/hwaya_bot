from Class.Food import Food
from Helper.DatabaseHelper import *
class MessageHelper:

    def __init__(self):
        self.message = ""
        
    def Add(self, text):
        self.message += text

    def GetMessage(self):
        return self.message
    
    def ConstructFoodList(self, foodList):
        count = 1
        for food in foodList:
            added_food = Food(food['item'], food['date'], food['location'])
            self.Add("\n" + str(count) + ". " + added_food.GetItem() + " 位於 " + added_food.GetLocation() + " 將於 " + added_food.GetDate() + "過期")
            count = count + 1
    
    def ConstructTheDayFood(self, id, foodList):
        count = 1
        for food in foodList:
            alert_food = Food(food['item'], food['date'], food['location'])
            self.Add("\n" + str(count) + ". " + alert_food.GetItem() + " 位於 " + alert_food.GetLocation())
            count = count + 1
            RemoveTheDayFood(id, alert_food)
            
    def ConstructTheDayFoodWithoutRemoval(self, id, foodList):
        count = 1
        for food in foodList:
            alert_food = Food(food['item'], food['date'], food['location'])
            self.Add("\n" + str(count) + ". " + alert_food.GetItem() + " 位於 " + alert_food.GetLocation())
            count = count + 1
            
    def ConstructThreeDaysFood(self, foodList):
        count = 1
        for food in foodList:
            alert_food = Food(food['item'], food['date'], food['location'])
            self.Add("\n" + str(count) + ". " + alert_food.GetItem() + " 位於 " + alert_food.GetLocation() + " 將於 " + alert_food.GetDate() + "過期")
            count = count + 1
    
    def ConstructTheMonthFood(self, foodList):
        count = 1
        for food in foodList:
            alert_food = Food(food['item'], food['date'], food['location'])
            self.Add("\n" + str(count) + ". " + alert_food.GetItem() + " 位於 " + alert_food.GetLocation() + " 將於 " + alert_food.GetDate() + "過期")
            count = count + 1