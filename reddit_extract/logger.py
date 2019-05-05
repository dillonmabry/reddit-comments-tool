import logging


class Logger(object):
    """
    Class to setup and utilize basic logging
    Args:
        name: Name of class utilizing logger
    """

    def __init__(self, name):
        logging.basicConfig(
            filename=None,
            level=logging.INFO,
            format='[%(asctime)s] {%(pathname)s:%(lineno)d} %(levelname)s - %(message)s',
            datefmt='%H:%M:%S'
        )
        name = name.replace('.log', '')
        logger = logging.getLogger('log_namespace.%s' % name)
        self._logger = logger

    def get(self):
        """
        Method to return an instance of the logger
        """
        return self._logger
