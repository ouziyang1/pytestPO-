import os
import sys
import time
from functools import wraps
from loguru import logger
from time import strftime


class LogManager:


    def __init__(self):
        self.logger=logger
        logger.remove()
        filename = strftime("%Y%m%d-%H%M%S")
        log_file_path = os.path.join('../logs',filename)
        log_format = '<green>{time:YYYY-MM-DD HH:mm:ss.SSS}</green> {level} {message}'
        level = 'DEBUG'
        rotation = '5MB'

        self.logger.add(log_file_path,
                        enqueue=True,
                        backtrace=True,
                        diagnose=True,
                        encoding='utf-8',
                        rotation=rotation)

        self.logger.add(sys.stderr,
                        format=log_format,
                        backtrace=True,
                        diagnose=True,
                        level=level,
                        colorize=True,)

    def runtime_logger(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            self.logger.info(f"{func.__name__} 当前开始执行")
            now1 = time.time()
            try:
                func(*args, **kwargs)
            except Exception as e:
                self.logger.error(f"当前用例执行失败，失败的原因是{e}")
            now2 = time.time()
            self.logger.success(f"{func.__name__} 执行成功，耗时: {now2 - now1}ms")
            return func

        return wrapper

    def runtime_logger_class(self, cls):
        for attr_name in dir(cls):
            if attr_name.startswith('test_') and callable(getattr(cls, attr_name)):
                setattr(cls, attr_name, self.runtime_logger(getattr(cls, attr_name)))
        return cls
my_log = LogManager()