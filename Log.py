import logging

def setup_logger():
    logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

def log_debug(message):
    logging.debug(message)

def log_info(message):
    logging.info(message)

def log_warning(message):
    logging.warning(message)

def log_error(message, log_condition=True):
    if log_condition:
        logging.error(message)

def log_critical(message):
    logging.critical(message)
