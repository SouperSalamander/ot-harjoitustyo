"""number theory calculator"""
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
        real_pass = FileReader(self.usern).find_existing_account()
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
        unique_id = FileReader().find_next_id()
        if self.password1 != self.password2:
            return 1
        if not re.search(r"[\d]+", self.password1):
            return 2
        if not re.search("[A-Z]", self.password1) and not re.search("[a-z]", self.password1):
            return 3
        if FileReader(self.chosen_user).find_existing_account() is not None:
            return 4
        account_string = str(unique_id) + ',' + self.chosen_user + ',' + self.password1
        FileEditor(account_string, None).add_new_account()
        return 0
                