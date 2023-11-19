from tkinter import *

root = Tk()
root.title("Number Theory")
root.geometry("400x400")

class Operations:
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

def gcf():
    gcf_entryBox1.delete(0, END)
    gcf_entryBox2.delete(0, END)
    hide_words()
    hide_frames()
    gcf_frame.pack(fill = "both", expand = 1)

def lcm():
    hide_words()
    hide_frames()
    lcm_frame.pack(fill = "both", expand = 1)

def pf():
    hide_words()
    hide_frames()
    pf_frame.pack(fill = "both", expand = 1)   

def enterLogin():
    pass

def login():
    user_entry.delete(0, END)
    pass_entry.delete(0, END)
    hide_words()
    hide_frames()
    login_frame.pack(fill = "both", expand = 1)

def clear(gcf_add_answer):
    gcf_entryBox1.delete(0, END)
    gcf_entryBox2.delete(0, END)
    hide_words()
    hide_frames()
    gcf_frame.pack(fill = "both", expand = 1)
    gcf_add_answer.destroy()

def gcf_calculation():
    num1 = gcf_entryBox1.get()
    num2 = gcf_entryBox2.get()
    gcf_add_answer = Label(gcf_frame, text = Operations(num1,num2).gcf())
    gcf_add_answer.grid(row = 6, column = 1, columnspan = 2)
    gcf_clear = Button(gcf_frame, text = "clear", command = lambda: clear(gcf_add_answer))
    gcf_clear.grid(row = 4, column = 3)

def create_account():
    pass

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
title_lbl = Label(gcf_frame, text = "Greatest Common Factor")
title_lbl.grid(row = 1, column = 1, columnspan = 2)

first_lbl = Label(gcf_frame, text = "first number: ")
first_lbl.grid(row = 2, column = 1)

gcf_entryBox1 = Entry(gcf_frame)
gcf_entryBox1.grid(row = 2, column = 2)

second_lbl = Label(gcf_frame, text = "second number: ")
second_lbl.grid(row = 3, column = 1)

gcf_entryBox2 = Entry(gcf_frame)
gcf_entryBox2.grid(row = 3, column = 2)

gcf_enter = Button(gcf_frame, text = "Calculate", width = 30, command = gcf_calculation)
gcf_enter.grid(row = 4, column = 1, columnspan = 2)

gcf_back = Button(gcf_frame, text = "back", command = mathMenu)
gcf_back.grid(row = 5, column = 3)

root.mainloop()
#<3
