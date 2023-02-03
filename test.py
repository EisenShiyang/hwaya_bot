# python test.py
from Helper.ActionHelper import ActionHelper
from Helper.ValidationHelper import ValidationHelper
from Helper.MessageHelper import MessageHelper
from Helper.DateHelper import *
print("TEST STARTS\n")

CheckYear("2/9")
print(GetCurrentTime())
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