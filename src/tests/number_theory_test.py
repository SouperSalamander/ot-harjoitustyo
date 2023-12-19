import unittest
import os
import hashlib
from functionality.account_login import *
from functionality.operations import *
from functionality.number_checks import *
from functionality.quizzes import *

class TestLogin(unittest.TestCase):
    def setUp(self):
        self.good_info = LoginClass("fake","account")
        self.bad_info = LoginClass("wrong","bad")

    def test_correct_login(self):
        fake_password = "account".encode()
        if os.path.isfile('userAccounts.txt') is False:
            with open('userAccounts.txt','a', encoding = "utf-8") as file:
                file.close()
        with open('userAccounts.txt', 'a', encoding = "utf-8") as file_object:
            file_object.write('0' + ',' + 'fake' + \
            ',' + hashlib.sha256(fake_password).hexdigest() + '\n')
            file_object.close()

        self.assertEqual(self.good_info.login_check(), True)

        with open("userAccounts.txt", "r", encoding = "utf-8") as f:
            lines = f.readlines()
        with open("userAccounts.txt", "w", encoding = "utf-8") as f:
            for line in lines:
                if line.split(",")[0] != "0":
                    f.write(line)

    def test_wrong_login(self):
        self.assertEqual(self.bad_info.login_check(), False)

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

    def test_account_exists_true(self):
        if os.path.isfile('userAccounts.txt') is False:
            with open('userAccounts.txt','a', encoding = "utf-8") as file:
                file.close()
        with open('userAccounts.txt', 'a', encoding = "utf-8") as file_object:
            file_object.write('0' + ',' + 'accountTest' + \
            ',' + 'pass1' + '\n')
            file_object.close()

        self.assertEqual(self.badAccountExists.account_check(), 4)

    def test_account_exists_false(self):
        if os.path.isfile('userAccounts.txt') is False:
            with open('userAccounts.txt','a', encoding = "utf-8") as file:
                file.close()
        with open('userAccounts.txt', 'a', encoding = "utf-8") as file_object:
            file_object.write('0' + ',' + 'accountTest' + \
            ',' + 'pass2' + '\n')
            file_object.write('0' + ',' + 'accountTest' + \
            ',' + 'pass1' + '\n')
            file_object.close()
        self.assertEqual(self.badAccountExists.account_check(), 4)

    def tearDown(self):
        with open("userAccounts.txt", "r", encoding = "utf-8") as f:
            lines = f.readlines()
        with open("userAccounts.txt", "w", encoding = "utf-8") as f:
            for line in lines:
                if line.split(",")[1] != "accountTest":
                    f.write(line)

class TestNumberChecker(unittest.TestCase):
    def setUp(self):
        self.good_num = EntryChecker("45")
        self.bad_num_letter = EntryChecker("abc")
        self.bad_num_cap = EntryChecker("ABC")
        self.bad_no_num = EntryChecker(" ")
        self.bad_num_zero = EntryChecker("0")
        self.bad_num_neg = EntryChecker("-5")
        self.bad_num_mix = EntryChecker("erjbfiFF?!] rf8329/.sd/")

    def test_good_entry(self):
        self.assertEqual(self.good_num.check_only_numbers(), True)

    def test_bad_entries(self):
        self.assertEqual(self.bad_num_letter.check_only_numbers(), False)
        self.assertEqual(self.bad_num_cap.check_only_numbers(), False)
        self.assertEqual(self.bad_no_num.check_only_numbers(), False)
        self.assertEqual(self.bad_num_zero.check_only_numbers(), False)
        self.assertEqual(self.bad_num_neg.check_only_numbers(), False)
        self.assertEqual(self.bad_num_mix.check_only_numbers(), False)

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

class TestQuiz(unittest.TestCase):
    def setUp(self):
        self.correct_gcf_answer = QuizClass(69,24,"3")
        self.wrong_gcf_answer = QuizClass(12,18,"5")
        self.correct_lcm_answer = QuizClass(3,4,"12")
        self.wrong_lcm_answer = QuizClass(3,4,"5")
        self.correct_pf_answer = QuizClass(20,None,"2 2 5")
        self.wrong_pf_answer = QuizClass(20,None,"2 5")
        self.wrong_pf_answer_same_length = QuizClass(20,None,"2 3 4")
        self.correct_pf_answer_diff_order = QuizClass(40,None,"2 2 5 2")

    def test_num_generator(self):
        self.assertTrue(1 <= int(QuizClass().get_numbers()[0]) <= 99)
        self.assertTrue(1 <= int(QuizClass().get_numbers()[1]) <= 99)

    def test_gcf_quiz(self):
        self.assertEqual(self.correct_gcf_answer.find_gcf_result(), "Correct")
        self.assertEqual(self.wrong_gcf_answer.find_gcf_result(), "Incorrect. Correct answer is: 6")

    def test_lcm_quiz(self):
        self.assertEqual(self.correct_lcm_answer.find_lcm_result(), "Correct")
        self.assertEqual(self.wrong_lcm_answer.find_lcm_result(), "Incorrect. Correct answer is: 12")

    def test_pf_quiz(self):
        self.assertEqual(self.correct_pf_answer.find_pf_result(), "Correct")
        self.assertEqual(self.wrong_pf_answer.find_pf_result(), "Incorrect. Correct answer is: [2, 2, 5]")
        self.assertEqual(self.wrong_pf_answer_same_length.find_pf_result(), "Incorrect. Correct answer is: [2, 2, 5]")
        self.assertEqual(self.correct_pf_answer_diff_order.find_pf_result(), "Correct")
