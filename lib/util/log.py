#coding:utf-8
from logging import getLogger,StreamHandler,DEBUG

"""Wraper of logger
"""
class Log(object):
    def __new__(cls, *args, **kwargs):
        if hasattr(cls, "__instance__"):
			return cls.__instance__
        cls.__instance__ = super(Log, cls).__new__(cls, *args, **kwargs)
		#logger configuration	
        cls.__logger = getLogger(__name__)
        handler = StreamHandler()
        handler.setLevel(DEBUG)
        cls.__logger.setLevel(DEBUG)
        cls.__logger.addHandler(handler)

    def critical(self, message):
        self._logger.critical(message)

    def error(self, message):
        self._logger.error(message)

    def warning(self, message):
        self._logger.warning(message)

    def info(self, message):
        self._logger.info(message)

    def debug(self, message):
        self._logger.debug(message)

if __name__ == '__main__':
    Log().info("00000000000")
