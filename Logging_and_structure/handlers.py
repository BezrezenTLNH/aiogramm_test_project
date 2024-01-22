# logger = logging.getLogger(__name__)
#
# stderr_handler = logging.StreamHandler()
# stdout_handler = logging.StreamHandler(sys.stdout)
#
# logger.addHandler(stdout_handler)
# logger.addHandler(stderr_handler)
#
# print(logger.handlers)
#
# logger.warning('Это лог с предупреждением!')

import logging

#
# # Define the first type of formatting
# format_1 = '#%(levelname)-8s [%(asctime)s] - %(filename)s:' \
#            '%(lineno)d - %(name)s - %(message)s'
#
# # Define the second type of formatting
# format_2 = '[{asctime}] #{levelname:8} {filename}:' \
#            '{lineno} - {name} - {message}'
#
# # Initialize the first formatter
# formatter_1 = logging.Formatter(fmt=format_1)
#
# # Initialize the second formatter
# formatter_2 = logging.Formatter(
#     fmt=format_2,
#     style='{'
# )
#
# # Create a logger
# logger = logging.getLogger(__name__)
#
# # Initialize a handler that will redirect logs to stderr
# stderr_handler = logging.StreamHandler()
#
# # Initialize the handler that will redirect logs to stdout
# stdout_handler = logging.StreamHandler(sys.stdout)
#
# # Set the formatters for the handlers
# stderr_handler.setFormatter(formatter_1)
# stdout_handler.setFormatter(formatter_2)
#
# # Add handlers to the logger
# logger.addHandler(stdout_handler)
# logger.addHandler(stderr_handler)
#
# # Create a log
# logger.warning('This is a warning log!')


logger = logging.getLogger(__name__)

file_handler = logging.FileHandler('logs.log')

logger.addHandler(file_handler)

print(logger.handlers)

logger.warning('This is a warning log!')
# By executing this code, we get the result in the console:
#
# [<FileHandler /<here_full_path_to_file_with_logs>/logs.log (NOTSET)>].
# And in the logs.txt file:
# This is the warning log!

# By default, logs will be written to the file by appending each new entry with a new line,
# but this behavior can be controlled.
# For example, you can overwrite the log file every time you run the code. To do this,
# pass the argument mode='w' to the FileHandler class
# (by default mode='a', from "append" - add, so we didn't specify it explicitly)
