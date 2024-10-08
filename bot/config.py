from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 6))
    API_HASH = env.get("TELEGRAM_API_HASH", "eb06d4abfb49dc3eeb1aeb98ae0f581e")
    OWNER_ID = int(env.get("OWNER_ID", 1881785806))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "1881785806 6645701618").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "Archive_DDL")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "7303581647:AAEAQpnBcen_-TGccFVPMioMPR7PuZ4xptk")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1001743701534))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://ddl.infinityfiles.eu.org")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 80))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
