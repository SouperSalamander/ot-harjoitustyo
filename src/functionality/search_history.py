"""edits search history"""
from functionality.file_useage import FileEditor

class SearchHistory():
    """class to add to search history"""
    def __init__(self, name, num1, num2,answer, operation):
        self.__name = name
        self.__num1 = num1
        self.__num2 = num2
        self.__answer = answer
        self.__operation = operation

    def edit_hist(self):
        """function to edit textfile"""
        if self.__operation != "pf:":
            new_hist_str = self.__num1 + " and " + self.__num2 + " " + \
            self.__operation + self.__answer + "\n"
        else:
            new_hist_str = self.__operation + self.__answer + "\n"
        FileEditor(new_hist_str,self.__name).add_search_history()
