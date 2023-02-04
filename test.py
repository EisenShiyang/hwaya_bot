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

now = datetime.now()
print(now.strftime("%H:%M:%S"))
if now.strftime("%H:%M:S") == "13:06":
    print("LALALALA")

user = {'id' : "Ub4f02f5551c8df3eda2a9d429f8e9d9d", 'name' : "Hank"}

messageHelper = MessageHelper()

# # Retrieve foods that are expired on that day
# the_day_food_count, the_day_food_list = GetTheDayFood(user['id'])
# if the_day_food_count > 0:
#     count = 1
#     messageHelper.Add(Messages.ROBOT_HI + user['name'] + "，以下物品已於今日到期，請記得處理!\n")
#     for food in the_day_food_list:
#         alert_food = Food(food['item'], food['date'], food['Location'])
#         messageHelper.Add(str(count) + ". " + alert_food.GetItem() + " 位於 " + alert_food.GetLocation()+"\n")
#         count = count + 1
# # Retrieve foods that will expire in the following three days
# three_days_food_count, three_days_food_list = GetThreeDaysFood(user['id'])
# if three_days_food_count > 0:
#     count = 1
#     messageHelper.Add(Messages.ROBOT_HI + user['name'] + "，以下物品將於三天之類過期，請盡快食用!\n")
#     for food in three_days_food_list:
#         alert_food = Food(food['item'], food['date'], food['Location'])
#         messageHelper.Add(str(count) + ". " + alert_food.GetItem() + " 位於 " + alert_food.GetLocation() + " 將於 " + alert_food.GetDate() + "過期\n")
#         count = count + 1

# print(messageHelper.GetMessage())
msg = "/新增：牛奶1～1/30@小"
#msg = "/註冊：Hank"
#msg = "/刪除"
#msg = "/help"
#msg = "123"
messageHelper = MessageHelper()
validationHelper = ValidationHelper("123",msg, messageHelper)
food = validationHelper.Execute()
if food:
    print(food.GetItem())
    actionHelper = ActionHelper(food, messageHelper)
    actionHelper.Execute()
    print(messageHelper.GetMessage())
else:
    print(messageHelper.GetMessage())

print("\nTEST ENDS")