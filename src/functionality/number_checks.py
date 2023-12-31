"""File checks user inputs."""
import re

class EntryChecker:
    """Class to check entries are only numbers.
    
    Attributes:
        __first_entry: input from user.
    """

    def __init__(self, first_entry):
        """Constructor, makes new entry checker object.
        
        Args:
            first_entry: input from user.
        """

        self.__first_entry = first_entry

    def check_only_numbers(self):
        """Function will check requirements are met.
        
        Returns:
            True, if entry is suitable, otherwise False.
        """
        if len(self.__first_entry) == 0:
            return False
        if not re.search("^[0-9]*$", self.__first_entry):
            return False
        if int(self.__first_entry) <= 0:
            return False
        return True
