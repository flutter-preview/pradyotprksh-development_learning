from loguru import logger


logger.add("log_file.log", retention="1 days")


def print_new_line():
    """
    Print new lines
    :return: none
    """
    logger.debug('🥳\n')


def log_info(message):
    """
    Show an information on the console
    :param message: message which needs to be shown
    """
    logger.info(message)


def log_debug(message):
    """
    Show a debug message on the console
    :param message: message which needs to be shown
    :return: non
    """
    logger.debug(message)


def log_error(message):
    """
    Show an error message on the console
    :param message: message which needs to be shown
    :return: none
    """
    logger.error(message)


def log_exception(exception):
    """
    Shows the exception which occured
    :param exception: exception which occured
    :return: none
    """
    logger.exception(exception)
