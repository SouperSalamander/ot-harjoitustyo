"""file checks user inputs"""
import re

class EntryChecker:
    """class to check entries are only numbers
    
    Attributes:
        __first_entry
    """

    def __init__(self, first_entry):
        self.__first_entry = first_entry

    def check_only_numbers(self):
        """function will check requirements are met"""
        if re.search("[A-Z]", self.__first_entry):
            return False
        if re.search("[a-z]", self.__first_entry):
            return False
        if self.__first_entry.isdigit() is False:
            return False
        if int(self.__first_entry) <= 0:
            return False
        return True
