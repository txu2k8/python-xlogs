#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file  : __init__.py.py
@Time  : 2020/12/7 15:34
@Author: Tao.Xu
@Email : tao.xu2008@outlook.com
"""

from .xlog import LogConfig, log
from .xlog2 import *
"""
Default(config.ini):
Save 30 days
info logs rotating every 1MB
error logs rotating every day
"""

__version__ = '2020.12.07'
__author__ = 'Tao.Xu'
__description__ = 'logging toolkit'
__email__ = 'tao.xu2008@outlook.com'
__names__ = 'xlogs'
__url__ = 'https://github.com/txu2k8/python-xlogs'


if __name__ == '__main__':
    pass
