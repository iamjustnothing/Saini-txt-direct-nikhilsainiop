#🇳‌🇮‌🇰‌🇭‌🇮‌🇱‌
# Add your details here and then deploy by clicking on HEROKU Deploy button
import os
from os import environ

API_ID = int(environ.get("API_ID", "27680167"))
API_HASH = environ.get("API_HASH", "90b8bad42e6210d0e1e04a858e045f55")
BOT_TOKEN = environ.get("BOT_TOKEN", "")
OWNER = int(environ.get("OWNER", "6775848126"))
CREDIT = "ᴊᴀᴄᴋ ꜱᴘᴀʀʀᴏᴡ"
AUTH_USER = os.environ.get('AUTH_USERS', '6775848126').split(',')
AUTH_USERS = [int(user_id) for user_id in AUTH_USER]
if int(OWNER) not in AUTH_USERS:
    AUTH_USERS.append(int(OWNER))
  
#WEBHOOK = True  # Don't change this
#PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
