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

class UI():
    def gcf(self):
        """shows greatest common factor frame"""
        self.gcf_entryBox1.delete(0, END)
        self.gcf_entryBox2.delete(0, END)
        self.hide_words()
        self.hide_frames()
        self.gcf_frame.pack(fill = "both", expand = 1)

    def lcm(self):
        """shows lowest common factor frame"""
        self.hide_words()
        self.hide_frames()
        self.lcm_frame.pack(fill = "both", expand = 1)

    def pf(self):
        """shows prime factorisation frame"""
        self.hide_words()
        self.hide_frames()
        self.pf_frame.pack(fill = "both", expand = 1)

    def login(self):
        """shows login frame"""
        self.user_entry.delete(0, END)
        self.pass_entry.delete(0, END)
        self.hide_words()
        self.hide_frames()
        self.login_frame.pack(fill = "both", expand = 1)

    def clear_history_frame(self):
        """clears history frame"""
        self.hide_words()
        self.hide_frames()
        self.history_frame.pack(fill = "both", expand = 1)
        self.hist_lbl.destroy()
        self.hist_back.destroy()
        self.math_menu()

    def see_history(self):
        """user can look at search history"""
        self.hide_words()
        self.hide_frames()
        self.history_frame.pack(fill = "both", expand = 1)
        history_text = FileReader(self.user_entry.get()).read_search_history()
        self.hist_lbl = Label(self.history_frame, text = history_text,bg = "#EAE0DA")
        self.hist_lbl.pack(pady = 3)
        self.hist_back = Button(self.history_frame, text = "back", bg = "#EAC7C7", command = lambda: self.clear_history_frame())
        self.hist_back.pack(pady = 3)

    def clear_gcf_test_lbls(self,flag):
        if hasattr(self, 'gcf_test_entry') is True:
            self.gcf_test_entry.pack_forget()
        if hasattr(self, 'gcf_box_lbl') is True:
            self.gcf_box_lbl.pack_forget()
        if hasattr(self, 'gcf_question_lbl') is True:
            self.gcf_question_lbl.pack_forget()
        if hasattr(self, 'back1') is True:
            self.back1.pack_forget()
        if hasattr(self, 'gcf_test_enter_btn') is True:
            self.gcf_test_enter_btn.pack_forget()
        if hasattr(self, 'gcf_test_answer_lbl') is True:
            self.gcf_test_answer_lbl.pack_forget()
        if hasattr(self, 'gcf_test_clear') is True:
            self.gcf_test_clear.pack_forget()
        if flag == 0:
            self.test_gcf()
        if flag == 1:
            self.try_quiz()

    def gcf_test_results(self,num1,num2):
        self.hide_words()
        self.hide_frames()
        self.gcf_quiz_frame.pack(fill = "both", expand = 1)
        flag = 2
        self.clear_gcf_test_lbls(flag)
        self.gcf_question_lbl.pack(pady = 3)
        self.gcf_box_lbl.pack()
        self.gcf_test_entry.pack()
        self.gcf_test_enter_btn.pack()
        attempt = self.gcf_test_entry.get()
        if EntryChecker(attempt).check_only_numbers() is False:
            messagebox.showerror("Error", "only accepts whole numbers more than zero (no spaces)")
            self.back1.pack()
        else:
            correct_gcf = QuizClass(num1,num2,attempt).find_gcf_result()
            self.gcf_test_answer_lbl = Label(self.gcf_quiz_frame, text = correct_gcf,bg = "#EAE0DA")
            self.gcf_test_answer_lbl.pack(pady = 3)
            self.back1.pack()
            flag = 0
            self.gcf_test_clear = Button(self.gcf_quiz_frame, text = "try again", bg = "#D5E3E8", command = lambda: self.clear_gcf_test_lbls(flag))
            self.gcf_test_clear.pack(pady = 3)

    def test_gcf(self):
        """user can answer questions about gcf"""
        self.hide_words()
        self.hide_frames()
        self.gcf_quiz_frame.pack(fill = "both", expand = 1)
        flag = 2
        self.clear_gcf_test_lbls(flag)
        num1,num2 = QuizClass().get_numbers()
        question = str(num1) + " , " + str(num2)
        self.gcf_question_lbl = Label(self.gcf_quiz_frame, text = question, font = (None, 22),bg = "#EAE0DA")
        self.gcf_question_lbl.pack(pady = 3)
        self.gcf_box_lbl = Label(self.gcf_quiz_frame, text = "Greatest Common Factor:",bg = "#EAE0DA")
        self.gcf_box_lbl.pack()
        self.gcf_test_entry = Entry(self.gcf_quiz_frame)
        self.gcf_test_entry.pack()
        attempt = self.gcf_test_entry.get()
        self.gcf_test_enter_btn = Button(self.gcf_quiz_frame, text = "Enter", bg = "#D5E3E8", command = lambda: self.gcf_test_results(num1,num2))
        self.gcf_test_enter_btn.pack(pady = 3)
        flag = 1
        self.back1 = Button(self.gcf_quiz_frame, text = "back", bg = "#EAC7C7", command = lambda: self.clear_gcf_test_lbls(flag))
        self.back1.pack(pady = 10)

    def clear_lcm_test_lbls(self, flag):
        if hasattr(self, 'lcm_test_entry') is True:
            self.lcm_test_entry.pack_forget()
        if hasattr(self, 'lcm_box_lbl') is True:
            self.lcm_box_lbl.pack_forget()
        if hasattr(self, 'lcm_question_lbl') is True:
            self.lcm_question_lbl.pack_forget()
        if hasattr(self, 'back2') is True:
            self.back2.pack_forget()
        if hasattr(self, 'lcm_test_enter_btn') is True:
            self.lcm_test_enter_btn.pack_forget()
        if hasattr(self, 'lcm_test_answer_lbl') is True:
            self.lcm_test_answer_lbl.pack_forget()
        if hasattr(self, 'lcm_test_clear') is True:
            self.lcm_test_clear.pack_forget()
        if flag == 0:
            self.test_lcm()
        if flag == 1:
            self.try_quiz()

    def lcm_test_results(self, num1, num2):
        self.hide_words()
        self.hide_frames()
        self.lcm_quiz_frame.pack(fill = "both", expand = 1)
        flag = 2 
        self.clear_lcm_test_lbls(flag)
        self.lcm_question_lbl.pack(pady = 3)
        self.lcm_box_lbl.pack()
        self.lcm_test_entry.pack()
        self.lcm_test_enter_btn.pack()
        attempt = self.lcm_test_entry.get()
        if EntryChecker(attempt).check_only_numbers() is False:
            messagebox.showerror("Error", "only accepts whole numbers more than zero (no spaces)")
            self.back2.pack()
        else:
            correct_lcm = QuizClass(num1,num2,attempt).find_lcm_result()
            self.lcm_test_answer_lbl = Label(self.lcm_quiz_frame, text = correct_lcm,bg = "#EAE0DA")
            self.lcm_test_answer_lbl.pack(pady = 3)
            self.back2.pack()
            flag = 0
            self.lcm_test_clear = Button(self.lcm_quiz_frame, text = "try again", bg = "#D5E3E8", command = lambda: self.clear_lcm_test_lbls(flag))
            self.lcm_test_clear.pack(pady = 3)

    def test_lcm(self):
        """user can answer questions about lcm"""
        self.hide_words()
        self.hide_frames()
        self.lcm_quiz_frame.pack(fill = "both", expand = 1)
        flag = 2
        self.clear_lcm_test_lbls(flag)
        num1,num2 = QuizClass().get_numbers()
        question = str(num1) + " , " + str(num2)
        self.lcm_question_lbl = Label(self.lcm_quiz_frame, text = question, font = (None, 22),bg = "#EAE0DA")
        self.lcm_question_lbl.pack(pady = 3)
        self.lcm_box_lbl = Label(self.lcm_quiz_frame, text = "Lowest Common Multiple:",bg = "#EAE0DA")
        self.lcm_box_lbl.pack()
        self.lcm_test_entry = Entry(self.lcm_quiz_frame)
        self.lcm_test_entry.pack()
        attempt = self.lcm_test_entry.get()
        self.lcm_test_enter_btn = Button(self.lcm_quiz_frame, text = "Enter", bg = "#D5E3E8", command = lambda: self.lcm_test_results(num1,num2))
        self.lcm_test_enter_btn.pack(pady = 3)
        flag = 1
        self.back2 = Button(self.lcm_quiz_frame, text = "back", bg = "#EAC7C7", command = lambda: self.clear_lcm_test_lbls(flag))
        self.back2.pack(pady = 10)

    def clear_pf_test_lbls(self,flag):
        if hasattr(self, 'pf_test_entry') is True:
            self.pf_test_entry.pack_forget()
        if hasattr(self, 'pf_box_lbl') is True:
            self.pf_box_lbl.pack_forget()
        if hasattr(self, 'pf_question_lbl') is True:
            self.pf_question_lbl.pack_forget()
        if hasattr(self, 'back3') is True:
            self.back3.pack_forget()
        if hasattr(self, 'pf_test_enter_btn') is True:
            self.pf_test_enter_btn.pack_forget()
        if hasattr(self, 'pf_test_answer_lbl') is True:
            self.pf_test_answer_lbl.pack_forget()
        if hasattr(self, 'pf_test_clear') is True:
            self.pf_test_clear.pack_forget()
        if flag == 0:
            self.test_pf()
        if flag == 1:
            self.try_quiz()

    def pf_test_results(self,num1):
        self.hide_words()
        self.hide_frames()
        self.pf_quiz_frame.pack(fill = "both", expand = 1)
        flag = 2
        self.clear_pf_test_lbls(flag)
        self.pf_question_lbl.pack(pady = 3)
        self.pf_box_lbl.pack()
        self.pf_test_entry.pack()
        self.pf_test_enter_btn.pack()
        attempt = self.pf_test_entry.get()
        if len(attempt) == 0:
            messagebox.showerror("Error", "answer can't be empty")
            self.back3.pack()
        else:
            correct_pf = QuizClass(num1,None,attempt).find_pf_result()
            self.pf_test_answer_lbl = Label(self.pf_quiz_frame, text = correct_pf,bg = "#EAE0DA")
            self.pf_test_answer_lbl.pack(pady = 3)
            self.back3.pack()
            flag = 0
            self.pf_test_clear = Button(self.pf_quiz_frame, text = "try again", bg = "#D5E3E8", command = lambda: self.clear_pf_test_lbls(flag))
            self.pf_test_clear.pack(pady = 3)

    def test_pf(self):
        """user can answer questions about pf"""
        self.hide_words()
        self.hide_frames()
        self.pf_quiz_frame.pack(fill = "both", expand = 1)
        flag = 2
        self.clear_pf_test_lbls(flag)
        num1,num2 = QuizClass().get_numbers()
        if num1 == 1:
            num1 += 1
        question = str(num1)
        self.pf_question_lbl = Label(self.pf_quiz_frame, text = question, font = (None, 22),bg = "#EAE0DA")
        self.pf_question_lbl.pack(pady = 3)
        self.pf_box_lbl = Label(self.pf_quiz_frame, text = "List all Prime Factors (separated by spaces):",bg = "#EAE0DA")
        self.pf_box_lbl.pack()
        self.pf_test_entry = Entry(self.pf_quiz_frame)
        self.pf_test_entry.pack()
        attempt = self.pf_test_entry.get()
        self.pf_test_enter_btn = Button(self.pf_quiz_frame, text = "Enter", bg = "#D5E3E8", command = lambda: self.pf_test_results(num1))
        self.pf_test_enter_btn.pack(pady = 3)
        flag = 1
        self.back3 = Button(self.pf_quiz_frame, text = "back", bg = "#EAC7C7", command = lambda: self.clear_pf_test_lbls(flag))
        self.back3.pack(pady = 10)

    def try_quiz(self):
        """user can pick topic for quiz"""
        self.hide_words()
        self.hide_frames()
        self.quiz_frame.pack(fill = "both", expand = 1)

    def gcf_clear(self):
        """clears gcf frame"""
        self.gcf_entryBox1.delete(0, END)
        self.gcf_entryBox2.delete(0, END)
        self.hide_words()
        self.hide_frames()
        self.gcf_frame.pack(fill = "both", expand = 1)
        if hasattr(self, 'gcf_add_answer') is True:
            self.gcf_add_answer.destroy()

    def gcf_calculation(self):
        """shows gcf result"""
        num1 = self.gcf_entryBox1.get()
        num2 = self.gcf_entryBox2.get()
        self.gcf_clear()
        self.gcf_entryBox1.insert(0,num1)
        self.gcf_entryBox2.insert(0,num2)
        if EntryChecker(num1).check_only_numbers() is False or EntryChecker(num2).check_only_numbers() is False:
            messagebox.showerror("Error", "only accepts whole numbers more than zero (no spaces)")
        else:
            gcf_list = list(GcfClass(num1,num2).gcf().split(" "))
            m = len(gcf_list)
            gcf_is = gcf_list[m-1]
            self.gcf_add_answer = Label(self.gcf_frame, text = GcfClass(num1,num2).gcf(),bg = "#EAE0DA")
            self.gcf_add_answer.grid(row = 6, column = 1, columnspan = 2)
            self.gcf_clear_frame = Button(self.gcf_frame, text = "clear", bg = "#EAC7C7", command = lambda: self.gcf_clear())
            self.gcf_clear_frame.grid(row = 4, column = 3)
            SearchHistory(self.user_entry.get(),num1,num2,gcf_is, "gcf: ").edit_hist()

    def lcm_clear(self):
        """clears lcm frame"""
        self.lcm_entryBox1.delete(0, END)
        self.lcm_entryBox2.delete(0, END)
        self.hide_words()
        self.hide_frames()
        self.lcm_frame.pack(fill = "both", expand = 1)
        if hasattr(self,'lcm_add_answer') is True:
            self.lcm_add_answer.destroy()

    def lcm_calculation(self):
        """shows lcm results"""
        num1 = self.lcm_entryBox1.get()
        num2 = self.lcm_entryBox2.get()
        self.lcm_clear()
        self.lcm_entryBox1.insert(0,num1)
        self.lcm_entryBox2.insert(0,num2)
        if EntryChecker(num1).check_only_numbers() is False or EntryChecker(num2).check_only_numbers() is False:
            messagebox.showerror("Error", "only accepts whole numbers more than zero (no spaces)")
        else:
            lcm_list = list(LcmClass(num1,num2).lcm().split(" "))
            m = len(lcm_list)
            lcm_is = lcm_list[m-1]
            self.lcm_add_answer = Label(self.lcm_frame, text = LcmClass(num1,num2).lcm(),bg = "#EAE0DA")
            self.lcm_add_answer.grid(row = 6, column = 1, columnspan = 2)
            self.lcm_clear_frame = Button(self.lcm_frame, text = "clear", bg = "#EAC7C7", command = lambda: self.lcm_clear())
            self.lcm_clear_frame.grid(row = 4, column = 3)
            SearchHistory(self.user_entry.get(),num1,num2,lcm_is, "lcm: ").edit_hist()

    def pf_clear(self):
        """clears pf frame"""
        self.pf_entryBox1.delete(0, END)
        self.hide_words()
        self.hide_frames()
        self.pf_frame.pack(fill = "both", expand = 1)
        if hasattr(self,'pf_add_answer') is True:
            self.pf_add_answer.destroy()

    def pf_calculation(self):
        """shows pf result"""
        num1 = self.pf_entryBox1.get()
        num2 = None
        self.pf_clear()
        self.pf_entryBox1.insert(0,num1)
        if num1 == '1':
            messagebox.showerror("Error", "1 is not suitable for prime factorisation")
        elif EntryChecker(num1).check_only_numbers() is False:
            messagebox.showerror("Error", "only accepts whole numbers more than one (no spaces)")
        else:
            pf_list = PfClass(num1).pf()
            pf_is = " "
            for i in range(0,len(pf_list)):
                if i != len(pf_list)-1:
                    pf_is = pf_is + str(pf_list[i]) + " x "
                else:
                    pf_is = pf_is + str(pf_list[i])
            pf_is = pf_is + " = " + num1
            self.pf_add_answer = Label(self.pf_frame, text = pf_is,bg = "#EAE0DA")
            self.pf_add_answer.grid(row = 6, column = 1, columnspan = 2)
            self.pf_clear_frame = Button(self.pf_frame, text = "clear", bg = "#EAC7C7", command = lambda: self.pf_clear())
            self.pf_clear_frame.grid(row = 3, column = 3)
            SearchHistory(self.user_entry.get(),num1,num2,pf_is, "pf:").edit_hist()

    def enter_login(self):
        """enter function for login"""
        user = self.user_entry.get()
        password = self.pass_entry.get()
        correct_details = LoginClass(user, password).login_check()
        if correct_details is False:
            messagebox.showerror("Error", "Incorrect")
        else:
            self.math_menu()

    def enter_create(self):
        """enter function for create account"""
        username = self.userCreate_entry.get()
        pass1 = self.pass1_entry.get()
        pass2 = self.pass2_entry.get()
        if len(username) == 0:
            messagebox.showerror("Error","Please enter a username.")
        elif " " in username:
            messagebox.showerror("Error","No spaces")
        elif " " in pass1:
            messagebox.showerror("Error","No spaces")
        elif " " in pass2:
            messagebox.showerror("Error","No spaces")
        else:
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
                self.login()

    def create_account(self):
        """shows the account creation frame"""
        self.userCreate_entry.delete(0, END)
        self.pass1_entry.delete(0, END)
        self.pass2_entry.delete(0, END)
        self.hide_words()
        self.hide_frames()
        self.create_frame.pack(fill = "both", expand = 1)

    def math_menu(self):
        """shows the menu frame"""
        self.hide_words()
        self.hide_frames()
        self.menu_frame.pack(fill = "both", expand = 1)

    def hide_frames(self):
        """hides all frames"""
        self.create_frame.pack_forget()
        self.login_frame.pack_forget()
        self.menu_frame.pack_forget()
        self.gcf_frame.pack_forget()
        self.lcm_frame.pack_forget()
        self.pf_frame.pack_forget()
        self.history_frame.pack_forget()
        self.quiz_frame.pack_forget()
        self.gcf_quiz_frame.pack_forget()
        self.lcm_quiz_frame.pack_forget()
        self.pf_quiz_frame.pack_forget()

    def hide_words(self):
        """clears words from the frames"""
        self.welcome_lbl.pack_forget()
        self.create_btn.pack_forget()
        self.login_btn.pack_forget()
        self.exit_btn.pack_forget()

    def back(self):
        """returns to welcome page"""
        self.hide_frames()
        self.welcome_lbl.pack()
        self.login_btn.pack(pady = 3)
        self.create_btn.pack(pady = 3)
        self.exit_btn.pack(pady = 3)

    def exit_function(self):
        """leaves program"""
        exit()

    def run(self):
        self.root = Tk()
        self.root.title("Number Theory")
        self.root.geometry("400x400")
        self.root.config(bg = "#EAE0DA")

        self.welcome_lbl = Label(self.root, text = "Welcome", font = (None, 22), bg = "#EAE0DA")
        self.welcome_lbl.pack()

        #creates login button
        self.login_btn = Button(self.root, text = "Login", bg = "#D5E3E8", command = self.login)
        self.login_btn.pack(pady = 3)

        #makes create account button
        self.create_btn = Button(self.root, text = "Create Account", bg = "#D5E3E8", command = self.create_account)
        self.create_btn.pack(pady = 3)

        #makes exit button
        self.exit_btn = Button(self.root, text = "Exit", bg = "#EAC7C7", command = self.exit_function)
        self.exit_btn.pack(pady = 3)

        #creats the different frames
        self.create_frame = Frame(self.root, width = 400, height = 400,bg = "#EAE0DA")
        self.login_frame = Frame(self.root, width = 400, height = 400,bg = "#EAE0DA")
        self.menu_frame = Frame(self.root, width = 400, height = 400,bg = "#EAE0DA")
        self.gcf_frame = Frame(self.root, width = 400, height = 400,bg = "#EAE0DA")
        self.lcm_frame = Frame(self.root, width = 400, height = 400,bg = "#EAE0DA")
        self.pf_frame = Frame(self.root, width = 400, height = 400,bg = "#EAE0DA")
        self.history_frame = Frame(self.root, width = 400, height = 400,bg = "#EAE0DA")
        self.quiz_frame = Frame(self.root, width = 400, height = 400,bg = "#EAE0DA")
        self.gcf_quiz_frame = Frame(self.root, width = 400, height = 400,bg = "#EAE0DA")
        self.lcm_quiz_frame = Frame(self.root, width = 400, height = 400,bg = "#EAE0DA")
        self.pf_quiz_frame = Frame(self.root, width = 400, height = 400,bg = "#EAE0DA")

        #login
        self.login_lbl = Label(self.login_frame, text = "Login", font = (None, 22),bg = "#EAE0DA")
        self.login_lbl.grid(row = 0, column = 1)

        self.lbl_username = Label(self.login_frame, text = "Username:",bg = "#EAE0DA")
        self.lbl_username.grid(row = 1, column = 0)

        self.user_entry = Entry(self.login_frame)
        self.user_entry.grid(row = 1, column = 1)

        self.lbl_password = Label(self.login_frame, text = "Password:",bg = "#EAE0DA")
        self.lbl_password.grid(row = 2, column = 0)

        self.pass_entry = Entry(self.login_frame, show = "*")
        self.pass_entry.grid(row = 2, column = 1)

        self.enter_btn = Button(self.login_frame, text = "Enter", bg = "#D5E3E8", command = self.enter_login)
        self.enter_btn.grid(row = 3, column = 1)

        self.back_btn_login = Button(self.login_frame, text = "back", bg = "#EAC7C7", command = self.back)
        self.back_btn_login.grid(row = 4, column = 2)

        self.back_btn = Button(self.create_frame, text = "back", bg = "#EAC7C7", command = self.back)
        self.back_btn.grid(row = 5, column = 2)

        #create account
        self.create_lbl = Label(self.create_frame, text = "Create Account", font = (None, 22),bg = "#EAE0DA")
        self.create_lbl.grid(row = 0, column = 1)

        self.userCreate = Label(self.create_frame, text = "Create Username:",bg = "#EAE0DA")
        self.userCreate.grid(row = 1, column = 0)

        self.userCreate_entry = Entry(self.create_frame)
        self.userCreate_entry.grid(row = 1, column = 1)

        self.pass1_lbl = Label(self.create_frame, text = "Create Password:",bg = "#EAE0DA")
        self.pass1_lbl.grid(row = 2, column = 0)

        self.pass1_entry = Entry(self.create_frame, show = "*")
        self.pass1_entry.grid(row = 2, column = 1)

        self.pass2_lbl = Label(self.create_frame, text = "Confirm Password:",bg = "#EAE0DA")
        self.pass2_lbl.grid(row = 3, column = 0)

        self.pass2_entry = Entry(self.create_frame, show = "*")
        self.pass2_entry.grid(row = 3, column = 1)

        self.enter_btn = Button(self.create_frame, text = "Enter", bg = "#D5E3E8", command = self.enter_create)
        self.enter_btn.grid(row = 4, column = 1)

        #math menu
        self.menu_lbl = Label(self.menu_frame, text = "Menu", font = (None, 22),bg = "#EAE0DA")
        self.menu_lbl.pack()

        self.gcf_btn = Button(self.menu_frame, text = "Greatest Common Factor", bg = "#D5E3E8", command = self.gcf)
        self.gcf_btn.pack(pady = 3)

        self.lcm_btn = Button(self.menu_frame, text = "Lowest Common Multiple", bg = "#D5E3E8", command = self.lcm)
        self.lcm_btn.pack(pady = 3)

        self.pf_btn = Button(self.menu_frame, text = "Prime Factorisation", bg = "#D5E3E8", command = self.pf)
        self.pf_btn.pack(pady = 3)

        self.quiz_btn = Button(self.menu_frame, text = "Test Yourself", bg = "#D5E3E8", command = self.try_quiz)
        self.quiz_btn.pack(pady = 3)

        self.history_btn = Button(self.menu_frame, text = "Search History", bg = "#D5E3E8", command = self.see_history)
        self.history_btn.pack(pady = 3)

        self.logOut_btn = Button(self.menu_frame, text = "Log Out", bg = "#EAC7C7", command = self.back)
        self.logOut_btn.pack(pady = 3)

        #gcf frame
        self.gcf_lbl = Label(self.gcf_frame, text = "Greatest Common Factor",bg = "#EAE0DA")
        self.gcf_lbl.grid(row = 1, column = 1, columnspan = 2)

        self.gcf_first_lbl = Label(self.gcf_frame, text = "first number: ",bg = "#EAE0DA")
        self.gcf_first_lbl.grid(row = 2, column = 1)

        self.gcf_entryBox1 = Entry(self.gcf_frame)
        self.gcf_entryBox1.grid(row = 2, column = 2)

        self.gcf_second_lbl = Label(self.gcf_frame, text = "second number: ",bg = "#EAE0DA")
        self.gcf_second_lbl.grid(row = 3, column = 1)

        self.gcf_entryBox2 = Entry(self.gcf_frame)
        self.gcf_entryBox2.grid(row = 3, column = 2)

        self.gcf_enter = Button(self.gcf_frame, text = "Calculate", bg = "#D5E3E8", width = 30, command = self.gcf_calculation)
        self.gcf_enter.grid(row = 4, column = 1, columnspan = 2)

        self.gcf_back = Button(self.gcf_frame, text = "back", bg = "#EAC7C7", command = self.math_menu)
        self.gcf_back.grid(row = 5, column = 3)

        #lcm frame
        self.lcm_lbl = Label(self.lcm_frame, text = "Lowest Common Multiple",bg = "#EAE0DA")
        self.lcm_lbl.grid(row = 1, column = 1, columnspan = 2)

        self.lcm_first_lbl = Label(self.lcm_frame, text = "first number: ",bg = "#EAE0DA")
        self.lcm_first_lbl.grid(row = 2, column = 1)

        self.lcm_entryBox1 = Entry(self.lcm_frame)
        self.lcm_entryBox1.grid(row = 2, column = 2)

        self.lcm_second_lbl = Label(self.lcm_frame, text = "second number: ",bg = "#EAE0DA")
        self.lcm_second_lbl.grid(row = 3, column = 1)

        self.lcm_entryBox2 = Entry(self.lcm_frame)
        self.lcm_entryBox2.grid(row = 3, column = 2)

        self.lcm_enter = Button(self.lcm_frame, text = "Calculate", bg = "#D5E3E8", width = 30, command = self.lcm_calculation)
        self.lcm_enter.grid(row = 4, column = 1, columnspan = 2)

        self.lcm_back = Button(self.lcm_frame, text = "back", bg = "#EAC7C7", command = self.math_menu)
        self.lcm_back.grid(row = 5, column = 3)

        #pf frame
        self.pf_lbl = Label(self.pf_frame, text = "Prime Factorisation",bg = "#EAE0DA")
        self.pf_lbl.grid(row = 1, column = 1, columnspan = 2)

        self.pf_first_lbl = Label(self.pf_frame, text = "enter number: ",bg = "#EAE0DA")
        self.pf_first_lbl.grid(row = 2, column = 1)

        self.pf_entryBox1 = Entry(self.pf_frame)
        self.pf_entryBox1.grid(row = 2, column = 2)

        self.pf_enter = Button(self.pf_frame, text = "Calculate", bg = "#D5E3E8", width = 30, command = self.pf_calculation)
        self.pf_enter.grid(row = 3, column = 1, columnspan = 2)

        self.pf_back = Button(self.pf_frame, text = "back", bg = "#EAC7C7", command = self.math_menu)
        self.pf_back.grid(row = 4, column = 3)

        #history frame
        self.hist_title_lbl = Label(self.history_frame, text = "Search History", font = (None, 22),bg = "#EAE0DA")
        self.hist_title_lbl.pack(pady = 3)

        #quiz menu
        self.quiz_title_lbl = Label(self.quiz_frame, text = "Test your Knowledge", font = (None, 22),bg = "#EAE0DA")
        self.quiz_title_lbl.pack(pady = 3)

        self.gcf_quiz_btn = Button(self.quiz_frame, text = "Greatest Common Factor", bg = "#D5E3E8", command = self.test_gcf)
        self.gcf_quiz_btn.pack(pady = 3)

        self.lcm_quiz_btn = Button(self.quiz_frame, text = "Lowest Common Multiple", bg = "#D5E3E8", command = self.test_lcm)
        self.lcm_quiz_btn.pack(pady = 3)

        self.pf_quiz_btn = Button(self.quiz_frame, text = "Prime Factorisation", bg = "#D5E3E8", command = self.test_pf)
        self.pf_quiz_btn.pack(pady = 3)

        self.quiz_back = Button(self.quiz_frame, text = "back", bg = "#EAC7C7", command = self.math_menu)
        self.quiz_back.pack(pady = 3)

        self.root.mainloop()
    #<3
