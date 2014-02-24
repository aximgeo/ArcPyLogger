"""
Title: ArcPy Logging Helper
Description: A helper function to setup the ArcPy logging on the logging root.
Usage:
"""

__author__ = 'cfricke'
__version__ = '0.9'
__maintainer__ = 'cfricke'
__status__ = 'Development'


import logging

from arcpylogger import ArcpyMessageHandler


def setupLogging(log_file=None, level=logging.DEBUG):
    """ Add an ArcpyMessageHandler to the root logger
        :param log_file: Log file location to write messages.  If none, then don't write to log file
        :type log_file: str
        :param level: logging level, can be logging.INFO, logging.DEBUG, logging.WARNING, logging.ERROR)
        :type level: logging level
    """
    try:
        if log_file:
            logging.basicConfig(filename=log_file,
                                filemode='w',
                                format='%(asctime)s %(levelname)-8s %(message)s',
                                datefmt='%a, %d %b %Y %H:%M:%S',
                                level=level)
        else:
            logging.basicConfig(level=level)

        # Check if there's already an ArcpyMessageHandler
        rootLogger = logging.getLogger()
        for h in rootLogger.handlers:
            if isinstance(h, ArcpyMessageHandler):
                return

        rootLogger.addHandler(ArcpyMessageHandler())

    except IOError:
        raise IOError('Unable to write log file to {0}'.format(log_file))