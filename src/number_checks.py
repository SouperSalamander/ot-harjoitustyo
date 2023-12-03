"""makes sure user only gives suitable numbers"""
import re

class EntryChecker:
    """class to check entries are only numbers"""
    def __init__(self, first_entry):
        self.first_entry = first_entry

    def check_only_numbers(self):
        """function will check requirements are met"""
        if re.search("[A-Z]", self.first_entry):
            return False
        if re.search("[a-z]", self.first_entry):
            return False
        if self.first_entry.isdigit() is False:
            return False
        if int(self.first_entry) <= 0:
            return False
        return True
