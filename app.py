from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import threading
from datetime import datetime
import time
import calendar
from Utils import Actions, Messages, Secret, Checker
from Helper.MessageHelper import MessageHelper
from Helper.ValidationHelper import ValidationHelper
from Helper.ActionHelper import ActionHelper
from Helper.DatabaseHelper import *
from Helper.DateHelper import *

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi(Secret.CHANNEL_ACCESS_TOKEN)
# Channel Secret
handler = WebhookHandler(Secret.CHANNEL_SECRET)

def push_message():
    while 1 == 1:
        # Execute every day
        time.sleep(86400)
        # Load registered user
        user_list = LoadUser()
        # For each user registered, will check their stored food and send them message if needed
        for user in user_list:
            messageHelper = MessageHelper()
            # Retrieve foods that expire on that day
            the_day_food_count, the_day_food_list = GetTheDayFood(user['id'])
            if the_day_food_count > 0:
                messageHelper.Add(Messages.ROBOT_HI + user['name'] + "，\n以下物品已於今日到期，請記得處理!")
                messageHelper.ConstructTheDayFood(user['id'], the_day_food_list)
                    
            # Retrieve foods that will expire in the following three days
            three_days_food_count, three_days_food_list = GetThreeDaysFood(user['id'])
            if three_days_food_count > 0:
                if the_day_food_count > 0: messageHelper.Add("\n")
                if the_day_food_count == 0 : messageHelper.Add(Messages.ROBOT_HI + user['name'] + "，\n")
                messageHelper.Add("以下物品將於三天之內過期，請盡快食用!")
                messageHelper.ConstructThreeDaysFood(three_days_food_list)
            
            day_today = GetToday().day
            last_day_date = calendar.monthrange(GetToday().year, GetToday().month)[1]
            # If it is the first day of that month, generate a monthly report
            the_month_food_count = 0
            if day_today == 1:
                the_month_food_count, the_month_food_list = GetTheMonthFood(user['id'])
                if the_month_food_count > 0:
                    if the_day_food_count > 0 or three_days_food_count > 0 : messageHelper.Add("\n")
                    if the_day_food_count == 0 and three_days_food_count == 0 : messageHelper.Add(Messages.ROBOT_HI + user['name'] + "，\n")
                    messageHelper.Add("以下物品將於這個月過期，請多多注意嚕～")
                    messageHelper.ConstructTheMonthFood(the_month_food_list)
            
            # If it is the last day of that month, generate a monthly review report
            the_month_food_left_count = 0
            if day_today == last_day_date:
                print("YETTTT")
            
            if the_day_food_count > 0 or three_days_food_count > 0 or the_month_food_count > 0:
                line_bot_api.push_message(user['id'], TextSendMessage(text=messageHelper.GetMessage()))

threading.Thread(target=push_message).start()

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
    message_from = event.source.type
    id = event.source.user_id
    messageHelper = MessageHelper()
    if message_from == "group":
        if Checker.GroupActionCheck(msg):
            validationHelper = ValidationHelper(id, msg, messageHelper)
            command = validationHelper.Execute()
            if command:
                if command.GetAction() == Actions.HELP:
                    messageHelper.Add(Messages.HELP_GROUP)
                elif command.GetAction() == Actions.HOWTO:
                    messageHelper.Add(Messages.HOW_TO_GROUP)
                elif command.GetAction() == Actions.LOCATION:
                    messageHelper.Add(Messages.LOCATION)
                else:
                    actionHelper = ActionHelper(command, messageHelper)
                    actionHelper.Execute()
                    
            message = TextSendMessage(text=messageHelper.GetMessage())
            line_bot_api.reply_message(event.reply_token, message)
            
    elif message_from == "user":
        validationHelper = ValidationHelper(id, msg, messageHelper)
        command = validationHelper.Execute()
        if command:
            if command.GetAction() == Actions.HELP:
                messageHelper.Add(Messages.HELP_USER)
            elif command.GetAction() == Actions.CODE:
                messageHelper.Add(Messages.CODE_INFO)
            elif command.GetAction() == Actions.ID:
                messageHelper.Add(id)
            elif command.GetAction() == Actions.HOWTO:
                messageHelper.Add(Messages.HOW_TO_USER)
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
