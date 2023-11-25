from tkinter import *
from tkinter import messagebox
import os
import re 

root = Tk()
root.title("Number Theory")
root.geometry("400x400")

#class to carry out gcf
class gcfClass:
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def gcf(self):
        first = int(self.number1)
        second = int(self.number2)
        isZero = False
        gcf_result = ""
        count = 0
        while isZero == False:
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
            gcf_result = gcf_result + "Step " + str(count) + ": " + str(first) + " / " + str(second) + " = " + str(division) + " remainder: " + str(remainder) + "\n"
            if remainder == 0:
                isZero = True
            else:
                first = second
                second = remainder
        gcf_result = gcf_result + "The Greatest Common Factor is " + str(second)
        return(gcf_result)

class lcmClass():
    def __init__(self, number1, number2):
        self.number1 = number1
        self.number2 = number2

    def lcm(self):
        first = int(self.number1)
        second = int(self.number2)
        gcf_list = list(gcfClass(first,second).gcf().split(" "))
        n = len(gcf_list)
        lcm_is = round((first*second)/(int(gcf_list[n-1])))
        line1 = "Step 1: " + str(first) + " * " + str(second) + " = " + str(first*second)
        line2 = "Step 2: Greatest Common Factor = " + gcf_list[n-1]
        line3 = "Step 3: " + str(first*second) + " / " + gcf_list[n-1] + " = " + str(lcm_is)
        line4 = "The Lowest Common Multiple is " + str(lcm_is)
        lcm_result = line1 + "\n" + line2 + "\n" + line3 + "\n" + line4 
        return(lcm_result)

class searchHistory():
    def __init__(self, name, num1, num2,answer, operation):
        self.name = name
        self.num1 = num1
        self.num2 = num2
        self.answer = answer
        self.operation = operation

    def editHist(self):
        user = self.name
        with open('userAccounts.txt', 'r') as l:
            for line in l:
                line = line.rstrip()
                fullLine = line.split(",")
                if user == fullLine[1]:
                    with open('userAccounts.txt', 'r') as file: 
                        data = file.readlines() 
                    
                    data[int(line[0])-1] = line + "," + self.num1 + " and " + self.num2 + " " + self.operation + self.answer + "\n"
                    with open('userAccounts.txt', 'w') as file: 
                        file.writelines(data) 
                    break

#shows greatest common factor frame
def gcf():
    gcf_entryBox1.delete(0, END)
    gcf_entryBox2.delete(0, END)
    hide_words()
    hide_frames()
    gcf_frame.pack(fill = "both", expand = 1)

#shows lowest common factor frame
def lcm():
    hide_words()
    hide_frames()
    lcm_frame.pack(fill = "both", expand = 1)

#shows prime factorisation frame
def pf():
    hide_words()
    hide_frames()
    pf_frame.pack(fill = "both", expand = 1)   

#shows login frame
def login():
    user_entry.delete(0, END)
    pass_entry.delete(0, END)
    hide_words()
    hide_frames()
    login_frame.pack(fill = "both", expand = 1)

def gcfClear(gcf_add_answer):
    gcf_entryBox1.delete(0, END)
    gcf_entryBox2.delete(0, END)
    hide_words()
    hide_frames()
    gcf_frame.pack(fill = "both", expand = 1)
    gcf_add_answer.destroy()

def gcf_calculation():
    num1 = gcf_entryBox1.get()
    num2 = gcf_entryBox2.get()
    gcf_add_answer = Label(gcf_frame, text = gcfClass(num1,num2).gcf())
    gcf_add_answer.grid(row = 6, column = 1, columnspan = 2)
    gcf_clear = Button(gcf_frame, text = "clear", command = lambda: gcfClear(gcf_add_answer))
    gcf_clear.grid(row = 4, column = 3)

def lcmClear(lcm_add_answer):
    lcm_entryBox1.delete(0, END)
    lcm_entryBox2.delete(0, END)
    hide_words()
    hide_frames()
    lcm_frame.pack(fill = "both", expand = 1)
    lcm_add_answer.destroy()

def lcm_calculation():
    num1 = lcm_entryBox1.get()
    num2 = lcm_entryBox2.get()
    lcm_list = list(lcmClass(num1,num2).lcm().split(" "))
    m = len(lcm_list)
    lcm_is = lcm_list[m-1]
    lcm_add_answer = Label(lcm_frame, text = lcmClass(num1,num2).lcm())
    lcm_add_answer.grid(row = 6, column = 1, columnspan = 2)
    lcm_clear = Button(lcm_frame, text = "clear", command = lambda: lcmClear(lcm_add_answer))
    lcm_clear.grid(row = 4, column = 3)
    searchHistory(user_entry.get(),num1,num2,lcm_is, "lcm: ").editHist() 

#enter function for login
def enterLogin():
    correctDetails = False
    user = user_entry.get()
    password = pass_entry.get()
    with open('userAccounts.txt', 'r') as l:
        for line in l:
            line = line.rstrip()
            fullLine = line.split(",")
            if user == fullLine[1] and password == fullLine[2]:
                correctDetails = True
                break
    if correctDetails == False:
        messagebox.showerror("Error", "Incorrect")
    else:
        mathMenu()

#enter function for create account
def enterCreate():
    correctDetails = False
    if os.path.getsize('userAccounts.txt') !=0:
        with open('userAccounts.txt', 'r') as l:
            list1 = l.readlines()
            fullList = list1
            lastLine = list1[-1]
            lastLine = lastLine.rstrip()
            line = lastLine.split(",")
            uniqID = line[0]
            uniqID = int(uniqID) + 1
    else:
        uniqID = 1
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
        with open('userAccounts.txt', 'r') as l:
            for line in l:
                line = line.rstrip()
                fullLine = line.split(",")
                if username == fullLine[1] and pass1 == fullLine[2]:
                    correctDetails = True     
        if correctDetails == True:
            messagebox.showerror("Error", "Account Already Exists") 
        else:
            fileObject = open('userAccounts.txt', 'a')
            fileObject.write(str(uniqID) + ',' + username + ',' + pass1 + '\n')
            fileObject.close()
            login()

def create_account():
    userCreate_entry.delete(0, END)
    pass1_entry.delete(0, END)
    pass2_entry.delete(0, END)
    hide_words()
    hide_frames()
    create_frame.pack(fill = "both", expand = 1)

def mathMenu():
    hide_words()
    hide_frames()
    menu_frame.pack(fill = "both", expand = 1)

#hides all frames
def hide_frames():
    create_frame.pack_forget()
    login_frame.pack_forget()
    menu_frame.pack_forget()
    gcf_frame.pack_forget()
    lcm_frame.pack_forget()
    pf_frame.pack_forget()

#clears words from the frames
def hide_words():
    welcome_lbl.pack_forget()
    create_btn.pack_forget()
    login_btn.pack_forget()

#returns to welcome page
def back():
    hide_frames()
    welcome_lbl.pack()
    login_btn.pack(pady = 3)
    create_btn.pack(pady = 3)

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

enter_btn = Button(login_frame, text = "Enter", command = enterLogin)
enter_btn.grid(row = 3, column = 1)

temp_btn = Button(login_frame, text = "TEMPORARY LOGIN BYPASS", command = mathMenu)
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

enter_btn = Button(create_frame, text = "Enter", command = enterCreate)
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

gcf_back = Button(gcf_frame, text = "back", command = mathMenu)
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

lcm_back = Button(lcm_frame, text = "back", command = mathMenu)
lcm_back.grid(row = 5, column = 3)

root.mainloop()
#<3
