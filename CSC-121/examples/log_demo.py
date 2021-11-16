# Filename: log_demo.py
# Author: Michael Souther
# Date: 10/07/2019
# Purpose: To Demo Logging
import logging

# Log Format

LOG_ENTRY="%(levelname)s %(asctime)s %(message)s"

# Note: That logging is set to debug. Normally it would be set to a warning or error. 
logging.basicConfig(filename="example.log",
                    format=LOG_ENTRY,
                    filemode='w',
                    level=logging.DEBUG)

logger=logging.getLogger()

logger.info("Test Message")
logger.debug("Test Debug")
logger.warning("Test Warning")
logger.error("Test Error")
logger.critical("Test Critical")

