from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import threading
from datetime import datetime
import time
from Utils import Actions, Messages
from Helper.MessageHelper import MessageHelper
from Helper.ValidationHelper import ValidationHelper
from Helper.ActionHelper import ActionHelper
from Helper.DatabaseHelper import *
from Class.Food import Food

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('2ntK2P9daJrdC8r0dyZ6AVe5jDfGIdf27wOWkn1pZ/VZEMOOjKhthuh3+7nya1ikWpLY3L2qVgagiKnplJPV8RncoLFgkvECh4yaMVhLL84zYo+Jl4rZfpzzPJKYaX3uhgEKdjxBlENDcpgGA+HPagdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('a7142968d06edae024e33e9f592d5413')

def push_message():
    while 1 == 1:
        # Execute every day
        time.sleep(20)
        # Load registered user
        user_list = LoadUser()
        # For each user registered, will check their stored food and send them message if needed
        for user in user_list:
            messageHelper = MessageHelper()
            # Retrieve foods that expire on that day
            the_day_food_count, the_day_food_list = GetTheDayFood(user['id'])
            if the_day_food_count > 0:
                messageHelper.Add(Messages.ROBOT_HI + user['name'] + "，以下物品已於今日到期，請記得處理!\n")
                messageHelper.ConstructTheDayFood(user['id'], the_day_food_list)
                    
            # Retrieve foods that will expire in the following three days
            three_days_food_count, three_days_food_list = GetThreeDaysFood(user['id'])
            if three_days_food_count > 0:
                count = 1
                messageHelper.Add(Messages.ROBOT_HI + user['name'] + "，以下物品將於三天之類過期，請盡快食用!\n")
                messageHelper.ConstructThreeDaysFood(three_days_food_list)
            
            if the_day_food_count > 0 or three_days_food_count > 0:
                line_bot_api.push_message(user['id'], TextSendMessage(text=messageHelper.GetMessage()))

#threading.Thread(target=push_message).start()

# Listen all requests from /callback
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# Main method for handling message
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    msg = event.message.text
    id = event.source.user_id
    messageHelper = MessageHelper()
    validationHelper = ValidationHelper(id, msg, messageHelper)
    command = validationHelper.Execute()

    if command:
        if command.GetAction() == Actions.HELP:
            messageHelper.Add(Messages.HELP)
        elif command.GetAction() == Actions.CODE:
            messageHelper.Add(Messages.CODE_INFO)
        elif command.GetAction() == Actions.ID:
            messageHelper.Add(id)
        elif command.GetAction() == Actions.HOWTO:
            messageHelper.Add(Messages.HOW_TO)
        elif command.GetAction() == Actions.LOCATION:
            messageHelper.Add(Messages.LOCATION)
        else:
            actionHelper = ActionHelper(command, messageHelper)
            actionHelper.Execute() 

    message = TextSendMessage(text=messageHelper.GetMessage())
    line_bot_api.reply_message(event.reply_token, message)
        
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
