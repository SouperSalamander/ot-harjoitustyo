import unittest
from src.numberTheory import GcfClass
from src.numberTheory import LcmClass
from src.numberTheory import LoginClass

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.goodInfo = LoginClass("salamander","a123")
        self.badInfo = LoginClass("wrong","bad")

    def test_correct_login(self):
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
