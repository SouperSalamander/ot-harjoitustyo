"""number theory calculator"""
import os
import re

class GcfClass:
    """class to carry out gcf"""
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def gcf(self):
        """function to carry out gcf"""
        first = int(self.number1)
        second = int(self.number2)
        is_zero = False
        gcf_result = ""
        count = 0
        while is_zero is False:
            count += 1
            difference =  first - second
            if difference < 0:
                temp = first
                first = second
                second = temp
            else:
                pass
            remainder = first % second
            division = int(first/second)
            gcf_result = gcf_result + "Step " + str(count) + ": " + str(first) + " / " + \
            str(second) + " = " + str(division) + " remainder: " + str(remainder) + "\n"
            if remainder == 0:
                is_zero = True
            else:
                first = second
                second = remainder
        gcf_result = gcf_result + "The Greatest Common Factor is " + str(second)
        return gcf_result

class LcmClass():
    """class to carry out lcm"""
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def lcm(self):
        """function to carry out lcm"""
        first = int(self.number1)
        second = int(self.number2)
        gcf_list = list(GcfClass(first,second).gcf().split(" "))
        n = len(gcf_list)
        lcm_is = round((first*second)/(int(gcf_list[n-1])))
        line1 = "Step 1: " + str(first) + " * " + str(second) + " = " + str(first*second)
        line2 = "Step 2: Greatest Common Factor = " + gcf_list[n-1]
        line3 = "Step 3: " + str(first*second) + " / " + gcf_list[n-1] + " = " + str(lcm_is)
        line4 = "The Lowest Common Multiple is " + str(lcm_is)
        lcm_result = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4
        return lcm_result

class ViewHistory():
    """gets the search history text for the label"""
    def __init__(self, name):
        self.name = name
    
    def get_info(self):
        """gets info from file"""
        hist_text = ""
        with open('userAccounts.txt', 'r', encoding = "utf-8") as l:
            for line in l:
                line = line.rstrip()
                full_line = line.split(",")
                if full_line[1] == self.name:
                    line = line.split(",")
                    for i in range(3,len(line)):
                        hist_text = hist_text + line[i] + "\n"
        return hist_text

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
        user = self.name
        with open('userAccounts.txt', 'r+', encoding = "utf-8") as l:
            data = l.readlines()
            for line in data:
                line = line.rstrip()
                full_line = line.split(",")
                if user == full_line[1]:
                    data[int(line[0])-1] = line + "," + self.num1 + " and " + \
                    self.num2 + " " + self.operation + self.answer + "\n"
                    l.seek(0)
                    l.writelines(data)
                    break

class LoginClass():
    """class to check login details"""
    def __init__(self, usern, passw):
        self.usern = usern
        self.passw = passw

    def login_check(self):
        """function compares user input to file"""
        with open('userAccounts.txt', 'r', encoding = "utf-8") as l:
            for line in l:
                line = line.rstrip()
                full_line = line.split(",")
                if self.usern == full_line[1] and self.passw == full_line[2]:
                    return True
            return False

class AccountCreation():
    """class to create accounts"""
    def __init__(self, chosen_user, password1, password2):
        self.chosen_user = chosen_user
        self.password1 = password1
        self.password2 = password2

    def account_check(self):
        """checks if the account meets requirements"""
        repeat_account = False
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
        if self.password1 != self.password2:
            return False, False, True, False, False
        elif not re.search(r"[\d]+", self.password1):
            return False, False, False, True, False
        elif not re.search("[A-Z]", self.password1) and not re.search("[a-z]", self.password1):
            return False, False, False, False, True
        else:
            with open('userAccounts.txt', 'r', encoding = "utf-8") as l:
                for line in l:
                    line = line.rstrip()
                    full_line = line.split(",")
                    if self.chosen_user == full_line[1] and self.password1 == full_line[2]:
                        repeat_account = True
            if repeat_account is True:
                return False, True, False, False, False
            else:
                file_object = open('userAccounts.txt', 'a', encoding = "utf-8")
                file_object.write(str(unique_id) + ',' + self.chosen_user + \
                ',' + self.password1 + '\n')
                file_object.close()
                return True, False, False, False, False
                