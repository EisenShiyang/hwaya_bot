import MessageHelper
class ActionHelper:
    _messageHelper = None
    def __init__(self):
        global _messageHelper
        _messageHelper = MessageHelper()
    
    def Execute(action):
        _messageHelper.Add(action)
        _messageHelper.Add("完成!")
    
    def GetResult():
        return _messageHelper.GetMessage()
