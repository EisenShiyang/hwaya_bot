# python test.py
from Helper.ActionHelper import ActionHelper
from Helper.ValidationHelper import ValidationHelper
print("TEST STARTS\n")

msg = "/添加:牛奶~12/10@左"
validationHelper = ValidationHelper(msg)
print(validationHelper.Execute())

actionHelper = ActionHelper()
actionHelper.Execute("666")
print(actionHelper.GetResult())

print("\nTEST ENDS")