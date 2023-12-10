from random import randint
from functionality.operations import GcfClass

class QuizClass():
    """gets question numbers for quizs"""
    def __init__(self,num1 = None ,num2 = None,attempt = None):
        self.num1 = num1
        self.num2 = num2
        self.attempt = attempt

    def get_numbers(self):
        """gets random numbers"""
        num1 = randint(1,99)
        num2 = randint(1,99)
        return num1,num2

    def find_gcf_result(self):
        gcf_list = list(GcfClass(self.num1,self.num2).gcf().split(" "))
        m = len(gcf_list)
        gcf_is = gcf_list[m-1]
        if gcf_is == self.attempt:
            return "Correct"
        incorrect_str = "Incorrect. Correct answer is: " + gcf_is
        return incorrect_str
            