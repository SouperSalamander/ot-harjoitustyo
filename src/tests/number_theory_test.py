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

        with open('userAccounts.txt', 'r', encoding = "utf-8") as lns:
            lines = lns.readlines()

        with open('userAccounts.txt', 'w', encoding = "utf-8") as lns:
            for line in lines:
                line = line.rstrip()
                full_line = line.split(",")
                if full_line[0] != "0":
                    lns.write(line)

    def test_wrong_login(self):
        self.assertEqual(self.badInfo.login_check(), False)

class TestAccountCreation(unittest.TestCase):
    def setUp(self):
        self.goodAccount = AccountCreation("accountTest","pass1","pass1")
        self.badAccountNoMatch = AccountCreation("accountTest","pass","pass1")
        self.badAccountNoNum = AccountCreation("accountTest","pass","pass")
        self.badAccountNoAlph = AccountCreation("accountTest","1","1")
        self.badAccountExists = AccountCreation("accountTest","pass1","pass1")

    def test_good_account(self):
        self.assertEqual(self.goodAccount.account_check(), 0)

    def test_no_match(self):
        self.assertEqual(self.badAccountNoMatch.account_check(), 1)

    def test_no_num(self):
        self.assertEqual(self.badAccountNoNum.account_check(), 2)

    def test_no_letter(self):
        self.assertEqual(self.badAccountNoAlph.account_check(), 3)

    def test_account_exists(self):
        if os.path.isfile('userAccounts.txt') is False:
            with open('userAccounts.txt','a', encoding = "utf-8") as file:
                file.close()
        with open('userAccounts.txt', 'a', encoding = "utf-8") as file_object:
            file_object.write('0' + ',' + 'accountTest' + \
            ',' + 'pass1' + '\n')
            file_object.close()

        self.assertEqual(self.badAccountExists.account_check(), 4)

    def tearDown(self):
        with open('userAccounts.txt', 'r', encoding = "utf-8") as lns:
            lines = lns.readlines()

        with open('userAccounts.txt', 'w', encoding = "utf-8") as lns:
            for line in lines:
                line = line.rstrip()
                full_line = line.split(",")
                if full_line[1] != "accountTest":
                    lns.write(line)

class TestOperations(unittest.TestCase):
    def setUp(self):
        self.calc1 = GcfClass(12,18)
        self.calc2 = LcmClass(32,13)
        self.pf1 = PfClass(9243)
        self.pf2 = PfClass(6314)
        self.pf3 = PfClass(6312)

    def test_gcf(self):
        class_return = list(self.calc1.gcf().split(" "))
        gcf_value = class_return[len(class_return)-1]
        self.assertEqual(gcf_value, "6")

    def test_lcm(self):
        class2_return = list(self.calc2.lcm().split(" "))
        lcm_value = class2_return[len(class2_return)-1]
        self.assertEqual(lcm_value, "416")

    def test_pf(self):
        self.assertEqual(self.pf1.pf(), [3, 3, 13, 79])
        self.assertEqual(self.pf2.pf(), [2, 7, 11, 41])
        self.assertEqual(self.pf3.pf(), [2, 2, 2, 3, 263])
