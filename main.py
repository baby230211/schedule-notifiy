from linebot import LineBotApi
from linebot.models import TextSendMessage
from linebot.exceptions import LineBotApiError
from dotenv import load_dotenv

load_dotenv()
import os

CHANNEL_TOKEN = os.getenv("CHANNEL_TOKEN")
GROUP_ID = os.getenv("GROUP_ID")

line_bot_api = LineBotApi(CHANNEL_TOKEN)

try:
    line_bot_api.push_message(GROUP_ID, TextSendMessage(text="Hello World!"))
except LineBotApiError as e:
    # error handle
    print(e)
