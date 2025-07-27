import logging.config

# logging.config.fileConfig('logging.ini')
logging.config.dictConfig({
  'version': 1,  # 'veretion' → 'version' に修正
  'formatters': {
    'sampleFormatter': {
      'format': '%(asctime)s %(name)-12s %(levelname)-8s %(message)s'
    }
  },
  'handlers': {
    'sampleHandlers': {  # 'sampleeHandlers' → 'sampleHandlers' に修正
      'class': 'logging.StreamHandler',
      'formatter': 'sampleFormatter',
      'level': logging.DEBUG
    }
  },
  'root': {
    'handlers': ['sampleHandlers'],
    'level': logging.WARNING,
  },
  'loggers': {
    'simpleExample': {
      'handlers': ['sampleHandlers'],
      'level': logging.DEBUG,
      'propagate': 0
    }
  }
})

logger = logging.getLogger('simpleExample')

logger.debug('debug message')
logger.info('info message')
logger.warning('warn message')
logger.error('error message')
logger.critical('critical message')
