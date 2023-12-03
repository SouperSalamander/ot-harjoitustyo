"""number theory calculator"""
import os

class FileReader:
    """class to return file content"""
    def __init__(self, line_choice):
        self.line_choice = line_choice

    def read_login_details(self):
        if os.path.isfile('userAccounts.txt') is False:
            with open('userAccounts.txt','a', encoding = "utf-8") as file:
                file.close()
        with open('userAccounts.txt', 'r', encoding = "utf-8") as l:
            for line in l:
                line = line.rstrip()
                full_line = line.split(",")
                if self.line_choice == full_line[1]:
                    return full_line[2]
        return None

    def read_search_history(self):
        hist_text = ""
        with open('userAccounts.txt', 'r', encoding = "utf-8") as l:
            for line in l:
                line = line.rstrip()
                full_line = line.split(",")
                if full_line[1] == self.line_choice:
                    line = line.split(",")
                    for i in range(3,len(line)):
                        hist_text = hist_text + line[i] + "\n"
        return hist_text

class FileEditor:
    """class for file use"""
    def __init__(self, file_content,location):
        self.file_content = file_content
        self.location = location

    def add_new_account(self):
        """funtion to change parts of file"""
        with open('userAccounts.txt', 'a', encoding = "utf-8") as file_object:
            file_object.write(self.file_content + '\n')
            file_object.close()

    def add_search_history(self):
        user = self.location
        with open('userAccounts.txt', 'r+', encoding = "utf-8") as l:
            data = l.readlines()
            for line in data:
                line = line.rstrip()
                full_line = line.split(",")
                if user == full_line[1]:
                    data[int(line[0])-1] = line + "," + self.file_content
                    l.seek(0)
                    l.writelines(data)
                    break
