#!/user/bin/even python
# -*- coding:utf-8 -*-

import os
import time
import logging
import inspect
from logging.handlers import RotatingFileHandler

dir = "../logout"
# print(os.listdir(dir) )
# dir = os.path.dirname(__file__)+"/config/logger/"
# dir = os.path.dirname(os.getcwd()) + "/config/logger/"
dir_time = time.strftime('%Y%m%d', time.localtime())

handlers = {
    # logging.NOTSET: os.path.join(dir, 'notset_%s.log' % dir_time),

    # logging.DEBUG: os.path.join(dir, 'debug_%s.log' % dir_time),

    logging.INFO: os.path.join(dir, 'info_%s.log' % dir_time),

    logging.WARNING: os.path.join(dir, 'warning_%s.log' % dir_time),

    logging.ERROR: os.path.join(dir, 'error_%s.log' % dir_time),

    # logging.CRITICAL: os.path.join(dir, 'critical_%s.log' % dir_time),
}


def createHandlers():
    logLevels = handlers.keys()
    for level in logLevels:
        path = os.path.abspath(handlers[level])
        handlers[level] = RotatingFileHandler(path, maxBytes=100000, mode='a', encoding='utf-8')


# 加载模块时创建全局变量
createHandlers()


class SpiderLog(object):

    def printfNow(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def __init__(self, level=logging.NOTSET):
        self.__loggers = {}

        self.logLevels = handlers.keys()

        for level in self.logLevels:
            logg = logging.getLogger(str(level))

            # 如果不指定level，获得的handler似乎是同一个handler?

            logg.addHandler(handlers[level])

            logg.setLevel(level)

            self.__loggers.update({level: logg})

    def getLogMessage(self, level, message):
        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[2]

        '''日志格式：[时间] [类型] [记录代码] 信息'''

        return "[%s] [%s] [%s - %s - %s] %s" % (self.printfNow(), level, filename, lineNo, functionName, message)

    def info(self, message):
        message = self.getLogMessage("info", message)

        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        message = self.getLogMessage("error", message)

        self.__loggers[logging.ERROR].error(message)

    def warning(self, message):
        message = self.getLogMessage("warning", message)

        self.__loggers[logging.WARNING].warning(message)

    def debug(self, message):
        message = self.getLogMessage("debug", message)

        self.__loggers[logging.DEBUG].debug(message)

    def critical(self, message):
        message = self.getLogMessage("critical", message)

        self.__loggers[logging.CRITICAL].critical(message)