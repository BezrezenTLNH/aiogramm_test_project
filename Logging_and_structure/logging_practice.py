import logging


# logging.basicConfig(level=logging.DEBUG)  # Will show all logs >= DEBUG (5 / 5)
# logging.basicConfig(level=logging.DEBUG)  # Will show all logs >= CRITICAL (1 / 5)
#
# logging.debug('This is the DEBUG level log')  # = 10
# logging.info('This is the INFO level log')  # = 20
# logging.warning('This is the WARNING level log')  # = 30
# logging.error('This is the ERROR level log')  # = 40
# logging.critical('This is the CRITICAL level log')  # = 50

# logger = logging.getLogger()
#
# print(logger)

# logger = logging.getLogger(__name__)
#
# print(logger)
# print(dir(logger))

# logger = logging.getLogger()
#
# print(logger.parent)
#
# logger = logging.getLogger(__name__)
#
# print(logger.parent)

# logger_1 = logging.getLogger('one.two')
#
# print(logger_1.parent)
#
# logger_2 = logging.getLogger('one.two.three')
#
# print(logger_2.parent)

# logger = logging.getLogger(__name__)
#
# logger.warning('Предупреждение!')
# logger.debug('Отладочная информация')



# Formatters

# https://docs.python.org/3/library/logging.html#formatter-objects


# %(asctime)s - time of log creation in a human-readable form. By default it looks like this - 2023-12-31 11:29:31,689
# %(filename)s - name of the module in which the log call was triggered
# %(funcName)s - name of the function in which the log call was triggered
# %(levelname)s - the level at which the log was called (DEBUG, INFO, etc.)
# %(lineno)d - number of the code line where the log was called
# %(name)s - name of the logger
# %(message)s - message to be output with the log

# By combining these formatting objects, you can flexibly customize how your logs will look. In this course we will use this view:
format='[%(asctime)s] #%(levelname)-8s %(filename)s: %(lineno)d - %(name)s - %(message)s'

# And logs formatted in this way will look like this:

# [2023-12-29 22:56:02,062] #INFO     dispatcher.py:172 - aiogram.event - Update id=563099722 is handled. Duration 272 ms by bot id=6341710373
# [2023-12-29 22:56:08,331] #DEBUG    intent_middleware.py:67 - aiogram_dialog.context.intent_middleware - Loading context for intent: `pCh8w8`, stack: ``, user: `173901673`, chat: `173901673`
# [2023-12-29 22:56:08,332] #DEBUG    dialog.py:121 - aiogram_dialog.dialog - Dialog render (Dialog 'FSMMainMenu')

# First comes the date and time of log creation in square brackets - [%(asctime)s],
# then the logging level #%(levelname)-8s, starting with the # symbol, is followed by a space.
# And exactly 8 characters are allocated for the logging level itself,
# and if the length of the string denoting the level is less than 8, spaces -8s are added to the right of it.
# After the log level comes the name of the module in which the log was triggered,
# and after the colon the line number in the code with the log call - %(filename)s:%(lineno)d.
# Then comes the name of the logger, which usually coincides with the full path to the module (starting from the entry point to the project)
# where the log was called - %(name)s. And at the very end, the log message itself - %(message)s.

format='[{asctime}] #{levelname:8} {filename}: {lineno} - {name} - {message}'

# The easiest way is to specify the formatting once at a basic logging configuration, such as at a project entry point:

# import logging
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='[%(asctime)s] #%(levelname)-8s %(filename)s:'
#            '%(lineno)d - %(name)s - %(message)s'
# )
#
# logger = logging.getLogger(__name__)
#
# logger.debug('Log of the DEBUG level')

# [2024-01-02 16:42:22,074] #DEBUG    test_5.py:11 - __main__ - Log of the DEBUG level

# import logging
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='[{asctime}] #{levelname:8} {filename}:'
#            '{lineno} - {name} - {message}',
#     style='{'
# )
#
# logger = logging.getLogger(__name__)
#
# logger.debug('Лог уровня DEBUG')

# import logging
#
# format_1 = '#%(levelname)-8s [%(asctime)s] - %(filename)s:'\
#            '%(lineno)d - %(name)s - %(message)s'
# format_2 = '[{asctime}] #{levelname:8} {filename}:'\
#            '{lineno} - {name} - {message}'
#
# formatter_1 = logging.Formatter(fmt=format_1)
# formatter_2 = logging.Formatter(
#     fmt=format_2,
#     style='{'
# )
