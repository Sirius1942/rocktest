from bear.install_data import testRun
# coding=utf-8
import time
import unittest
from bear.base import Ski

class TestBearInstall(unittest.TestCase):
    def test_bearinstall(self):
        print("如果用例失败，代表BearFrame 框架没有正确安装，请用 {pip install BearFramework}命令安装")
        self.assertEqual(testRun(),"OK")