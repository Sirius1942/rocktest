# coding=utf-8
import time
import unittest
from bear.base import Ski
from keywords.businessKW.bsend import login

class TestUserLogin(unittest.TestCase,Ski):

    def setUp(self):
        # 非测试步骤的时候直接调用 “业务”  关键字  【规范】 业务关键字可以直接调用，通用关键字（driver）层 尽量不要直接调用。
        # 考虑是否要设置一个关键字做隔离？留给使用者
        # 如果想隔离方法可以直接使用 self.step
        # self.step("login",{"username": "admin","password": "admin"})
        login({"username": "admin","password": "admin"}) 
    def tearDown(self):
        pass

    @Ski.case()
    def test_login(self):
        res=self.step("login",{"username": "admin","password": "admin"})
        self.assertEqual(200,res.result.status_code)

    @Ski.case()
    def test_getuserlist(self):
        res=self.step("getUserInfo",{'name':'admin'})
        self.assertEqual(200,res.result.status_code)
    
    @Ski.case()
    def test_robotframwork_selenium(self):
        print("I'm in test_two test_send")
        self.step("Open Browser","http://www.agavetest.info/rockprod/","chrome")
        self.step("input text","name=username","admin")
        self.step("input text","name=password","admin")
        self.step("set browser implicit wait","5")
        self.step("click button","id=login_button")
        self.step("close browser")
        
    

