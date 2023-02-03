# python test.py
from Helper.ActionHelper import ActionHelper
from Helper.ValidationHelper import ValidationHelper
from Helper.MessageHelper import MessageHelper
import Helper.DatabaseHelper
print("TEST STARTS\n")

#msg = "/新增：牛奶1～12/10@小"
msg = "/註冊：Hank"
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