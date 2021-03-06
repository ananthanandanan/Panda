#!/usr/bin/env python
import logging
import os
import logging.handlers
LOG_FILE_ONE = "/var/log/nawab"



class Nawab_Logging(object):
    
    def __init__(self, dirpath, level):
       self.setup_logger('log_result',"results.log", level)
       self.setup_logger('log_error', "error.log", level)
        
    
     ##setting up the logger
    def setup_logger(self, logger_name, log_file, level):
        log_setup = logging.getLogger(logger_name)
        formatter = logging.Formatter(fmt=
            '%(asctime)s %(msecs)d,%(lineno)d %(levelname)-4s %(message)s', datefmt='%Y-%m-%d %I:%M:%S %p')
        fileHandler = logging.FileHandler(log_file, mode='a')
        fileHandler.setFormatter(formatter)
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(formatter)
        log_setup.setLevel(level)
        log_setup.addHandler(fileHandler)
        log_setup.addHandler(streamHandler)
        
        pass
    
    def logger(self, msg, level, logfile):

        if logfile == 'results':
            log = logging.getLogger('log_result')
        if logfile == 'error':
            log = logging.getLogger('log_error')
        if level == 'info':
            log.info(msg)
        if level == 'warning':
            log.warning(msg)
        if level == 'error':
            log.error(msg)
        if level == 'debug':
            log.debug(msg)
        pass
  
def main():
    default_path = "/var/log/nawab/"
    level = 20
    Logger = Nawab_Logging(default_path,level)  
    Logger.logger('Hello', 'info', 'results')
    
if __name__ == "__main__":

    main()