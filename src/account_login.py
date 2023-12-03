"""number theory calculator"""
import os
import re
from src.file_useage import FileEditor
from src.file_useage import FileReader

class LoginClass():
    """class to check login details"""
    def __init__(self, usern, passw):
        self.usern = usern
        self.passw = passw

    def login_check(self):
        """function compares user input to file"""
        real_pass = FileReader(self.usern).read_login_details()
        if self.passw == real_pass:
            return True
        return False

class AccountCreation():
    """class to create accounts"""
    def __init__(self, chosen_user, password1, password2):
        self.chosen_user = chosen_user
        self.password1 = password1
        self.password2 = password2

    def account_check(self):
        """checks if the account meets requirements"""
        repeat_account = False
        if os.path.isfile('userAccounts.txt') is False:#add a read file thingy here that does this
            with open('userAccounts.txt','a', encoding = "utf-8") as file:
                file.close()
        if os.path.getsize('userAccounts.txt') !=0:
            with open('userAccounts.txt', 'r', encoding = "utf-8") as l:
                list1 = l.readlines()
                last_line = list1[-1]
                last_line = last_line.rstrip()
                line = last_line.split(",")
                unique_id = line[0]
                unique_id = int(unique_id) + 1
        else:
            unique_id = 1
        if self.password1 != self.password2:
            return 1
        if not re.search(r"[\d]+", self.password1):
            return 2
        if not re.search("[A-Z]", self.password1) and not re.search("[a-z]", self.password1):
            return 3
        with open('userAccounts.txt', 'r', encoding = "utf-8") as l:
            for line in l:
                line = line.rstrip()
                full_line = line.split(",")
                if self.chosen_user == full_line[1] and self.password1 == full_line[2]:
                    repeat_account = True
        if repeat_account is True:
            return 4
        account_string = str(unique_id) + ',' + self.chosen_user + ',' + self.password1
        FileEditor(account_string, None).add_new_account()
        return 0
                