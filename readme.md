# ArcPy Logger #
ArcPyLogger is a python module that attaches the ArcPy messaging interface to the standard python logging module. 
This gives us the ability to concurrently write a single log message to the ArcGIS for Desktop/Server Console, 
a Log File, and to the Command Line Console. ArcPyLogger makes the development of Python projects more uniform by 
standardizing a single method for communicating back to the client.

## Install ##

Use pip to install this utility to your python site-packages.  This will allow you to use it throughout projects!

    pip install git+ssh://git@git.gisinc.com:7999/pyt/arcpylogger.git

## Initialize ##
    import logging
    import ArcPyLogger

    message = 'Example Message'
    warning = 'Example Warning'
    error = 'Example Error'

    log_file = r'example_log_file.txt'

### Use Helper Function ###

    ###
    # Use Helper function
    ###

    # Set logfile and log some sample message types
    ArcPyLogger.setupLogging()

    logging.info(message)
    logging.warning(warning)
    logging.error(error)
    
### Use Helper Function with Log File ###

    ###
    # Use Helper function
    ###

    # Set logfile and log some sample message types
    ArcPyLogger.setupLogging(log_file)

    logging.info(message)
    logging.warning(warning)
    logging.error(error)

### Use Python Class ###

    logging.basicConfig(level=level)
    # Check if there's already an ArcpyMessageHandler
    rootLogger = logging.getLogger()
    for h in rootLogger.handlers:
        if isinstance(h, ArcPyLogger.ArcpyMessageHandler):
            return

    rootLogger.addHandler(ArcPyLogger.ArcpyMessageHandler())
