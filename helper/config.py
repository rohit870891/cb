
from . import *

try:
    APP_ID = config("APP_ID", default=21624420, cast=int)
    API_HASH = config("API_HASH", default="eb06d4abfb49dc3eeb1aeb98ae0f581e")
    BOT_TOKEN = config("BOT_TOKEN", default="8065030679:AAE-Vvvejh6maceHLBamYQPOYIyC-sMUM2w")
    OWNER = config("OWNER_ID", default=7328629001, cast=int)
    LOG = config("LOG_CHANNEL", default=-1002200709110, cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
