import unittest
from src.numberTheory import gcfClass
from src.numberTheory import lcmClass
from src.numberTheory import loginClass

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.goodInfo = loginClass("user1","abc1")

    def test_correct_login(self):
        self.assertEqual(self.goodInfo.loginCheck(), True)

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.calc1 = gcfClass(12,18)
        self.calc2 = lcmClass(32,13)

    def test_gcf(self):
        class_return = list(self.calc1.gcf().split(" "))
        gcf_value = class_return[len(class_return)-1]
        self.assertEqual(gcf_value, "6")

    def test_lcm(self):
        class2_return = list(self.calc2.lcm().split(" "))
        lcm_value = class2_return[len(class2_return)-1]
        self.assertEqual(lcm_value, "416")