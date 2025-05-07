
from . import *

try:
    APP_ID = config("APP_ID", default=20718334, cast=int)
    API_HASH = config("API_HASH", default="4e81464b29d79c58d0ad8a0c55ece4a5")
    BOT_TOKEN = config("BOT_TOKEN", default="8065030679:AAE-Vvvejh6maceHLBamYQPOYIyC-sMUM2w")
    OWNER = config("OWNER_ID", default=7328629001, cast=int)
    LOG = config("LOG_CHANNEL", default=-1002200709110, cast=int)
except Exception as e:
    LOGS.info("Environment vars Missing")
    LOGS.info("something went wrong")
    LOGS.info(str(e))
    exit(1)
