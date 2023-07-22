import os
from enum import Enum

from dotenv import load_dotenv

load_dotenv()

bot_token = os.getenv('BOT_TOKEN')
db_file = 'database.vdb'


class States(Enum):
    S_START = '0'
    S_CHOSE_AUDIO = '1'
