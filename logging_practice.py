import logging


logging.basicConfig(level=logging.DEBUG)  # Will show all logs >= DEBUG (5 / 5)
logging.basicConfig(level=logging.DEBUG)  # Will show all logs >= CRITICAL (1 / 5)

logging.debug('This is the DEBUG level log')  # = 10
logging.info('This is the INFO level log')  # = 20
logging.warning('This is the WARNING level log')  # = 30
logging.error('This is the ERROR level log')  # = 40
logging.critical('This is the CRITICAL level log')  # = 50

