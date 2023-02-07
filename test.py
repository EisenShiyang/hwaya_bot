# python test.py
from Helper.ActionHelper import ActionHelper
from Helper.ValidationHelper import ValidationHelper
from Helper.MessageHelper import MessageHelper
from Helper.DateHelper import *
from Helper.DatabaseHelper import *
from Class.Food import Food
from Utils import Messages
from datetime import datetime
print("TEST STARTS\n")

# user = {'id' : "Ub4f02f5551c8df3eda2a9d429f8e9d9d", 'name' : "Hank"}
# msg = "/新增：醬味糙米餅～3/24@零食"
# messageHelper = MessageHelper()
# validationHelper = ValidationHelper(user['id'], msg, messageHelper)
# command = validationHelper.Execute()
# actionHelper = ActionHelper(command, messageHelper)
# actionHelper.Execute()

# print(messageHelper.GetMessage())

user_list = LoadUser()
# For each user registered, will check their stored food and send them message if needed
for user in user_list:
    messageHelper = MessageHelper()
    # Retrieve foods that expire on that day
    the_day_food_count, the_day_food_list = GetTheDayFood(user['id'])
    if the_day_food_count > 0:
        messageHelper.Add(Messages.ROBOT_HI + user['name'] + "，以下物品已於今日到期，請記得處理!")
        messageHelper.ConstructTheDayFoodWithoutRemoval(user['id'], the_day_food_list)
            
    # Retrieve foods that will expire in the following three days
    three_days_food_count, three_days_food_list = GetThreeDaysFood(user['id'])
    if three_days_food_count > 0:
        if the_day_food_count > 0: messageHelper.Add("\n")
        messageHelper.Add(Messages.ROBOT_HI + user['name'] + "，以下物品將於三天之內過期，請盡快食用!")
        messageHelper.ConstructThreeDaysFood(three_days_food_list)
    
    # If it is the first day of that month, generate a monthly report
    day_today = datetime.now().day
    the_month_food_count = 0
    if day_today == 8:
        the_month_food_count, the_month_food_list = GetTheMonthFood(user['id'])
        if the_month_food_count > 0:
            if the_day_food_count > 0 or three_days_food_count > 0 : messageHelper.Add("\n")
            messageHelper.Add(Messages.ROBOT_HI + user['name'] + "，以下物品將於這個月過期，請多多注意嚕～")
            messageHelper.ConstructTheMonthFood(the_month_food_list)
    
    if the_day_food_count > 0 or three_days_food_count > 0 or the_month_food_count > 0:
        print(messageHelper.GetMessage())
    
    
    

print("\nTEST ENDS")