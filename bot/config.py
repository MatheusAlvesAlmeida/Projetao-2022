import os
from dotenv import load_dotenv

load_dotenv()

telegram_token = os.getenv("TELEGRAM_TOKEN_DEV")

message_timeout = os.getenv("MESSAGE_TIMEOUT")

ubs_name = os.getenv("UBS_NAME")