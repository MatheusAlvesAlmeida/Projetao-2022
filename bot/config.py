import os
import pyrebase
from dotenv import load_dotenv

load_dotenv()

is_production = os.getenv("IS_PRODUCTION", "True") == "True"

telegram_token = os.getenv("TELEGRAM_TOKEN")

telegram_token_dev = os.getenv("TELEGRAM_TOKEN_DEV")

telegram_token_dev = os.getenv("TELEGRAM_TOKEN_DEV")

message_timeout = os.getenv("MESSAGE_TIMEOUT", 120)

ubs_name = os.getenv("UBS_NAME")

def get_telegram_token():
    """
    returns the correct token prod or dev token
    """
    if is_production:
        print("Bot starting in production.")
        return telegram_token
    print("Bot starting in development.")
    return telegram_token_dev

pyrebase_api = os.getenv("PYREBASE_API_KEY")

auth_domain = os.getenv("AUTH_DOMAIN")

database_url = os.getenv("DATABASE_URL")

storage_bucket = os.getenv("STORAGE_BUCKET")

pyrebase_config = {
  "apiKey": pyrebase_api,
  "authDomain": auth_domain,
  "databaseURL": database_url,
  "storageBucket": storage_bucket
}

firebase = pyrebase.initialize_app(pyrebase_config)

# Temporarily replace quote function
def noquote(s):
    return s

pyrebase.pyrebase.quote = noquote