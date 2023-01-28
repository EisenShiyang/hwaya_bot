from Helper.MessageHelper import MessageHelper
class ActionHelper:

    def __init__(self):
        self._messageHelper = MessageHelper()
    
    def Execute(self, action):
        self._messageHelper.Add(action)
        self._messageHelper.Add("完成!")
    
    def GetResult(self):
        return self._messageHelper.GetMessage()
