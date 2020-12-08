#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
@file  : test.py
@Time  : 2020/12/7 15:49
@Author: Tao.Xu
@Email : tao.xu2008@outlook.com
"""

import time
import logging
import unittest

from xlogs import Log, log


class XLogTC(unittest.TestCase):
    """xlogs test case"""
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    @unittest.skip("skip")
    def test_log_1(self):
        @log(log_file='./')
        def func():
            time.sleep(2)
            return 5
        self.assertTrue(func() == 5)

    @unittest.skip("skip")
    def test_log_2(self):
        Log("./log2")
        logger = logging.getLogger()
        logger.info("info oooooo")
        logger.debug("debug ggggg")
        logger.error("err rrrr")
        self.assertTrue(1)

    def test_log_3(self):
        Log("./log3_1/")
        logger1 = logging.getLogger()
        logger1.info("logger1 info oooooo")
        logger1.debug("logger1 debug ggggg")
        logger1.error("logger1 err rrrr")

        Log("./log3_2/").log_reset()
        logger2 = logging.getLogger()
        logger2.info("logger2 info oooooo")
        logger2.debug("logger2 debug ggggg")
        logger2.error("logger2 err rrrr")
        self.assertTrue(1)


if __name__ == '__main__':
    # test
    # unittest.main()
    suite = unittest.TestLoader().loadTestsFromTestCase(XLogTC)
    unittest.TextTestRunner(verbosity=2).run(suite)
