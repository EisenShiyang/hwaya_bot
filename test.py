# python test.py
from Helper.ActionHelper import ActionHelper
print("TEST STARTS")

actionHelper = ActionHelper()
actionHelper.Execute("666")
print(actionHelper.GetResult())

print("TEST ENDS")