"""File for quiz functionality."""
from random import randint
from functionality.operations import GcfClass
from functionality.operations import LcmClass
from functionality.operations import PfClass

class QuizClass():
    """Class handles quiz questions and answers.

    Attributes: 
        __num1: the first number in the question.
        __num2: the second number in the question.
        __attempt: the users attempt at the answer.
    """

    def __init__(self,num1 = None ,num2 = None,attempt = None):
        """Contructor, makes new quiz object.

        Args:
            num1: the first number in the question.
            num2: the second number in the question.
            attempt: the users attempt at the answer.
        """

        self.__num1 = num1
        self.__num2 = num2
        self.__attempt = attempt

    def get_numbers(self):
        """generates random numbers.
        
        Returns:
            Two whole numbers between 1 and 99.
        """

        num1 = randint(1,99)
        num2 = randint(1,99)
        return num1,num2

    def find_gcf_result(self):
        """Gets gcf answer and compares it to the users answer.
        
        Returns: 
            String, that tells the user their quiz result.
        """

        gcf_list = list(GcfClass(self.__num1,self.__num2).gcf().split(" "))
        m = len(gcf_list)
        gcf_is = gcf_list[m-1]
        if gcf_is == self.__attempt:
            return "Correct"
        incorrect_str = "Incorrect. Correct answer is: " + gcf_is
        return incorrect_str

    def find_lcm_result(self):
        """Gets lcm answer and compares it to the users answer.
        
        Returns: 
            String, that tells the user their quiz result.
        """

        lcm_list = list(LcmClass(self.__num1,self.__num2).lcm().split(" "))
        m = len(lcm_list)
        lcm_is = lcm_list[m-1]
        if lcm_is == self.__attempt:
            return "Correct"
        incorrect_str = "Incorrect. Correct answer is: " + lcm_is
        return incorrect_str

    def find_pf_result(self):
        """Gets pf answer and compares it to the users answer.
        
        Returns: 
            String, that tells the user their quiz result.
        """

        pf_is = PfClass(self.__num1).pf()
        attempt = str(self.__attempt).split(" ")
        input_len = len(attempt)
        print(attempt)
        for i in range(input_len-1):
            for j in range(0,input_len-i-1):
                if attempt[j] > attempt[j+1]:
                    swapped = True
                    attempt[j],attempt[j+1] = attempt[j+1],attempt[j]
            if not swapped:
                pass
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
            