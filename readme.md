# ArcPy Logger #
ArcPyLogger is a python module that attaches the ArcPy messaging interface to the standard python logging module. 

By default ArcPy does not follow the Python standard for writing messages to the logging interface. This module extends
the existing python logging interface with the ability to write messages to the ArcGIS Desktop or ArcGIS Server
console. In addition, a helper function is included to write messages concurrently to a File and ArcGIS Consoles.

ArcPyLogger will make the development of ArcPy Python projects more standards compliant by standardizing on 
a single method for communicating back to the client.

## Install ##

Use pip to install this utility to your python site-packages.  This will allow you to use it throughout projects!

    pip install git+ssh://git@git.gisinc.com:7999/pyt/arcpylogger.git
    
If you do not have Pip, you can install this package using the standard python packaging system.

    git clone git+ssh://git@git.gisinc.com:7999/pyt/arcpylogger.git
    cd arcpylogger
    python setup.py install

## Usage ##

### Initialize ##
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
