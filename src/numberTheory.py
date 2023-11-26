from tkinter import *
from tkinter import messagebox
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

def gcf():
    """shows greatest common factor frame"""
    gcf_entryBox1.delete(0, END)
    gcf_entryBox2.delete(0, END)
    hide_words()
    hide_frames()
    gcf_frame.pack(fill = "both", expand = 1)

def lcm():
    """shows lowest common factor frame"""
    hide_words()
    hide_frames()
    lcm_frame.pack(fill = "both", expand = 1)

def pf():
    """shows prime factorisation frame"""
    hide_words()
    hide_frames()
    pf_frame.pack(fill = "both", expand = 1)   

def login():
    """shows login frame"""
    user_entry.delete(0, END)
    pass_entry.delete(0, END)
    hide_words()
    hide_frames()
    login_frame.pack(fill = "both", expand = 1)

def gcf_clear(gcf_add_answer):
    """clears gcf frame"""
    gcf_entryBox1.delete(0, END)
    gcf_entryBox2.delete(0, END)
    hide_words()
    hide_frames()
    gcf_frame.pack(fill = "both", expand = 1)
    gcf_add_answer.destroy()

def gcf_calculation():
    """shows gcf result"""
    num1 = gcf_entryBox1.get()
    num2 = gcf_entryBox2.get()
    gcf_add_answer = Label(gcf_frame, text = GcfClass(num1,num2).gcf())
    gcf_add_answer.grid(row = 6, column = 1, columnspan = 2)
    gcf_clear_frame = Button(gcf_frame, text = "clear", command = lambda: gcf_clear(gcf_add_answer))
    gcf_clear_frame.grid(row = 4, column = 3)

def lcm_clear(lcm_add_answer):
    """clears lcm frame"""
    lcm_entryBox1.delete(0, END)
    lcm_entryBox2.delete(0, END)
    hide_words()
    hide_frames()
    lcm_frame.pack(fill = "both", expand = 1)
    lcm_add_answer.destroy()

def lcm_calculation():
    """shows lcm results"""
    num1 = lcm_entryBox1.get()
    num2 = lcm_entryBox2.get()
    lcm_list = list(LcmClass(num1,num2).lcm().split(" "))
    m = len(lcm_list)
    lcm_is = lcm_list[m-1]
    lcm_add_answer = Label(lcm_frame, text = LcmClass(num1,num2).lcm())
    lcm_add_answer.grid(row = 6, column = 1, columnspan = 2)
    lcm_clear_frame = Button(lcm_frame, text = "clear", command = lambda: lcm_clear(lcm_add_answer))
    lcm_clear_frame.grid(row = 4, column = 3)
    SearchHistory(user_entry.get(),num1,num2,lcm_is, "lcm: ").edit_hist()

def enter_login():
    """enter function for login"""
    user = user_entry.get()
    password = pass_entry.get()
    correct_details = LoginClass(user, password).login_check()
    if correct_details is False:
        messagebox.showerror("Error", "Incorrect")
    else:
        math_menu()

def enter_create():
    """enter function for create account"""
    correct_details = False
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
    username = userCreate_entry.get()
    pass1 = pass1_entry.get()
    pass2 = pass2_entry.get()
    if pass1 != pass2:
        messagebox.showerror("Error", "Passwords don't match")
    elif not re.search(r"[\d]+", pass1):
        messagebox.showerror("Error", "Must contain a number")
    elif not re.search("[A-Z]", pass1) and not re.search("[a-z]", pass1):
        messagebox.showerror("Error", "Must contain a letter")
    else:
        with open('userAccounts.txt', 'r', encoding = "utf-8") as l:
            for line in l:
                line = line.rstrip()
                full_line = line.split(",")
                if username == full_line[1] and pass1 == full_line[2]:
                    correct_details = True
        if correct_details is True:
            messagebox.showerror("Error", "Account Already Exists")
        else:
            file_object = open('userAccounts.txt', 'a', encoding = "utf-8")
            file_object.write(str(unique_id) + ',' + username + ',' + pass1 + '\n')
            file_object.close()
            login()

def create_account():
    """shows the account creation frame"""
    userCreate_entry.delete(0, END)
    pass1_entry.delete(0, END)
    pass2_entry.delete(0, END)
    hide_words()
    hide_frames()
    create_frame.pack(fill = "both", expand = 1)

def math_menu():
    """shows the menu frame"""
    hide_words()
    hide_frames()
    menu_frame.pack(fill = "both", expand = 1)

def hide_frames():
    """hides all frames"""
    create_frame.pack_forget()
    login_frame.pack_forget()
    menu_frame.pack_forget()
    gcf_frame.pack_forget()
    lcm_frame.pack_forget()
    pf_frame.pack_forget()

def hide_words():
    """clears words from the frames"""
    welcome_lbl.pack_forget()
    create_btn.pack_forget()
    login_btn.pack_forget()

def back():
    """returns to welcome page"""
    hide_frames()
    welcome_lbl.pack()
    login_btn.pack(pady = 3)
    create_btn.pack(pady = 3)

if __name__=="__main__":

    root = Tk()
    root.title("Number Theory")
    root.geometry("400x400")

    welcome_lbl = Label(root, text = "Welcome", font = (None, 22))
    welcome_lbl.pack()

    #creates login button
    login_btn = Button(root, text = "Login", command = login)
    login_btn.pack(pady = 3)

    #makes create account button
    create_btn = Button(root, text = "Create Account", command = create_account)
    create_btn.pack(pady = 3)

    #creats the different frames
    create_frame = Frame(root, width = 400, height = 400)
    login_frame = Frame(root, width = 400, height = 400)
    menu_frame = Frame(root, width = 400, height = 400)
    gcf_frame = Frame(root, width = 400, height = 400)
    lcm_frame = Frame(root, width = 400, height = 400)
    pf_frame = Frame(root, width = 400, height = 400)

    #login
    login_lbl = Label(login_frame, text = "Login", font = (None, 22))
    login_lbl.grid(row = 0, column = 1)

    lbl_username = Label(login_frame, text = "Username:")
    lbl_username.grid(row = 1, column = 0)

    user_entry = Entry(login_frame)
    user_entry.grid(row = 1, column = 1)

    lbl_password = Label(login_frame, text = "Password:")
    lbl_password.grid(row = 2, column = 0)

    pass_entry = Entry(login_frame, show = "*")
    pass_entry.grid(row = 2, column = 1)

    enter_btn = Button(login_frame, text = "Enter", command = enter_login)
    enter_btn.grid(row = 3, column = 1)

    temp_btn = Button(login_frame, text = "TEMPORARY LOGIN BYPASS", command = math_menu)
    temp_btn.grid(row = 4, column = 1)

    back_btn = Button(login_frame, text = "BACK", command = back)
    back_btn.grid(row = 4, column = 2)

    back_btn = Button(create_frame, text = "BACK", command = back)
    back_btn.grid(row = 5, column = 2)

    #create account
    create_lbl = Label(create_frame, text = "Create Account", font = (None, 22))
    create_lbl.grid(row = 0, column = 1)

    userCreate = Label(create_frame, text = "Create Username:")
    userCreate.grid(row = 1, column = 0)

    userCreate_entry = Entry(create_frame)
    userCreate_entry.grid(row = 1, column = 1)

    pass1_lbl = Label(create_frame, text = "Create Password:")
    pass1_lbl.grid(row = 2, column = 0)

    pass1_entry = Entry(create_frame, show = "*")
    pass1_entry.grid(row = 2, column = 1)

    pass2_lbl = Label(create_frame, text = "Confirm Password:")
    pass2_lbl.grid(row = 3, column = 0)

    pass2_entry = Entry(create_frame, show = "*")
    pass2_entry.grid(row = 3, column = 1)

    enter_btn = Button(create_frame, text = "Enter", command = enter_create)
    enter_btn.grid(row = 4, column = 1)

    #math menu
    menu_lbl = Label(menu_frame, text = "Menu", font = (None, 22))
    menu_lbl.pack()

    gcf_btn = Button(menu_frame, text = "Greatest Common Factor", command = gcf)
    gcf_btn.pack(pady = 3)

    lcm_btn = Button(menu_frame, text = "Lowest Common Multiple", command = lcm)
    lcm_btn.pack(pady = 3)

    pf_btn = Button(menu_frame, text = "Prime Factorisation", command = pf)
    pf_btn.pack(pady = 3)

    logOut_btn = Button(menu_frame, text = "Log Out", command = back)
    logOut_btn.pack(pady = 3)

    #gcf frame
    gcf_lbl = Label(gcf_frame, text = "Greatest Common Factor")
    gcf_lbl.grid(row = 1, column = 1, columnspan = 2)

    gcf_first_lbl = Label(gcf_frame, text = "first number: ")
    gcf_first_lbl.grid(row = 2, column = 1)

    gcf_entryBox1 = Entry(gcf_frame)
    gcf_entryBox1.grid(row = 2, column = 2)

    gcf_second_lbl = Label(gcf_frame, text = "second number: ")
    gcf_second_lbl.grid(row = 3, column = 1)

    gcf_entryBox2 = Entry(gcf_frame)
    gcf_entryBox2.grid(row = 3, column = 2)

    gcf_enter = Button(gcf_frame, text = "Calculate", width = 30, command = gcf_calculation)
    gcf_enter.grid(row = 4, column = 1, columnspan = 2)

    gcf_back = Button(gcf_frame, text = "back", command = math_menu)
    gcf_back.grid(row = 5, column = 3)

    #lcm frame
    lcm_lbl = Label(lcm_frame, text = "Lowest Common Multiple")
    lcm_lbl.grid(row = 1, column = 1, columnspan = 2)

    lcm_first_lbl = Label(lcm_frame, text = "first number: ")
    lcm_first_lbl.grid(row = 2, column = 1)

    lcm_entryBox1 = Entry(lcm_frame)
    lcm_entryBox1.grid(row = 2, column = 2)

    lcm_second_lbl = Label(lcm_frame, text = "second number: ")
    lcm_second_lbl.grid(row = 3, column = 1)

    lcm_entryBox2 = Entry(lcm_frame)
    lcm_entryBox2.grid(row = 3, column = 2)

    lcm_enter = Button(lcm_frame, text = "Calculate", width = 30, command = lcm_calculation)
    lcm_enter.grid(row = 4, column = 1, columnspan = 2)

    lcm_back = Button(lcm_frame, text = "back", command = math_menu)
    lcm_back.grid(row = 5, column = 3)

    root.mainloop()
#<3
