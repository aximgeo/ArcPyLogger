__doc__ = """
Title: ArcPy Logging Helper
Description: A helper function to setup the ArcPy logging on the logging root.
Usage:
"""

__author__ = 'Christopher Fricke (cfricke@gisinc.com) and Charles Arnold (carnold@gisinc.com)'
__version__ = '0.9.0'
__status__ = 'Development'
__copyright__ = 'Copyright 2015, GISi'
__license__ = 'MIT'


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
        root_logger = logging.getLogger()
        for h in root_logger.handlers:
            if isinstance(h, ArcpyMessageHandler):
                return

        root_logger.addHandler(ArcpyMessageHandler())

    except IOError:
        raise IOError('Unable to write log file to {0}'.format(log_file))