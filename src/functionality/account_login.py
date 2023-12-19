"""File deals with user accounts."""
import re
import hashlib
from functionality.file_useage import FileEditor
from functionality.file_useage import FileReader

class LoginClass():
    """Class to check login details.
    
    Attributes:
        __usern: the username input by the user.
        __passw: the password input by the user.
    """

    def __init__(self, usern, passw):
        """Constructor, makes new login object.

        Args: 
            usern: the username input by the user.
            passw: the password input by the user.
        """

        self.__usern = usern
        self.__passw = passw

    def login_check(self):
        """Function compares username input to username stored in file.
        
        Returns:
            True, if the username and password match the file, otherwise false.
        """

        password_input = self.__passw.encode()
        real_pass = FileReader(self.__usern).find_existing_account()
        if hashlib.sha256(password_input).hexdigest() == real_pass:
            return True
        return False

class AccountCreation():
    """Class to create accounts.
    
    Attributes:
        __chosen_user: users input username.
        __password1: users input password.
        __password2: users second input password.
    """

    def __init__(self, chosen_user, password1, password2):
        """Constructor, makes new create account object.

        Args:
            chosen_user: users input username.
            password1: users input password.
            password2: users second input password.
        """

        self.__chosen_user = chosen_user
        self.__password1 = password1
        self.__password2 = password2

    def account_check(self):
        """Function checks if the account meets requirements.
        
        Returns:
            0, if the account meets the requirements, otherwise number 1 to 4 depending on issue.
        """
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
        account_string = str(unique_id) + ',' + self.__chosen_user + \
        ',' + hashlib.sha256(password).hexdigest()
        FileEditor(account_string, None).add_new_account()
        return 0
