import unittest
import os
from src.number_theory import GcfClass
from src.number_theory import LcmClass
from src.number_theory import LoginClass

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.goodInfo = LoginClass("fake","account")
        self.badInfo = LoginClass("wrong","bad")

    def test_correct_login(self):
        if os.path.isfile('userAccounts.txt') is False:
            with open('userAccounts.txt','a', encoding = "utf-8") as file:
                file.close()
        with open('userAccounts.txt', 'a', encoding = "utf-8") as file_object:
            file_object.write('0' + ',' + 'fake' + \
            ',' + 'account' + '\n')
            file_object.close()
        self.assertEqual(self.goodInfo.login_check(), True)

    def test_wrong_login(self):
        self.assertEqual(self.badInfo.login_check(), False)

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.calc1 = GcfClass(12,18)
        self.calc2 = LcmClass(32,13)

    def test_gcf(self):
        class_return = list(self.calc1.gcf().split(" "))
        gcf_value = class_return[len(class_return)-1]
        self.assertEqual(gcf_value, "6")

    def test_lcm(self):
        class2_return = list(self.calc2.lcm().split(" "))
        lcm_value = class2_return[len(class2_return)-1]
        self.assertEqual(lcm_value, "416")
