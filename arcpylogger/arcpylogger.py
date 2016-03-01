__doc__ = """
Title: ArcPy Logger
Description: Classes to define ArcPy message stream handlers!
Usage:
"""

import logging
import logging.handlers

import arcpy


class ArcpyMessageStream(object):
    """
    A class that looks like a stream (i.e., has a 'write' method and an 'encoding' property)
    for use with the logging.StreamHandler class.
    Anything passed to 'write' is forward to arcpy.Add[Message|Warning|Error], based on the
    last call to setWriteLevel (default is ArcpyMessageStream.MESSAGE)
    """

    MESSAGE = 0
    WARNING = 1
    ERROR = 2

    def __init__(self, encoding):
        """

        :param encoding:
        :return:
        """
        self.encoding = encoding
        self.setWriteLevel(ArcpyMessageStream.MESSAGE)

    def setWriteLevel(self, level):
        """
        Set what arcpy.*Message function should be called on ArcpyMessageStream.write

        :param level: ArcpyMessageStream.MESSAGE, ArcpyMessageStream.WARNING or ArcpyMessageStream.ERROR
        """

        if level == ArcpyMessageStream.MESSAGE:
            self.write = lambda m: arcpy.AddMessage(m.strip())
        elif level == ArcpyMessageStream.WARNING:
            self.write = lambda m: arcpy.AddWarning(m.strip())
        elif level == ArcpyMessageStream.ERROR:
            self.write = lambda m: arcpy.AddError(m.strip())
        else:
            raise ValueError('Invalid "level" argument ({0})'.format(level))


class ArcpyMessageHandler(logging.StreamHandler):
    
    def __init__(self, encoding=None):
        """
        :param encoding:
        :return:
        """
        super(ArcpyMessageHandler, self).__init__(ArcpyMessageStream(encoding))

    def emit(self, record):
        """
        set the write level on the ArcpyMessageStream before emitting the message ..
        :param record:
        :return:
        """
        if record.levelno >= logging.ERROR:
            self.stream.setWriteLevel(ArcpyMessageStream.ERROR)
        elif record.levelno >= logging.WARNING:
            self.stream.setWriteLevel(ArcpyMessageStream.WARNING)
        else:
            self.stream.setWriteLevel(ArcpyMessageStream.MESSAGE)

        super(ArcpyMessageHandler, self).emit(record)
