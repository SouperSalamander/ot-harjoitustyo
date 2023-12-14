from functionality.account_login import *
from functionality.operations import *
from functionality.file_useage import *
from functionality.number_checks import *
from functionality.search_history import *
from functionality.quizzes import *
from tkinter import *
from tkinter import messagebox
import os
import re
import math
import hashlib

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

def clear_history_frame(hist_lbl,hist_back):
    """clears history frame"""
    hide_words()
    hide_frames()
    history_frame.pack(fill = "both", expand = 1)
    hist_lbl.destroy()
    hist_back.destroy()
    math_menu()

def see_history():
    """user can look at search history"""
    hide_words()
    hide_frames()
    history_frame.pack(fill = "both", expand = 1)
    history_text = FileReader(user_entry.get()).read_search_history()
    hist_lbl = Label(history_frame, text = history_text)
    hist_lbl.pack(pady = 3)
    hist_back = Button(history_frame, text = "BACK", command = lambda: clear_history_frame(hist_lbl,hist_back))
    hist_back.pack(pady = 3)

def clear_gcf_test_lbls(flag, gcf_test_entry,gcf_question_lbl,gcf_box_lbl,back,gcf_test_enter_btn,gcf_test_answer_lbl,gcf_test_clear):
    gcf_test_entry.pack_forget()
    gcf_box_lbl.pack_forget()
    gcf_question_lbl.pack_forget()
    back.pack_forget()
    gcf_test_enter_btn.pack_forget()
    gcf_test_entry
    if flag == 1:
        try_quiz()
    else:
        gcf_test_answer_lbl.pack_forget()
        gcf_test_clear.pack_forget()
        test_gcf()

def gcf_test_results(num1,num2,gcf_question_lbl,gcf_box_lbl,gcf_test_entry,back,gcf_test_enter_btn,gcf_test_answer_lbl):
    hide_words()
    hide_frames()
    gcf_quiz_frame.pack(fill = "both", expand = 1)
    gcf_question_lbl.pack(pady = 3)
    gcf_box_lbl.pack()
    gcf_test_enter_btn.pack()
    attempt = gcf_test_entry.get()
    if EntryChecker(attempt).check_only_numbers() is False:
        messagebox.showerror("Error", "only accepts whole numbers more than zero (no spaces)")
    else:
        correct_gcf = QuizClass(num1,num2,attempt).find_gcf_result()
        gcf_test_answer_lbl = Label(gcf_quiz_frame, text = correct_gcf)
        gcf_test_answer_lbl.pack(pady = 3)
        back.pack()
        flag = 0
        gcf_test_clear = Button(gcf_quiz_frame, text = "try again", command = lambda: clear_gcf_test_lbls(flag, gcf_test_entry,gcf_question_lbl,gcf_box_lbl,back,gcf_test_enter_btn,gcf_test_answer_lbl,gcf_test_clear))
        gcf_test_clear.pack(pady = 3)

def test_gcf():
    """user can answer questions about gcf"""
    hide_words()
    hide_frames()
    gcf_quiz_frame.pack(fill = "both", expand = 1)
    num1,num2 = QuizClass().get_numbers()
    question = str(num1) + " , " + str(num2)
    gcf_question_lbl = Label(gcf_quiz_frame, text = question, font = (None, 22))
    gcf_question_lbl.pack(pady = 3)
    gcf_box_lbl = Label(gcf_quiz_frame, text = "Greatest Common Factor:")
    gcf_box_lbl.pack()
    gcf_test_entry = Entry(gcf_quiz_frame)
    gcf_test_entry.pack()
    attempt = gcf_test_entry.get()
    gcf_test_enter_btn = Button(gcf_quiz_frame, text = "Enter", command = lambda: gcf_test_results(num1,num2,gcf_question_lbl,gcf_box_lbl,gcf_test_entry,back,gcf_test_enter_btn,gcf_test_answer_lbl))
    gcf_test_enter_btn.pack(pady = 3)
    flag = 1
    gcf_test_answer_lbl = None
    gcf_test_clear = None
    back = Button(gcf_quiz_frame, text = "back", command = lambda: clear_gcf_test_lbls(flag, gcf_test_entry,gcf_question_lbl,gcf_box_lbl,back,gcf_test_enter_btn,gcf_test_answer_lbl,gcf_test_clear))
    back.pack(pady = 10)

def clear_lcm_test_lbls(flag, lcm_test_entry,lcm_question_lbl,lcm_box_lbl,back,lcm_test_enter_btn,lcm_test_answer_lbl,lcm_test_clear):
    lcm_test_entry.pack_forget()
    lcm_box_lbl.pack_forget()
    lcm_question_lbl.pack_forget()
    back.pack_forget()
    lcm_test_enter_btn.pack_forget()
    lcm_test_entry
    if flag == 1:
        try_quiz()
    else:
        lcm_test_answer_lbl.pack_forget()
        lcm_test_clear.pack_forget()
        test_lcm()

def lcm_test_results(num1,num2,lcm_question_lbl,lcm_box_lbl,lcm_test_entry,back,lcm_test_enter_btn,lcm_test_answer_lbl):
    hide_words()
    hide_frames()
    lcm_quiz_frame.pack(fill = "both", expand = 1)
    lcm_question_lbl.pack(pady = 3)
    lcm_box_lbl.pack()
    lcm_test_enter_btn.pack()
    attempt = lcm_test_entry.get()
    if EntryChecker(attempt).check_only_numbers() is False:
        messagebox.showerror("Error", "only accepts whole numbers more than zero (no spaces)")
    else:
        correct_lcm = QuizClass(num1,num2,attempt).find_lcm_result()
        lcm_test_answer_lbl = Label(lcm_quiz_frame, text = correct_lcm)
        lcm_test_answer_lbl.pack(pady = 3)
        back.pack()
        flag = 0
        lcm_test_clear = Button(lcm_quiz_frame, text = "try again", command = lambda: clear_lcm_test_lbls(flag, lcm_test_entry,lcm_question_lbl,lcm_box_lbl,back,lcm_test_enter_btn,lcm_test_answer_lbl,lcm_test_clear))
        lcm_test_clear.pack(pady = 3)

def test_lcm():
    """user can answer questions about lcm"""
    hide_words()
    hide_frames()
    lcm_quiz_frame.pack(fill = "both", expand = 1)
    num1,num2 = QuizClass().get_numbers()
    question = str(num1) + " , " + str(num2)
    lcm_question_lbl = Label(lcm_quiz_frame, text = question, font = (None, 22))
    lcm_question_lbl.pack(pady = 3)
    lcm_box_lbl = Label(lcm_quiz_frame, text = "Lowest Common Multiple:")
    lcm_box_lbl.pack()
    lcm_test_entry = Entry(lcm_quiz_frame)
    lcm_test_entry.pack()
    attempt = lcm_test_entry.get()
    lcm_test_enter_btn = Button(lcm_quiz_frame, text = "Enter", command = lambda: lcm_test_results(num1,num2,lcm_question_lbl,lcm_box_lbl,lcm_test_entry,back,lcm_test_enter_btn,lcm_test_answer_lbl))
    lcm_test_enter_btn.pack(pady = 3)
    flag = 1
    lcm_test_answer_lbl = None
    lcm_test_clear = None
    back = Button(lcm_quiz_frame, text = "back", command = lambda: clear_lcm_test_lbls(flag, lcm_test_entry,lcm_question_lbl,lcm_box_lbl,back,lcm_test_enter_btn,lcm_test_answer_lbl,lcm_test_clear))
    back.pack(pady = 10)

def clear_pf_test_lbls(flag, pf_test_entry,pf_question_lbl,pf_box_lbl,back,pf_test_enter_btn,pf_test_answer_lbl,pf_test_clear):
    pf_test_entry.pack_forget()
    pf_box_lbl.pack_forget()
    pf_question_lbl.pack_forget()
    back.pack_forget()
    pf_test_enter_btn.pack_forget()
    pf_test_entry
    if flag == 1:
        try_quiz()
    else:
        pf_test_answer_lbl.pack_forget()
        pf_test_clear.pack_forget()
        test_pf()

def pf_test_results(num1,pf_question_lbl,pf_box_lbl,pf_test_entry,back,pf_test_enter_btn,pf_test_answer_lbl):
    hide_words()
    hide_frames()
    pf_quiz_frame.pack(fill = "both", expand = 1)
    pf_question_lbl.pack(pady = 3)
    pf_box_lbl.pack()
    pf_test_enter_btn.pack()
    attempt = pf_test_entry.get()
    correct_pf = QuizClass(num1,None,attempt).find_pf_result()
    pf_test_answer_lbl = Label(pf_quiz_frame, text = correct_pf)
    pf_test_answer_lbl.pack(pady = 3)
    back.pack()
    flag = 0
    pf_test_clear = Button(pf_quiz_frame, text = "try again", command = lambda: clear_pf_test_lbls(flag, pf_test_entry,pf_question_lbl,pf_box_lbl,back,pf_test_enter_btn,pf_test_answer_lbl,pf_test_clear))
    pf_test_clear.pack(pady = 3)

def test_pf():
    """user can answer questions about pf"""
    hide_words()
    hide_frames()
    pf_quiz_frame.pack(fill = "both", expand = 1)
    num1,num2 = QuizClass().get_numbers()
    question = str(num1)
    pf_question_lbl = Label(pf_quiz_frame, text = question, font = (None, 22))
    pf_question_lbl.pack(pady = 3)
    pf_box_lbl = Label(pf_quiz_frame, text = "Prime Factorisation:")
    pf_box_lbl.pack()
    pf_test_entry = Entry(pf_quiz_frame)
    pf_test_entry.pack()
    attempt = pf_test_entry.get()
    pf_test_enter_btn = Button(pf_quiz_frame, text = "Enter", command = lambda: pf_test_results(num1,pf_question_lbl,pf_box_lbl,pf_test_entry,back,pf_test_enter_btn,pf_test_answer_lbl))
    pf_test_enter_btn.pack(pady = 3)
    flag = 1
    pf_test_answer_lbl = None
    pf_test_clear = None
    back = Button(pf_quiz_frame, text = "back", command = lambda: clear_pf_test_lbls(flag, pf_test_entry,pf_question_lbl,pf_box_lbl,back,pf_test_enter_btn,pf_test_answer_lbl,pf_test_clear))
    back.pack(pady = 10)

def try_quiz():
    """user can pick topic for quiz"""
    hide_words()
    hide_frames()
    quiz_frame.pack(fill = "both", expand = 1)

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
    if EntryChecker(num1).check_only_numbers() is False or EntryChecker(num2).check_only_numbers() is False:
        messagebox.showerror("Error", "only accepts whole numbers more than zero (no spaces)")
    else:
        gcf_list = list(GcfClass(num1,num2).gcf().split(" "))
        m = len(gcf_list)
        gcf_is = gcf_list[m-1]
        gcf_add_answer = Label(gcf_frame, text = GcfClass(num1,num2).gcf())
        gcf_add_answer.grid(row = 6, column = 1, columnspan = 2)
        gcf_clear_frame = Button(gcf_frame, text = "clear", command = lambda: gcf_clear(gcf_add_answer))
        gcf_clear_frame.grid(row = 4, column = 3)
        SearchHistory(user_entry.get(),num1,num2,gcf_is, "gcf: ").edit_hist()

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
    if EntryChecker(num1).check_only_numbers() is False or EntryChecker(num2).check_only_numbers() is False:
        messagebox.showerror("Error", "only accepts whole numbers more than zero (no spaces)")
    else:
        lcm_list = list(LcmClass(num1,num2).lcm().split(" "))
        m = len(lcm_list)
        lcm_is = lcm_list[m-1]
        lcm_add_answer = Label(lcm_frame, text = LcmClass(num1,num2).lcm())
        lcm_add_answer.grid(row = 6, column = 1, columnspan = 2)
        lcm_clear_frame = Button(lcm_frame, text = "clear", command = lambda: lcm_clear(lcm_add_answer))
        lcm_clear_frame.grid(row = 4, column = 3)
        SearchHistory(user_entry.get(),num1,num2,lcm_is, "lcm: ").edit_hist()

def pf_clear(pf_add_answer):
    """clears pf frame"""
    pf_entryBox1.delete(0, END)
    hide_words()
    hide_frames()
    pf_frame.pack(fill = "both", expand = 1)
    pf_add_answer.destroy()

def pf_calculation():
    """shows pf result"""
    num1 = pf_entryBox1.get()
    num2 = None
    if EntryChecker(num1).check_only_numbers() is False:
        messagebox.showerror("Error", "only accepts whole numbers more than zero (no spaces)")
    else:
        num1 = pf_entryBox1.get()
        num2 = None
        pf_list = PfClass(num1).pf()
        pf_is = " "
        for i in range(0,len(pf_list)):
            if i != len(pf_list)-1:
                pf_is = pf_is + str(pf_list[i]) + " x "
            else:
                pf_is = pf_is + str(pf_list[i])
        pf_is = pf_is + " = " + num1
        pf_add_answer = Label(pf_frame, text = pf_is)
        pf_add_answer.grid(row = 6, column = 1, columnspan = 2)
        pf_clear_frame = Button(pf_frame, text = "clear", command = lambda: pf_clear(pf_add_answer))
        pf_clear_frame.grid(row = 3, column = 3)
        SearchHistory(user_entry.get(),num1,num2,pf_is, "pf:").edit_hist()

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
    username = userCreate_entry.get()
    pass1 = pass1_entry.get()
    pass2 = pass2_entry.get()
    account_error_value = AccountCreation(username, pass1, pass2).account_check()
    if account_error_value == 1:
        messagebox.showerror("Error", "Passwords don't match")
    if account_error_value == 2:
        messagebox.showerror("Error", "Must contain a number")
    if account_error_value == 3:
        messagebox.showerror("Error", "Must contain a letter")
    if account_error_value == 4:
        messagebox.showerror("Error", "Account Already Exists")
    if account_error_value == 0:
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
    history_frame.pack_forget()
    quiz_frame.pack_forget()
    gcf_quiz_frame.pack_forget()
    lcm_quiz_frame.pack_forget()
    pf_quiz_frame.pack_forget()

def hide_words():
    """clears words from the frames"""
    welcome_lbl.pack_forget()
    create_btn.pack_forget()
    login_btn.pack_forget()
    exit_btn.pack_forget()

def back():
    """returns to welcome page"""
    hide_frames()
    welcome_lbl.pack()
    login_btn.pack(pady = 3)
    create_btn.pack(pady = 3)
    exit_btn.pack(pady = 3)

def exit_function():
    """leaves program"""
    exit()

if __name__ == "__main__":
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

    #makes exit button
    exit_btn = Button(root, text = "Exit", command = exit_function)
    exit_btn.pack(pady = 3)

    #creats the different frames
    create_frame = Frame(root, width = 400, height = 400)
    login_frame = Frame(root, width = 400, height = 400)
    menu_frame = Frame(root, width = 400, height = 400)
    gcf_frame = Frame(root, width = 400, height = 400)
    lcm_frame = Frame(root, width = 400, height = 400)
    pf_frame = Frame(root, width = 400, height = 400)
    history_frame = Frame(root, width = 400, height = 400)
    quiz_frame = Frame(root, width = 400, height = 400)
    gcf_quiz_frame = Frame(root, width = 400, height = 400)
    lcm_quiz_frame = Frame(root, width = 400, height = 400)
    pf_quiz_frame = Frame(root, width = 400, height = 400)

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

    quiz_btn = Button(menu_frame, text = "Test Yourself", command = try_quiz)
    quiz_btn.pack(pady = 3)

    history_btn = Button(menu_frame, text = "Search History", command = see_history)
    history_btn.pack(pady = 3)

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

    #pf frame
    pf_lbl = Label(pf_frame, text = "Prime Factorisation")
    pf_lbl.grid(row = 1, column = 1, columnspan = 2)

    pf_first_lbl = Label(pf_frame, text = "enter number: ")
    pf_first_lbl.grid(row = 2, column = 1)

    pf_entryBox1 = Entry(pf_frame)
    pf_entryBox1.grid(row = 2, column = 2)

    pf_enter = Button(pf_frame, text = "Calculate", width = 30, command = pf_calculation)
    pf_enter.grid(row = 3, column = 1, columnspan = 2)

    pf_back = Button(pf_frame, text = "back", command = math_menu)
    pf_back.grid(row = 4, column = 3)

    #history frame
    hist_title_lbl = Label(history_frame, text = "Search History", font = (None, 22))
    hist_title_lbl.pack(pady = 3)

    #quiz menu
    quiz_title_lbl = Label(quiz_frame, text = "Test your Knowledge", font = (None, 22))
    quiz_title_lbl.pack(pady = 3)

    gcf_quiz_btn = Button(quiz_frame, text = "Greatest Common Factor", command = test_gcf)
    gcf_quiz_btn.pack(pady = 3)

    lcm_quiz_btn = Button(quiz_frame, text = "Lowest Common Multiple", command = test_lcm)
    lcm_quiz_btn.pack(pady = 3)

    pf_quiz_btn = Button(quiz_frame, text = "Prime Factorisation", command = test_pf)
    pf_quiz_btn.pack(pady = 3)

    quiz_back = Button(quiz_frame, text = "back", command = math_menu)
    quiz_back.pack(pady = 3)

    root.mainloop()
#<3
