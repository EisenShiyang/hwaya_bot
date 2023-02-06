HELP_USER = """🤖:以下為目前支援的指令~
       /help -> 指令協助
       /code -> 查看程式碼相關
       /id   -> 獲取自己的ID
       /howto-> 指令相關規則
       /list -> 列出已存取的食物
       /location -> 查看已登錄之地點
       /註冊 -> 註冊自己(第一次使用請先註冊)
       /新增 -> 新增食物
       /刪除 -> 刪除食物"""
HELP_GROUP = """🤖:以下為目前支援的指令~
       /help -> 指令協助   
       /howto-> 指令相關規則
       /list -> 列出已存取的食物
       /location -> 查看已登錄之地點
       /新增 -> 新增食物(確認訊息將會傳至私人聊天室)
       /刪除 -> 刪除食物(確認訊息將會傳至私人聊天室)"""
CODE_INFO = """GitHub : https://github.com/EisenShiyang/hwaya_bot
Technologies used : Python, MongoDB, Fly.io
You are welcome to fork the project to add in any feature or optimize the code🤠"""
HOW_TO_USER = """🤖:以下為目前指令的規則~
       1. /註冊 -> ：[名字]
          Ex: /註冊：Shiyang
       2. /新增 -> ：[食物名]～[月日]@位置
          Ex: /新增：牛奶1～5/16@大
       3. /刪除 -> ：[食物名]～[月日]@位置
          Ex: /刪除：牛奶1～5/16@大"""
COMMAND_NOT_FOUND = """🤖: 尚未支援此指令ㄛ🥴
        請輸入 /help 查詢支援指令或 /howto 查詢指令細節"""
LOCATION ="""🤖: 以下為目前已登錄的地點
        1. 大 -> 大冰箱
        2. 小 -> 小冰箱"""
DEVICE_ERROR = "🤖: 逼波逼波!! 目前不支援電腦輸入，請使用手機進行操作唷~"
ACTION_ERROR = """🤖: 逼波逼波!!動作指令有錯誤!! 請查看/help尋求更多幫助"""
NOT_REGISTERED = """🤖: 使用者尚未註冊，請查看/howto並利用[/註冊]指令"""
SYMBOL_ORDER_ERROR = """🤖: 指令符號發生錯誤，請查看/howto了解使用細節"""
LOCATION_ERROR = """🤖: 找不到指定的地點... 請查看/location了解登陸地點"""
NAME_MISSING = """🤖: 你是說...註冊誰? 請查看/howto了解使用細節"""
USER_EXISTED = """🤖: 你已經登錄過嚕~ 想改名請來房間找我🥸"""
REGISTER_SUCCESS = """! 恭喜註冊成功~ 歡迎使用!"""
ADD_SUCCESS = """🤖: 成功加入食物!"""
DELETE_SUCCESS = """🤖: 已刪除"""
ROBOT_EMOJI = """🤖: """
ROBOT_HI = """🤖: 安安"""
FOOD_LIST = """🤖: 目前加入的食物如下"""
FOOD_LIST_EMPTY = """🤖: 還沒加入任何食物捏😫"""
GROUP_NOT_SUPPORT = """🤖: 此指令並不支援"""