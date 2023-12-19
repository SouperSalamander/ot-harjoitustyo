"""File handles account file access."""
import os

class FileReader:
    """Class to return file content.
    
    Attributes:
        __line_choice: the username input from user.
    """

    def __init__(self, line_choice = None):
        """Constructor, makes new file reader.
        
        Args:
            line_choice: the username input from user.
        """

        self.__line_choice = line_choice

    def find_next_id(self):
        """Function finds the 0th element of the last line in the file.
        
        Returns:
            Integer, any whole number more than zero.
        """

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
        """Function checks if an account is already present in the file.
        
        Returns:
            String, if the account exists, otherwise None.
        """

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
        """Function to create the search history.
        
        Returns:
            String.
        """

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
    """Class for editing file contents. 
    
    Attributes:
        __file_content: a string to be added to the file.
        __location: the line in the file.
    """

    def __init__(self, file_content,location):
        """Constructor, creates new file editor.
        
        Args:
            file_content: a string to be added to the file.
            location: the line in the file.
        """

        self.__file_content = file_content
        self.__location = location

    def add_new_account(self):
        """Funtion to add account details to the file."""

        with open('userAccounts.txt', 'a', encoding = "utf-8") as file_object:
            file_object.write(self.__file_content + '\n')
            file_object.close()

    def add_search_history(self):
        """Function adds the search history string to a specific line of the file."""

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
