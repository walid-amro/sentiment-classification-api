# import logging
# from logging.handlers import RotatingFileHandler

# from app.core.config import config

# LOGGING_LEVEL = logging.INFO
# LOGGING_FORMAT = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"

# logging.basicConfig(level=LOGGING_LEVEL, format=LOGGING_FORMAT)

# file_handler = RotatingFileHandler(
#     config.LOG_FILE_PATH, maxBytes=config.LOG_FILE_MAX_BYTES, backupCount=5
# )
# file_handler.setLevel(LOGGING_LEVEL)
# file_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))

# logging.getLogger("").addHandler(file_handler)


