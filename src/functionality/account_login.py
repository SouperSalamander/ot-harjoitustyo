"""number theory calculator"""
import re
import hashlib
from functionality.file_useage import FileEditor
from functionality.file_useage import FileReader

class LoginClass():
    """class to check login details"""
    def __init__(self, usern, passw):
        self.__usern = usern
        self.__passw = passw

    def login_check(self):
        """function compares user input to file"""
        real_pass = FileReader(self.__usern).find_existing_account()
        if self.__passw == real_pass:
            return True
        return False

class AccountCreation():
    """class to create accounts"""
    def __init__(self, chosen_user, password1, password2):
        self.__chosen_user = chosen_user
        self.__password1 = password1
        self.__password2 = password2

    def account_check(self):
        """checks if the account meets requirements"""
        unique_id = FileReader().find_next_id()
        if self.__password1 != self.__password2:
            return 1
        if not re.search(r"[\d]+", self.__password1):
            return 2
        if not re.search("[A-Z]", self.__password1) and not re.search("[a-z]", self.__password1):
            return 3
        if FileReader(self.__chosen_user).find_existing_account() is not None:
            return 4
        password = self.__password1.encode()
        account_string = str(unique_id) + ',' + self.__chosen_user + ',' + str(hashlib.sha256(password))
        FileEditor(account_string, None).add_new_account()
        return 0
