#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file  : xlogs.py
@Time  : 2020/12/7 15:40
@Author: Tao.Xu
@Email : tao.xu2008@outlook.com
"""

import functools
import logging
import os
import logging.config
import configparser
import threading
import sys


class Log(object):
    """Logging toolkit"""
    _lock = threading.Lock()  # 实现线程锁，增加安全性

    def __init__(self, log_file=None, config_file=None):
        """初始化日志保存文件和日志配置文件
        :param log_file: 日志保存文件
        :param config_file: 日志配置文件
        """
        self.config_file = config_file or os.path.dirname(__file__) + os.sep + 'config.ini'
        self.log_file = log_file if log_file else './logs'
        if not hasattr(Log, "_init"):  # 增加初始化屬性
            with Log._lock:  # 加锁防止多线程环境中两个线程同时实例化
                if not hasattr(Log, "_init"):
                    self.log_config()
                    Log._init = True

    def log_config(self) -> configparser:
        """加载当前文件下的log.ini文件
        默认日志文件夹在当前运训目录的logs下\n
        如果要自定义文件夹，只需要将custom_dir定义该目录即可，修改目录下的日志文件夹只需要定义handlers即可，程序会自动寻找handlers下的args的值。\n
        将匹配信息直接写入内存中
        [handlers]\n
        keys = consoleHandler,fileHandler,errorHandler
        self.config_file: 日志配置文件\n
        self.log_file: 自定义日志保存文件夹\n
        :return: 日志文件配置对象
        """
        cfg = configparser.RawConfigParser()
        cfg.read(self.config_file)
        if not os.path.exists(self.log_file):
            os.mkdir(self.log_file)
        handle = cfg.items('handlers')
        for _, v in handle:
            for vs in v.split(','):
                for key, value in cfg.items('handler_' + vs):
                    if key == 'args':
                        e = eval(value)
                        if isinstance(e[0], str):
                            es = self.log_file + os.sep + os.path.basename(e[0])
                            value = str((es, *e[1:]))
                            cfg.set('handler_' + vs, 'args', value)
        logging.config.fileConfig(cfg)
        return cfg

    def log_reset(self):
        self.log_config()

    def __new__(cls, *args, **kwargs):
        """实现单例模式"""
        if not hasattr(Log, "_instance"):
            with Log._lock:  # 加锁防止多线程环境中两个线程同时实例化
                if not hasattr(Log, "_instance"):
                    Log._instance = super(Log, cls).__new__(cls)
        return Log._instance


def log(log_file, config_file=None):
    """日志装饰器，用于测试函数的时候打印日志
    关于日志配置：可以参考官网配置： https://docs.python.org/3.7/library/logging.config.html
    Usage:
    from pyunit_log import log
    if __name__ == '__main__':
        @log(log_file='./logs',config_file=None)
        def division():
            pass
    :param log_file: 日志地址保存地方
    :param config_file: 日志配置地址保存地址
    """

    def inner(fun):
        Log(log_file=log_file, config_file=config_file)

        @functools.wraps(fun)
        def wraps(*args, **kwargs):
            try:
                logging.getLogger('info').info(f'Running：{fun.__name__}')
                f = fun(*args, **kwargs)
                logging.getLogger('info').info(f'Complete：{fun.__name__}')
                return f
            except Exception as e:
                logging.getLogger('info').error(f'Run：{fun.__name__}, Exception:{str(e)}')
                with open(log_file + os.sep + 'error.log', 'a', newline='\n')as f:
                    f.write('+' * 70 + os.linesep)
                logging.getLogger('error').exception(e)
                with open(log_file + os.sep + 'error.log', 'a', newline='\n')as f:
                    f.write('#' * 70 + os.linesep + os.linesep)
                raise e

        return wraps

    return inner


if __name__ == '__main__':
    pass
