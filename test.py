# python test.py
from Helper.ActionHelper import ActionHelper
from Helper.ValidationHelper import ValidationHelper
print("TEST STARTS\n")

msg = "/新增:牛奶~12/10@左"
#msg = "/help"
#msg = "123"
validationHelper = ValidationHelper(msg)
food = validationHelper.Execute()
print(food.GetItem())

actionHelper = ActionHelper()
actionHelper.Execute("666")
print(actionHelper.GetResult())

print("\nTEST ENDS")