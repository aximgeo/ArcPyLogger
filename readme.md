# ArcPy Logger #
A python module for adding writing log messages to the ArcPy messaging interface.  Super useful for ArcGIS Server GP Services

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


#TODO: Document everything!