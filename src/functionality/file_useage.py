"""number theory calculator"""
import os

class FileReader:
    """class to return file content"""
    def __init__(self, line_choice = None):
        self.__line_choice = line_choice

    def find_next_id(self):
        if os.path.isfile('userAccounts.txt') is False:
            with open('userAccounts.txt','a', encoding = "utf-8") as file:
                file.close()
        if os.path.getsize('userAccounts.txt') !=0:
            with open('userAccounts.txt', 'r', encoding = "utf-8") as l:
                list1 = l.readlines()
                last_line = list1[-1]
                last_line = last_line.rstrip()
                line = last_line.split(",")
                unique_id = line[0]
                unique_id = int(unique_id) + 1
        else:
            unique_id = 1
        return unique_id

    def find_existing_account(self):
        if os.path.isfile('userAccounts.txt') is False:
            with open('userAccounts.txt','a', encoding = "utf-8") as file:
                file.close()
        with open('userAccounts.txt', 'r', encoding = "utf-8") as l:
            for line in l:
                line = line.rstrip()
                full_line = line.split(",")
                if self.__line_choice == full_line[1]:
                    return full_line[2]
        return None

    def read_search_history(self):
        hist_text = ""
        with open('userAccounts.txt', 'r', encoding = "utf-8") as l:
            for line in l:
                line = line.rstrip()
                full_line = line.split(",")
                if full_line[1] == self.__line_choice:
                    line = line.split(",")
                    for i in range(3,len(line)):
                        hist_text = hist_text + line[i] + "\n"
        return hist_text

class FileEditor:
    """class for file use"""
    def __init__(self, file_content,location):
        self.__file_content = file_content
        self.__location = location

    def add_new_account(self):
        """funtion to change parts of file"""
        with open('userAccounts.txt', 'a', encoding = "utf-8") as file_object:
            file_object.write(self.__file_content + '\n')
            file_object.close()

    def add_search_history(self):
        """function adds the search history string to a specific line of the file"""
        user = self.__location
        with open('userAccounts.txt', 'r+', encoding = "utf-8") as l:
            data = l.readlines()
            for line in data:
                line = line.rstrip()
                full_line = line.split(",")
                if user == full_line[1]:
                    data[int(line[0])-1] = line + "," + self.__file_content
                    l.seek(0)
                    l.writelines(data)
                    break
