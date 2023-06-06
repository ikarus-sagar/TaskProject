import logging
import logging.handlers
import os

log_filename = '/var/log/my_app.log'

# Create a file handler that will write to log_filename and rotate the log file
# when it reaches 10 MB. It will keep up to 5 old log files.
handler = logging.handlers.RotatingFileHandler(
    log_filename, maxBytes=10*1024*1024, backupCount=5)

# Set the log level and format for the handler.
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
handler.setFormatter(formatter)

# Get the root logger and add the handler to it.
logger = logging.getLogger('my_app')
logger.setLevel(logging.INFO)
logger.addHandler(handler)

# Set file permissions to rw-------.
os.chmod(log_filename, 0o600)
