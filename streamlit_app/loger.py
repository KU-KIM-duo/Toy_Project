import logging

class mylog:
    def __init__ (self, log_file_path, level = logging.INFO):
        self.logger = logging.getLogger(__name__)
        self.logger.setLevel(level)
        #self.logger = logging.basicConfig(filename = log_file_path, level = level)
        
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s|%(filename)s:%(lineno)s] >> %(message)s')
        
        stream_handler = logging.StreamHandler()
        file_handler = logging.FileHandler(log_file_path)
        
        stream_handler.setFormatter(formatter)
        file_handler.setFormatter(formatter)
        
        stream_handler.setLevel(level)
        file_handler.setLevel(level)
        
        self.logger.addHandler(stream_handler)
        self.logger.addHandler(file_handler)
        
        
    def log(self,code,level=logging.INFO):
        if level == logging.DEBUG:
            self.logger.debug('activate %s', code)
        elif level == logging.INFO:
            self.logger.info('activate %s', code)
        elif level == logging.WARNING:
            self.logger.warning('activate %s', code)
        elif level == logging.ERROR:
            self.logger.error('activate %s', code)
        elif level == logging.CRITICAL:
            self.logger.critical('activate %s', code)