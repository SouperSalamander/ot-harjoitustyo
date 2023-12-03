"""edits search history"""
from src.file_useage import FileEditor

class SearchHistory():
    """class to add to search history"""
    def __init__(self, name, num1, num2,answer, operation):
        self.name = name
        self.num1 = num1
        self.num2 = num2
        self.answer = answer
        self.operation = operation

    def edit_hist(self):
        """function to edit textfile"""
        if self.operation != "pf:":
            new_hist_str = self.num1 + " and " + self.num2 + " " + \
            self.operation + self.answer + "\n"
        else:
            new_hist_str = self.operation + self.answer + "\n"
        FileEditor(new_hist_str,self.name).add_search_history()
