"""File for making search history."""
from functionality.file_useage import FileEditor

class SearchHistory():
    """Class to add to search history.
    
    Attributes:
        __name: input username.
        __num1: user input.
        __num2: user input.
        __answer: calculated result.
        __operation: operation used.
    """

    def __init__(self, name, num1, num2,answer, operation):
        """Constructor, makes new search history object.
        
        Args:
            name: input username.
            num1: user input.
            num2: user input.
            answer: calculated result.
            operation: operation used.
        """

        self.__name = name
        self.__num1 = num1
        self.__num2 = num2
        self.__answer = answer
        self.__operation = operation

    def edit_hist(self):
        """Function creates the string that is sent to file editor class."""

        if self.__operation != "pf:":
            new_hist_str = self.__num1 + " and " + self.__num2 + " " + \
            self.__operation + self.__answer + "\n"
        else:
            new_hist_str = self.__operation + self.__answer + "\n"
        FileEditor(new_hist_str,self.__name).add_search_history()
