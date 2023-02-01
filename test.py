# python test.py
from Helper.ActionHelper import ActionHelper
from Helper.ValidationHelper import ValidationHelper
from Helper.MessageHelper import MessageHelper
import Helper.DatabaseHelper
print("TEST STARTS\n")

msg = "/新增:牛奶~12/10@小"
#msg = "/刪除"
#msg = "/help"
#msg = "123"
Helper.DatabaseHelper.LoadUser()
Helper.DatabaseHelper.LoadFood()
messageHelper = MessageHelper()
validationHelper = ValidationHelper(msg, messageHelper)
food = validationHelper.Execute()
if food:
    print(food.GetItem())
    actionHelper = ActionHelper(food, messageHelper)
    actionHelper.Execute()
    print(messageHelper.GetMessage())
else:
    print(messageHelper.GetMessage())

print("\nTEST ENDS")