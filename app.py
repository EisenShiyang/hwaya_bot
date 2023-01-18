from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import tempfile
import datetime
import time
from Utils import Actions, Messages

app = Flask(__name__)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')
# Channel Access Token
line_bot_api = LineBotApi('2ntK2P9daJrdC8r0dyZ6AVe5jDfGIdf27wOWkn1pZ/VZEMOOjKhthuh3+7nya1ikWpLY3L2qVgagiKnplJPV8RncoLFgkvECh4yaMVhLL84zYo+Jl4rZfpzzPJKYaX3uhgEKdjxBlENDcpgGA+HPagdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('a7142968d06edae024e33e9f592d5413')

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
    
    if msg == Actions.HELP:
        msg = Messages.HELP
    elif msg == Actions.CODE:
        msg = Messages.CODE_INFO
    elif msg in Actions.FOOD:
        msg = "想存東西R人類"
    else:
        msg = Messages.COMMAND_NOT_FOUND

    message = TextSendMessage(text=msg)
    line_bot_api.reply_message(event.reply_token, message)
        
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
