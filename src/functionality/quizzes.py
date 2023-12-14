from random import randint
from functionality.operations import GcfClass
from functionality.operations import LcmClass
from functionality.operations import PfClass

class QuizClass():
    """gets question numbers for quizs"""
    def __init__(self,num1 = None ,num2 = None,attempt = None):
        self.__num1 = num1
        self.__num2 = num2
        self.__attempt = attempt

    def get_numbers(self):
        """gets random numbers"""
        num1 = randint(1,99)
        num2 = randint(1,99)
        return num1,num2

    def find_gcf_result(self):
        """gets gcf answer and compares it to the users answer"""
        gcf_list = list(GcfClass(self.__num1,self.__num2).gcf().split(" "))
        m = len(gcf_list)
        gcf_is = gcf_list[m-1]
        if gcf_is == self.__attempt:
            return "Correct"
        incorrect_str = "Incorrect. Correct answer is: " + gcf_is
        return incorrect_str

    def find_lcm_result(self):
        """gets lcm answer and compares it to the users answer"""
        lcm_list = list(LcmClass(self.__num1,self.__num2).lcm().split(" "))
        m = len(lcm_list)
        lcm_is = lcm_list[m-1]
        if lcm_is == self.__attempt:
            return "Correct"
        incorrect_str = "Incorrect. Correct answer is: " + lcm_is
        return incorrect_str

    def find_pf_result(self):
        """gets pf answer and compares it to the users answer"""
        pf_is = PfClass(self.__num1).pf()
        attempt = str(self.__attempt).split(" ")
        input_len = len(attempt)
        if input_len != len(pf_is):
            incorrect_str = "Incorrect. Correct answer is: " + str(pf_is)
            return incorrect_str
        for i in range(0, input_len-1):
            if attempt[i] == str(pf_is[i]):
                pass
            else:
                incorrect_str = "Incorrect. Correct answer is: " + str(pf_is)
                return incorrect_str
        return "Correct"
            