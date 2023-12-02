import unittest
import os
from src.number_theory import GcfClass
from src.number_theory import LcmClass
from src.number_theory import PfClass
from src.number_theory import LoginClass
from src.number_theory import AccountCreation

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

class TestAccountCreation(unittest.TestCase):
    def setUp(self):
        self.goodAccount = AccountCreation("accountTest","pass1","pass1")
        self.badAccountNoMatch = AccountCreation("accountTest","pass","pass1")
        self.badAccountNoNum = AccountCreation("accountTest","pass","pass")
        self.badAccountNoAlph = AccountCreation("accountTest","1","1")

    def test_good_account(self):
        self.assertEqual(self.goodAccount.account_check(), (True,False,False,False,False))

    def test_no_match(self):
        self.assertEqual(self.badAccountNoMatch.account_check(), (False,False,True,False,False))

    def test_no_num(self):
        self.assertEqual(self.badAccountNoNum.account_check(), (False,False,False,True,False))

    def test_no_letter(self):
        self.assertEqual(self.badAccountNoAlph.account_check(), (False,False,False,False,True))

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.calc1 = GcfClass(12,18)
        self.calc2 = LcmClass(32,13)
        self.calc3 = PfClass(9243)

    def test_gcf(self):
        class_return = list(self.calc1.gcf().split(" "))
        gcf_value = class_return[len(class_return)-1]
        self.assertEqual(gcf_value, "6")

    def test_lcm(self):
        class2_return = list(self.calc2.lcm().split(" "))
        lcm_value = class2_return[len(class2_return)-1]
        self.assertEqual(lcm_value, "416")

    def test_pf(self):
        self.assertEqual(self.calc3.pf(), [3, 3, 13, 79])
