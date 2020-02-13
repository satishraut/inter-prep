'''
Logging means tracing the events. When some software runs

Level ====== Numeric Value

NOTSET =====> 0
DEBUG  =====> 10
INFO   =====> 20
WARNING =====> 30
ERROR  ======> 40
CRITICAL =====> 50

'''

import logging

#Create and configure logger
logging.basicConfig(filename='newfile.log', format='%(asctime)s %(message)s', filemode='w')

#Creating an object
logger = logging.getLogger()

#Setting the threshold of logger to DEBUG
logger.setLevel(logging.WARNING)

#Test messages

logger.debug('Harmless debug message')
logger.info('INFO message')
logger.warning('WARNING message')
logger.error('ERROR messages')
logger.critical('CRITICAL messages')
